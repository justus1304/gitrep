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


#def plot_temperaturdifferenz():
#    # Ergebnisse laden
#    daten = np.genfromtxt("Daten/T1T4NEU.txt", unpack = True)
#    
#    # Plot erstellen
#    plt.figure(figsize=(10, 6))
#    plt.plot(zeit, delta_T, label='Temperaturdifferenz $\Delta T = T1 - T2$', color='blue')
#    plt.xlabel('Zeit [s]')
#    plt.ylabel('Temperaturdifferenz [°C]')
#    plt.title('Temperaturdifferenz über die Zeit')
#    plt.legend()
#    plt.grid(True)
#    
#    # Plot speichern
#    plt.savefig('plot_differenz.pdf')
#plot_temperaturdifferenz()

#Dynamische methode Messing
def messing():
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    t, T_1, T_2 = np.genfromtxt("Daten/messing.txt", unpack=True)
    #x aus differenz bilden(Aufgabenspezifisch)
    #fig, ax = plt.subplots(1, 1, layout="constrained")
    #x-Achse anzeigebereich
    x_plot = np.linspace(0,1000)
    # ??
    fig, ax = plt.subplots(1, 1, layout="constrained")
    #label der Messwerte
    ax.plot(t, T_1, "kx", label="T_1",markersize=1,)
    ax.plot(t, T_2, "rx", label="T_2",markersize=1,)
    ax.grid(True)

    #Legende anzeigen lassen (labels)
    ax.legend()
    #ax.set_xlim(0.0026, 0.00345)
    #Achsenbeschriftungen
    #ax.set(xlabel=r"t/\unit{\sec}$ ", ylabel=r"$T/unit{\degree\celsius}$");
    fig.savefig("build/messingPlot.pdf")
messing()