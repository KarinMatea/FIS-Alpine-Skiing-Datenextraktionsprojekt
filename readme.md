# FIS Alpine Skiing Datenextraktionsprojekt und Datenvisualisierung

## Projektübersicht

Dieses Python-Projekt extrahiert Daten von der FIS Alpine Skiing Website, speziell die Cup-Standings und speichert diese in einer Excel-Datei. Es nutzt Selenium für das Web Scraping und Pandas für die Datenverarbeitung.

## Datenvisualisierung

Das Projekt beinhaltet nun auch Funktionen zur Datenvisualisierung, die es ermöglichen, die extrahierten Daten grafisch darzustellen. Dies wird durch die Verwendung von Python-Bibliotheken wie Matplotlib und Seaborn erreicht.


## Systemanforderungen

- Python 3
- Pip (Python Package Installer)
- Google Chrome Browser
- Chrome WebDriver

## Anwendung
- Python und die Pakete Selenium, BeautifulSoup, Openpyxl, Matplotlib, Seaborn und pandas werden benötigt.
- Das Skript extrahiert Daten von der FIS-Website und speichert sie in einer Excel-Datei.

### Schritt 1: Umgebung vorbereiten

- **Repository klonen**:
  ```bash
  git clone [URL Ihres Repositories]
  cd [Name Ihres Projektverzeichnisses]
  ```

- **Virtuelle Umgebung erstellen und aktivieren**:
  ```bash
  python -m venv venv
  venv\Scripts\activate  # Windows
  source venv/bin/activate  # MacOS/Linux
  ```

- **Erforderliche Pakete installieren**:
  ```bash
  pip install selenium beautifulsoup4 pandas openpyxl
  ```

- **Chrome WebDriver herunterladen**:
  Laden Sie eine mit Ihrer Chrome-Version kompatible Version des Chrome WebDrivers herunter und speichern Sie ihn in einem bekannten Verzeichnis.(Version .119 benötigt)

### Schritt 2: Konfiguration

- **Setzen des WebDriver-Pfades** in der `scrape_fis_data.py`:
  ```python
  webdriver_path = r'Ihr\Chromedriver\Pfad\chromedriver.exe'
  ```

### Schritt 3: Ausführung

- **Starten des Skripts**:
  ```bash
  python scrape_fis_data.py
  ```

## Projektstruktur

- `scrape_fis_data.py`: Hauptscript für Web Scraping und Datenverarbeitung.
- `README.md`: Projektdokumentation.
- `requirements.txt`: Liste der benötigten Python-Pakete.

## Beiträge und Entwicklung

- **Pull-Requests**: Bei Verbesserungen oder Fehlerbehebungen erstellen Sie bitte Pull-Requests.
- **Feedback**: Für Feedback oder Vorschläge erstellen Sie bitte ein Issue im Repository.

## Autor

KMP

---

### Hinweise:

- Ersetzen Sie `[URL Ihres Repositories]` und `[Name Ihres Projektverzeichnisses]` mit den entsprechenden Informationen.
- Passen Sie den Pfad zum Chrome WebDriver entsprechend an.
- Wählen Sie eine Lizenz, die zu Ihrem Projekt passt, und fügen Sie diese im Lizenzbereich ein.
- Ergänzen Sie Ihren Namen im Abschnitt Autor.
