import matplotlib.pyplot as plt
import numpy as np

from uncertainties import ufloat

import uncertainties.unumpy as unp
from scipy.stats import sem

def verlaufT1T4():
    # 1. Daten einlesen mit genfromtxt
    # Angenommen, die Datei hat Spalten: Zeit, Temperatur T1, Temperatur T4.
    # Überspringen der Kopfzeile (falls vorhanden) mit `skip_header=1`.

    zeit, temp_t1, temp_t4 = np.genfromtxt('Daten/T1T4.txt', unpack=True)

    # 2. Spalten in Variablen speichern
    #zeit = daten[:, 0]   # Erste Spalte: Zeit t in s
    #temp_t1 = daten[:, 1]  # Zweite Spalte: Temperatur T1 in °C
    #temp_t4 = daten[:, 2]  # Dritte Spalte: Temperatur T4 in °C

    # 3. Figure und Achse explizit erstellen
    fig, ax = plt.subplots(figsize=(10, 6))

    # 4. Daten plotten
    ax.plot(zeit, temp_t1, label='Temperatur T1 (°C)', color='red', marker='o')
    ax.plot(zeit, temp_t4, label='Temperatur T4 (°C)', color='blue', marker='x')

    ax.set_xlim(0, 900)  # x-Achse von 0 bis 1500
    ax.set_ylim(0, 50)    # y-Achse von 0 bis 45

    # 5. Diagramm beschriften
    ax.set_title('Temperaturverlauf über die Zeit')
    ax.set_xlabel('Zeit (s)')
    ax.set_ylabel('Temperatur (°C)')
    ax.legend()
    ax.grid(True)

    # 5. Plot speichern
    fig.savefig("build/tempverlaufT1T4.pdf")

verlaufT1T4()


