# -*- coding: utf-8 -*-
# Rainer brell <nvda@brell.net>
# total Commander extended 
import re
import appModuleHandler
import controlTypes
import braille
import winUser
from NVDAObjects import NVDAObject

_LB_GETCURSEL = 0x0188  # index of the focused item (0-based)
_LB_GETCOUNT  = 0x018B  # total number of list items

class _LCLListBrailleRegion(braille.NVDAObjectRegion):
	"""Braille region that prepends the first letter of the parent list's name.

	Lowercase when the item is not selected; uppercase when selected.
	braille.Region.update() must be called after modifying rawText so the
	braille cells are re-translated from the new text.
	"""

	def update(self):
		super().update()
		try:
			obj = self.obj
			original = self.rawText

			# 1. Replace localized position text ("7 von 14", "7 of 14", …) with "7/14".
			#    Using the exact numbers from positionInfo makes the match
			#    language-independent and prevents accidental hits on other digits.
			pos = obj.positionInfo
			index = pos.get("indexInGroup")
			count = pos.get("similarItemsInGroup")
			if index and count:
				# (?<!\d) / (?!\d) prevent matches inside larger numbers
				self.rawText = re.sub(
					rf'(?<!\d){index}\s+\w+(?:\s+\w+)?\s+{count}(?!\d)',
					f'{index}/{count}',
					self.rawText,
				)

			# 2. Prepend prefix letter from parent list name (braille only)
			parent = obj.parent
			if parent and parent.name:
				letter = parent.name[0]
				selected = controlTypes.State.SELECTED in obj.states
				prefix = letter.upper() if selected else letter.lower()
				self.rawText = prefix + " " + self.rawText

			# Re-translate to braille cells only when rawText actually changed
			if self.rawText != original:
				braille.Region.update(self)
		except Exception:
			pass

class LCLListBoxOverlay(NVDAObject):
	"""Overlay class for LCLListBox items in Total Commander.

	- Tab characters in the item name are replaced with spaces (speech and braille).
	- The prefix letter appears on the braille display only, not in speech.
	- positionInfo supplies index and total count for speech ("X of Y") and braille ("X/Y").
	"""

	@property
	def name(self):
		raw = super().name
		if raw:
			return raw.replace("\t", " ")
		return raw

	@property
	def positionInfo(self):
		# Prefer data already exposed by the accessibility layer
		info = super().positionInfo
		if info.get("indexInGroup") and info.get("similarItemsInGroup"):
			return info
		# Fallback: query the list box directly via standard Windows messages
		try:
			hwnd = self.windowHandle
			index = winUser.sendMessage(hwnd, _LB_GETCURSEL, 0, 0)
			count = winUser.sendMessage(hwnd, _LB_GETCOUNT, 0, 0)
			if index >= 0 and count > 0:
				return {
					"indexInGroup": index + 1,   # convert to 1-based
					"similarItemsInGroup": count,
				}
		except Exception:
			pass
		return {}

	def getBrailleRegions(self, review=False):
		region = _LCLListBrailleRegion(self)
		return [region]


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName == "LCLListBox":
			clsList.insert(0, LCLListBoxOverlay)
