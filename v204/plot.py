import matplotlib.pyplot as plt
import numpy as np

from uncertainties import ufloat

import uncertainties.unumpy as unp
from scipy.stats import sem

def verlaufT1T4():
    # 1. Daten einlesen mit genfromtxt
    # Angenommen, die Datei hat Spalten: Zeit, Temperatur T1, Temperatur T4.
    # Überspringen der Kopfzeile (falls vorhanden) mit `skip_header=1`.

    zeit, temp_T1, temp_T4 = np.genfromtxt('Daten/T1T4.txt', unpack=True)

    # 3. Figure und Achse explizit erstellen
    fig, ax = plt.subplots(figsize=(10, 6))

    # 4. Daten plotten
    ax.plot(zeit, temp_T1, label='Temperatur T1 (°C)', color='red', marker='o')
    ax.plot(zeit, temp_T4, label='Temperatur T4 (°C)', color='blue', marker='x')

    ax.set_xlim(0, 1000)  
    ax.set_ylim(0, 55)    

    # 5. Diagramm beschriften
    ax.set_title('Temperaturverlauf über die Zeit')
    ax.set_xlabel('Zeit (s)')
    ax.set_ylabel('Temperatur (°C)')
    ax.legend()
    ax.grid(True)

    # 5. Plot speichern
    fig.savefig("build/tempverlaufT1T4.pdf")
verlaufT1T4()

def verlaufT5T8():
    # 1. Daten einlesen mit genfromtxt
    # Angenommen, die Datei hat Spalten: Zeit, Temperatur T1, Temperatur T4.
    # Überspringen der Kopfzeile (falls vorhanden) mit `skip_header=1`.

    zeit, temp_T5, temp_T8 = np.genfromtxt('Daten/T5T8.txt', unpack=True)

    # 3. Figure und Achse explizit erstellen
    fig, ax = plt.subplots(figsize=(10, 6))

    # 4. Daten plotten
    ax.plot(zeit, temp_T5, label='Temperatur T5 (°C)', marker='o')
    ax.plot(zeit, temp_T8, label='Temperatur T8 (°C)', marker='x')

    ax.set_xlim(0, 1000)  
    ax.set_ylim(0, 55)    

    # 5. Diagramm beschriften
    ax.set_title('Temperaturverlauf über die Zeit')
    ax.set_xlabel('Zeit (s)')
    ax.set_ylabel('Temperatur (°C)')
    ax.legend()
    ax.grid(True)

    # 5. Plot speichern
    fig.savefig("build/tempverlaufT5T8.pdf")
verlaufT5T8()


