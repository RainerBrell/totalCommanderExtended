# Übersetzungsleitfaden für Übersetzer

## Übersicht

Viele NVDA-Add-ons verwenden das Crowdin-Projekt für NVDA-Add-ons („nvdaaddons“), um Übersetzungen zu verwalten.

Dieses Projekt ermöglicht es Übersetzern, sowohl Schnittstellenübersetzungen als auch Dokumentationsübersetzungen beizusteuern.

Übersetzungen werden über den von der NVDA-Add-on-Vorlage bereitgestellten Lokalisierungsworkflow wieder mit den Add-on-Repositorys synchronisiert.

## Treten Sie der Übersetzungs-Community bei

Bevor Übersetzer Übersetzungen beisteuern, sollten sie sich in die Mailingliste von NVDA Translations eintragen.

Die Mailingliste ist der wichtigste Ort für die Diskussion überübersetzungsbezogener Themen innerhalb der NVDA-Community.

## NVDA Translations-Mailingliste

Die NVDA-Community unterhält die Mailingliste NVDA Translations auf Groups.io.

Diese Mailingliste wird verwendet für:

* Besprechen Sie übersetzungsbezogene Themen.
* Fordern Sie Zugang zu Übersetzungsteams an.
* Koordinierung der Übersetzungsbemühungen.
* Übersetzungsprobleme melden.
* Besprechen Sie Probleme mit Übersetzungstools oder Arbeitsabläufen.

Übersetzern wird empfohlen, sich in die Mailingliste einzutragen:

https://groups.io/g/nvda-translations

Die Mailingliste ist oft der beste Ort, um Fragen zu stellen, Zugang zu einem Übersetzungsteam anzufordern und um Hilfe von anderen Übersetzern und Projektbetreuern zu bitten.

## Dem Übersetzungsprojekt beitreten

So tragen Sie Übersetzungen bei:

1. Erstellen Sie ein Crowdin-Konto.
1. Abonnieren Sie die Mailingliste von NVDA Translations.
1. Fordern Sie bei Bedarf Zugang zum entsprechenden Übersetzungsteam an.
1. Treten Sie dem NVDA Add-ons Crowdin-Projekt bei.
1. Wählen Sie die Sprache aus, die Sie übersetzen möchten.
1. Beginnen Sie mit der Übersetzung von Schnittstellenzeichenfolgen und Dokumentation.

## Übersetzungsmethoden

Übersetzungen können entweder über die Crowdin-Weboberfläche oder lokale Übersetzungstools durchgeführt werden.

### Crowdin Web-Editor

Crowdin bietet einen webbasierten Editor, der Übersetzern Folgendes ermöglicht:

* Übersetzen Sie Zeichenfolgen online.
* Überprüfen Sie vorhandene Übersetzungen.
* Verbesserungsvorschläge.
* Abstimmung über Übersetzungsvorschläge.

Diese Methode erfordert keine zusätzliche Softwareinstallation.

### Poedit

Viele NVDA-Übersetzer bevorzugen aufgrund der Zugänglichkeit und Benutzerfreundlichkeit die lokale Verwendung von [Poedit](https://poedit.com/).

Poedit unterstützt beides:

* Portable Object-Dateien (`.po`), die für Schnittstellenübersetzungen verwendet werden.
* XLIFF-Dateien („.xliff“), die für Dokumentationsübersetzungen verwendet werden.

Nachdem die Übersetzungen lokal abgeschlossen wurden, können die Dateien mit [l10nUtil.exe](https://github.com/nvaccess/nvdaL10n/releases/latest) wieder auf Crowdin hochgeladen werden.

## Interface-Strings übersetzen

Schnittstellenübersetzungen werden in Portable Object-Dateien (`.po`) gespeichert.

Diese Dateien können entweder übersetzt werden:

* Direkt in Crowdin.
* Mit Poedit.

## Dokumentation übersetzen

Dokumentationsübersetzungen werden in XLIFF-Dateien („.xliff“) gespeichert.

Diese Dateien werden automatisch aus der Add-on-Dokumentation generiert.

Dokumentation kann übersetzt werden:

* Direkt in Crowdin.
* Mit Poedit.Bei der Übersetzung von Dokumentationen:

* Übersetzen Sie nur den Textinhalt.
* Platzhalter und Formatierung beibehalten.
* Ändern Sie die XLIFF-Struktur nicht manuell.

## Offline-Übersetzungen hochladen

Nachdem die Dateien lokal übersetzt wurden, können sie mit [l10nUtil.exe](https://github.com/nvaccess/nvdaL10n/releases/latest) auf Crowdin hochgeladen werden.

Beispiele:

„cmd
l10nUtil.exe uploadTranslationFile fr addonName.po -c addon
„

„cmd
l10nUtil.exe uploadTranslationFile fr addonName.xliff -c addon
„

Wo:

* „fr“ ist der Crowdin-Sprachcode.
* „addonName.po“ ist eine übersetzte Schnittstellendatei.
* „addonName.xliff“ ist eine übersetzte Dokumentationsdatei.

Nach dem Hochladen stehen die Übersetzungen in Crowdin zur Verfügung und können später wieder mit dem Add-on-Repository synchronisiert werden.

## Verwenden von l10nUtil.exe

So zeigen Sie die vollständige Liste der verfügbaren Befehle an:

„cmd
l10nUtil.exe --help
„

oder:

„cmd
l10nUtil.exe -h
„

So zeigen Sie Hilfe für einen bestimmten Befehl an:

„cmd
l10nUtil.exe downloadTranslationFile --help
„

oder:

„cmd
l10nUtil.exe downloadTranslationFile -h
„

Eine vollständige Liste der unterstützten Befehle und Optionen finden Sie in der Hilfeausgabe des Dienstprogramms.

## So funktioniert die Synchronisierung

Übersetzungen werden nicht sofort in GitHub-Repositorys importiert.

Der Add-on-Betreuer führt einen Synchronisierungsworkflow aus, der:

1. Stellt eine Verbindung zum NVDA Add-ons Crowdin-Projekt her.
1. Lädt abgeschlossene Übersetzungen herunter.
1. Überprüft den Prozentsatz der abgeschlossenen Übersetzung.
1. Synchronisiert geeignete Übersetzungen zurück in das Repository.

Abhängig von der Repository-Konfiguration werden Übersetzungen möglicherweise erst nach Erreichen eines Mindestabschlussprozentsatzes synchronisiert.

Dieser Schwellenwert wird vom Add-on-Betreuer gesteuert.

## Warum ist meine Übersetzung noch nicht erschienen?

Mögliche Gründe sind:

* Der Synchronisierungsworkflow wurde noch nicht ausgeführt.
* Der erforderliche Fertigstellungsgrad der Übersetzung wurde noch nicht erreicht.
* Der Betreuer hat die Synchronisierung vorübergehend deaktiviert.
* Die Übersetzung wurde nach dem letzten Synchronisierungszyklus abgeschlossen.

## Best Practices

So verbessern Sie die Übersetzungsqualität:

* Behalten Sie die Konsistenz mit der vorhandenen Terminologie bei.
* Platzhalter und Formatierung beibehalten.
* Überprüfen Sie vorhandene Übersetzungen, bevor Sie neue Terminologie einführen.
* Koordinieren Sie sich nach Möglichkeit mit anderen Übersetzern.
* Testen Sie übersetzte Dateien nach Möglichkeit lokal, bevor Sie sie hochladen.

## Probleme melden

Wenn Sie auf Übersetzungsprobleme stoßen:

* Wenden Sie sich an den Add-on-Betreuer.
* Öffnen Sie gegebenenfalls ein Problem im Add-on-Repository.
* Bitten Sie um Hilfe auf der Mailingliste von NVDA Translations.
* Besprechen Sie übersetzungsbezogene Probleme mit der NVDA-Übersetzungsgemeinschaft.

## Häufig gestellte Fragen

### Kann ich sowohl Dokumentation als auch Schnittstellenzeichenfolgen übersetzen?

Ja.

Das Crowdin-Projekt für NVDA-Add-ons unterstützt sowohl Schnittstellenübersetzungen (`.po`) als auch Dokumentationsübersetzungen (`.xliff`).### Muss ich die Crowdin-Weboberfläche verwenden?

Nein.

Viele Übersetzer arbeiten direkt in Crowdin, andere nutzen lieber Poedit und laden ihre fertigen Übersetzungen anschließend mit „l10nUtil.exe“ hoch.

Beide Ansätze werden vom NVDA Add-ons-Übersetzungsworkflow unterstützt.

### Benötige ich Zugriff auf GitHub?

Nicht unbedingt.

Die meisten Übersetzer arbeiten ausschließlich über Crowdin oder über lokale Übersetzungstools in Kombination mit „l10nUtil.exe“.

Der Synchronisierungsworkflow wird vom Add-on-Betreuer verwaltet und importiert Übersetzungen automatisch in GitHub-Repositorys.

### Kann ich die Synchronisierung erzwingen?

Nein.

Die Synchronisierung wird vom Add-on-Betreuer über den Lokalisierungsworkflow gesteuert, der von der NVDA-Add-on-Vorlage bereitgestellt wird.