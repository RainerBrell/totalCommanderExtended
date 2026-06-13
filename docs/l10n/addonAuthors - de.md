Übersetzungsleitfaden für Autoren

Überblick

Diese Vorlage unterstützt die Übersetzung von Add-ons mit Crowdin.

Crowdin-Projekteinrichtung

Sie benötigen ein Crowdin-Konto und einen API-Token mit Berechtigungen zur Verwaltung eines Projekts.
Wenn Sie das Community-Projekt Crowdin project to translate NVDA add-ons nutzen möchten:

   Zugang anfordern: Senden Sie eine Nachricht an die NVDA translation mailing list (nvda-translations@groups.io) oder an die NVDA Add-ons Mailing List (nvda-addons@groups.io), in der Sie um eine Einladung bitten, dem Projekt als Entwickler beizutreten.
   API-Token: Nach der Einladung generieren Sie einen API-Token in Ihren Crowdin-Kontoeinstellungen.

GitHub-Secrets und -Variablen

Damit die Workflows mit Crowdin kommunizieren können, müssen Sie das folgende Secret zu Ihrem GitHub-Repository hinzufügen (`Settings > Secrets and variables > Actions`):

   `CROWDINTOKEN`: Fügen Sie hier Ihren Crowdin-API-Token ein.

Optional, wenn Sie das Crowdin community project nicht nutzen möchten, können Sie Repository-Variablen unter Settings > Secrets and variables > Actions > Variables erstellen, indem Sie den Tab Variables auswählen und auf New repository variable klicken.

Die folgenden Repository-Variablen werden unterstützt:

   `CROWDINPROJECTID`: Fügen Sie hier die Projekt-ID Ihres Crowdin-Projekts ein.
   `L10NUTILCONFIG`: Der Pfad zur YAML-Datei, die die Konfiguration für `l10nUtil.exe` enthält, welche von den Übersetzungs-Skripten verwendet wird.
    Weitere Details finden Sie im nvdaL10n repository.
   `MINPERCENTAGETRANSLATED`: Definiert den erforderlichen Mindestprozentsatz der Übersetzungsfertigstellung, bevor eine übersetzte Datei zurück ins Repository synchronisiert wird.
    Der Wert muss zwischen `0` und `100` liegen.

Beispiele für `MINPERCENTAGETRANSLATED`:

   `50`: Importiert Dateien, die zu mindestens 50 % übersetzt sind.
   `75`: Importiert Dateien, die zu mindestens 75 % übersetzt sind.
   `100`: Importiert nur vollständig übersetzte Dateien.

Wenn `MINPERCENTAGETRANSLATED` nicht definiert ist, verwendet der Workflow einen Standardwert von `50`.

Infrastruktur

Stellen Sie sicher, dass Ihr Repository die folgenden Dateien enthält (in dieser Vorlage bereitgestellt):

   Workflows: `.github/workflows/crowdinL10n.yml`
   Skripte: Der Ordner `.github/scripts/`, der `checkTranslation.py`, `languageMappings.json`, `setOutputs.py` und `crowdinSync.ps1` enthält.

Die Dokumentationssynchronisation basiert auf der in `l10nUtil.exe` integrierten XLIFF-Unterstützung.

Der Befehl `md2xliff` wird verwendet, um die Quell-XLIFF-Datei aus der englischen Dokumentationsdatei `readme.md` zu generieren.
Übersetzte XLIFF-Dateien, die von Crowdin heruntergeladen wurden, werden dann mit `l10nUtil.exe xliff2md` wieder in Markdown-Dokumentation umgewandelt.

Ausführen des Workflows

Der Übersetzungs-Workflow wird wöchentlich ausgeführt.
Sie können den Workflow auch manuell von GitHub oder über die GitHub CLI ausführen.

Wenn Sie mehrere Add-ons verwalten, sollten Sie unterschiedliche Cron-Zeitpläne für jedes Repository in Betracht ziehen.
Obwohl der Workflow eine zufällige Startverzögerung enthält, um Kollisionen zu reduzieren, können dennoch gleichzeitige Crowdin-Synchronisationsaufträge auftreten.

Dokumentations- und Oberflächenübersetzungen werden nur synchronisiert, wenn ihr Übersetzungsanteil den konfigurierten Schwellenwert `MINPERCENTAGETRANSLATED` erreicht.

Dieser Validierungsmechanismus wird konsequent auf `.po`- und `.xliff`-Übersetzungsdateien angewendet.
