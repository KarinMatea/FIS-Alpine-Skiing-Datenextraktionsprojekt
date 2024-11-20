from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from datetime import datetime
import time

# Pfad zum Chromedriver
webdriver_path = r"C:\Users\chromedriver-win64\chromedriver.exe"


# URL der FIS Cup Standings
url = 'https://www.fis-ski.com/DB/alpine-skiing/cup-standings.html?sectorcode=AL&seasoncode=2024&cupcode=NC-WC&disciplinecode=ALL&gendercode=A&nationcode='

# Selenium Webdriver konfigurieren
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)


driver.get(url)

# Aktuellen Zeitstempel erzeugen
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

time.sleep(5)

# HTML-Inhalt abrufen
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')


driver.quit()

# Extrahieren des div-Elements mit der Klasse 'tbody'
tbody_div = soup.find('div', class_='tbody')

# Extrahieren aller Zeilen, die in <a class='table-row'> enthalten sind
rows = []
for row in tbody_div.find_all('a', class_='table-row'):
    # Namen des Landes
    container_div = row.find('div', class_='container g-row')
    name_div = container_div.find('div', class_='g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top') if container_div else None
    name = name_div.get_text(strip=True) if name_div else "Name nicht gefunden"

    # Land
    country_span = row.find('span', class_='country__name-short')
    country = country_span.text.strip() if country_span else "Land nicht gefunden"

    # Punkte

    points_div = row.find('div', class_='pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold')
    points = points_div.get_text(strip=True) if points_div else "Punkte nicht gefunden"

    rows.append([name, country, points])

# Erstellen eines DataFrame
headers = ['Name', 'Country', 'Points']
df = pd.DataFrame(rows, columns=headers)

# Globale Einstellungen anpassen
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = 'r'
mpl.rcParams['font.size'] = 12
mpl.rcParams['axes.labelsize'] = 15
mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10

# Erstelleung des Plots
plt.figure(figsize=(12, 6))
sns.boxplot(x='Country', y='Points', data=df)
plt.title('Punkteverteilung pro Land')

png_file_name = f"fis_visualization_{current_time}.png"

# Speichern der Visualisierung als PNG-Datei
plt.savefig(png_file_name)

print(f"Visualisierung gespeichert in: {png_file_name}")


file_name = f"fis_country_points_{current_time}.xlsx"

# Exportieren der Daten in eine Excel-Datei
df.to_excel(file_name, index=False)

print(f"Daten gespeichert in: {file_name}")




