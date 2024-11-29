import matplotlib.pyplot as plt
import numpy as np

from uncertainties import ufloat

import uncertainties.unumpy as unp
from scipy.stats import sem

def verlaufT1T4():
    # 1. Daten einlesen mit genfromtxt
    # Angenommen, die Datei hat Spalten: Zeit, Temperatur T1, Temperatur T4.
    # Überspringen der Kopfzeile (falls vorhanden) mit `skip_header=1`.

<<<<<<< HEAD
    zeit, temp_t1, temp_t4 = np.genfromtxt('Daten/T1T4.txt', unpack=True)

    # 2. Spalten in Variablen speichern
    #zeit = daten[:, 0]   # Erste Spalte: Zeit t in s
    #temp_t1 = daten[:, 1]  # Zweite Spalte: Temperatur T1 in °C
    #temp_t4 = daten[:, 2]  # Dritte Spalte: Temperatur T4 in °C
||||||| 908d01f
    daten = np.genfromtxt('Daten/T1T4.txt', unpack=True)

    # 2. Spalten in Variablen speichern
    zeit = daten[:, 0]   # Erste Spalte: Zeit t in s
    temp_t1 = daten[:, 1]  # Zweite Spalte: Temperatur T1 in °C
    temp_t4 = daten[:, 2]  # Dritte Spalte: Temperatur T4 in °C
=======
    zeit, temp_T1, temp_T4 = np.genfromtxt('Daten/T1T4.txt', unpack=True)
>>>>>>> refs/remotes/origin/main

    # 3. Figure und Achse explizit erstellen
    fig, ax = plt.subplots(figsize=(10, 6))

    # 4. Daten plotten
    ax.plot(zeit, temp_T1, label='Temperatur T1 (°C)', color='red', marker='o')
    ax.plot(zeit, temp_T4, label='Temperatur T4 (°C)', color='blue', marker='x')

<<<<<<< HEAD
    ax.set_xlim(0, 900)  # x-Achse von 0 bis 1500
    ax.set_ylim(0, 50)    # y-Achse von 0 bis 45
||||||| 908d01f
    ax.set_xlim(0, 1500)  # x-Achse von 0 bis 1500
    ax.set_ylim(0, 45)    # y-Achse von 0 bis 45
=======
    ax.set_xlim(0, 1000)  
    ax.set_ylim(0, 55)    
>>>>>>> refs/remotes/origin/main

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


