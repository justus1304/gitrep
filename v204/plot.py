import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from uncertainties import ufloat
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from scipy.stats import sem
#berechnung der Konstanten der Stäbe

#Abmessungen in cm
l_Mb = 9
b_Mb = 1.2
h_Mb = 0.4

l_A = 9
b_A = 1.2
h_A = 0.4

l_E = 9
b_E = 1.2
h_E = 0.4

#Dichte in kg/m^3
r_M = 8520
r_A = 2800
r_E = 8000

#wärmekapazitäten
c_M = 385
c_A = 830
c_E = 400

#Abstand Thermoelemente in (m)
dx = 0.03

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
    ax.set_xlabel('Zeit (s)')
    ax.set_ylabel('Temperatur (°C)')
    ax.legend()
    ax.grid(True)

    # 5. Plot speichern
    fig.savefig("build/tempverlaufT5T8.pdf")
verlaufT5T8()


def plot_temperaturdifferenz12():
   # Ergebnisse laden
   t, T1, T2 = np.genfromtxt("Daten/T1T2diff.txt", unpack = True)
   Delta_T = T2 - T1
   # Plot erstellen
   plt.figure(figsize=(10, 6))
   plt.plot(t, Delta_T, label='Temperaturdifferenz $\Delta T = T1 - T2$', color='blue')
   plt.xlabel('Zeit [s]')
   plt.ylabel('T [°C]')
   plt.legend()
   plt.grid(True)
   
   # Plot speichern
   plt.savefig("plotdiff12.pdf")
plot_temperaturdifferenz12()

def plot_temperaturdifferenz78():
   # Ergebnisse laden
   t, T7, T8 = np.genfromtxt("Daten/T7T8diff.txt", unpack = True)
   Delta_T = T7 - T8
   # Plot erstellen
   plt.figure(figsize=(10, 6))
   plt.plot(t, Delta_T, label='Temperaturdifferenz $\Delta T = T7 - T8$', color='blue')
   plt.xlabel('Zeit [s]')
   plt.ylabel('T [°C]')
   plt.legend()
   plt.grid(True)
   # Plot speichern
   plt.savefig("plotdiff78.pdf")
plot_temperaturdifferenz78()





#################################################################################################################################

#Dynamische methode Messing
def messing():
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    t, T_1, T_2 = np.genfromtxt("Daten/messing.txt", unpack=True)
    T_1 = T_1 + 273
    T_2 = T_2 + 273

    T_1peaks, _ = find_peaks(T_1, height=0)
    T_1lows, _ = find_peaks(-T_1)

    T_2peaks, _ = find_peaks(T_2, height=0)
    T_2lows, _ = find_peaks(-T_2)

    #x-Achse anzeigebereich
    x_plot = np.linspace(0,1000)
    # ??
    fig, ax = plt.subplots(1, 1, layout="constrained")
    #ploten der Meswerte und Maxima/Minima
    ax.plot(t, T_1, "kx", label="Temperatur $T_2$",markersize=1,)
    ax.plot(t, T_2, "rx", label="Temperatur $T_1$",markersize=1,)
    ax.plot(t[T_1peaks], T_1[T_1peaks], "rx", label='Maxima')
    ax.plot(t[T_1lows], T_1[T_1lows], "bx", label='Minima')

    ax.plot(t[T_2peaks], T_2[T_2peaks], "rx")
    ax.plot(t[T_2lows], T_2[T_2lows], "bx")
    ax.grid(True)

    #phasendifferenz in (s)
    pd = t[T_1peaks] - t[T_2peaks]
    print ("T1T2 Delta t (s)= ", pd)
    Mwpd = ufloat(np.mean(pd), stats.sem(pd))
    print("Mwpd = ", np.mean(pd), " +- ", stats.sem(pd))

    #Amplituden in (K)
#########################berechnung Amplituden A_nah
    A_nah = [0]*10
    i = 0
    while(i<=9):
        A_nah[i] = 0.5 * (T_1[T_1peaks][i+1] - 0.5 * (T_1[T_1peaks][i+1] - T_1[T_1lows][i]) - T_1[T_1lows][i])
        i = i + 1
#########################
    A_nah = np.array(A_nah)
    print("A_nah = ", A_nah)


#########################berechnung Amplituden A_fern
    A_fern = [0]*10
    i = 0
    while(i<=9):
        A_fern[i] = 0.5 * (T_2[T_2peaks][i+1] - 0.5 * (T_2[T_2peaks][i+1] - T_2[T_2lows][i]) - T_2[T_2lows][i])
        i = i + 1
#########################
    A_fern = np.array(A_fern)
    print("A_fern = ", A_fern)

    print("")
    print("MwA_nah = ", np.mean(A_nah), " +- ", stats.sem(A_nah))
    print("MwA_fern = ", np.mean(A_fern), " +- ", stats.sem(A_fern))

    #ln(anteil)

    #ln(anteil)
    lnan = np.log(A_fern/A_nah)
    print("ln(A_nah / A_fern) ", lnan)

    Mwln = ufloat(np.mean(lnan), stats.sem(lnan))
    print("Mwln(A_nah/A_fern) = ", Mwln)

    #berechnung der wärmeleitfähigkeit k
    k = (r_M * c_M * (dx)**2)/(2 * Mwpd * Mwln)
    print(k)
    ax.legend(markerscale = 2)
    ax.set(xlabel=r"$t/\unit{\second}$ ", ylabel=r"$T/\unit{\kelvin}$");
    fig.savefig("build/messingPlot.pdf")
messing()
print("")
print("")

###############
#Aluminium
###############
print("Werte für Aluminium")
#Dynamische methode Aluminium
def Aluminium():
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    t, T_5, T_6 = np.genfromtxt("Daten/Aluminium.txt", unpack=True)
    T_5 = T_5 + 273
    T_6 = T_6 + 273

    T_5peaks, _ = find_peaks(T_5, height=0)
    T_5lows, _ = find_peaks(-T_5)

    T_6peaks, _ = find_peaks(T_6, height=0)
    T_6lows, _ = find_peaks(-T_6)

    #x-Achse anzeigebereich
    x_plot = np.linspace(0,1000)
    # ??
    fig, ax = plt.subplots(1, 1, layout="constrained")
    #ploten der Meswerte und Maxima/Minima
    ax.plot(t, T_5, "kx", label="Temperatur $T_6$",markersize=1,)
    ###umgekehrte T1,T2 weil erst falsch und zu faul zum korrigieren 
    ax.plot(t, T_6, "rx", label="Temperatur $T_5$",markersize=1,)
    ax.plot(t[T_5peaks], T_5[T_5peaks], "rx", label='Maxima')
    ax.plot(t[T_5lows], T_5[T_5lows], "bx", label='Minima')

    ax.plot(t[T_6peaks], T_6[T_6peaks], "rx")
    ax.plot(t[T_6lows], T_6[T_6lows], "bx")
    ax.grid(True)

    #phasendifferenz in (s)
    pd = t[T_5peaks] - t[T_6peaks]
    print ("T1T2 Delta t (s)= ", pd)
    Mwpd = ufloat(np.mean(pd), stats.sem(pd))
    print("Mwpd = ", np.mean(pd), " +- ", stats.sem(pd))

    #Amplituden in (K)
#########################berechnung Amplituden A_nah
    A_nah = [0]*10
    i = 0
    while(i<=9):
        A_nah[i] = 0.5 * (T_5[T_5peaks][i+1] - 0.5 * (T_5[T_5peaks][i+1] - T_5[T_5lows][i]) - T_5[T_5lows][i])
        i = i + 1
#########################
    A_nah = np.array(A_nah)
    print("A_nah = ", A_nah)


#########################berechnung Amplituden A_fern
    A_fern = [0]*10
    i = 0
    while(i<=9):
        A_fern[i] = 0.5 * (T_6[T_6peaks][i+1] - 0.5 * (T_6[T_6peaks][i+1] - T_6[T_6lows][i]) - T_6[T_6lows][i])
        i = i + 1
#########################
    A_fern = np.array(A_fern)
    print("A_fern = ", A_fern)

    print("")
    print("MwA_nah = ", np.mean(A_nah), " +- ", stats.sem(A_nah))
    print("MwA_fern = ", np.mean(A_fern), " +- ", stats.sem(A_fern))

    #ln(anteil)
    lnan = np.log(A_fern/A_nah)
    print("ln(A_nah / A_fern) ", lnan)

    Mwln = ufloat(np.mean(lnan), stats.sem(lnan))
    print("Mwln(A_nah/A_fern) = ", Mwln)

    #berechnung der wärmeleitfähigkeit k
    k = (r_A * c_A * (dx)**2)/(2 * Mwpd * Mwln)
    print(k)
    ax.legend(markerscale = 2)
    ax.set(xlabel=r"$t/\unit{\second}$ ", ylabel=r"$T/\unit{\kelvin}$");
    fig.savefig("build/AluminiumPlot.pdf")
Aluminium()

print("")
print("")

##############
#Edelstahl
##############
print("Werte für Edelstahl")
#Dynamische methode Edelstahl
def Edelstahl():
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    t, T_8, T_7 = np.genfromtxt("Daten/Edelstahl.txt", unpack=True)
    T_8 = T_8 + 273
    T_7 = T_7 + 273

    T_8peaks, _ = find_peaks(T_8, height=0)
    T_8lows, _ = find_peaks(-T_8)

    T_7peaks, _ = find_peaks(T_7, height=0)
    T_7lows, _ = find_peaks(-T_7)

    #x-Achse anzeigebereich
    x_plot = np.linspace(0,1000)
    # ??
    fig, ax = plt.subplots(1, 1, layout="constrained")
    #ploten der Meswerte und Maxima/Minima
    ax.plot(t, T_8, "kx", label="Temperatur $T_8$",markersize=1,)
    ax.plot(t, T_7, "rx", label="Temperatur $T_7$",markersize=1,)
    ax.plot(t[T_8peaks], T_8[T_8peaks], "rx", label='Maxima')
    ax.plot(t[T_8lows], T_8[T_8lows], "bx", label='Minima')

    ax.plot(t[T_7peaks], T_7[T_7peaks], "rx")
    ax.plot(t[T_7lows], T_7[T_7lows], "bx")
    ax.grid(True)

    print(t[T_8peaks])
    print(t[T_7peaks])

    #phasendifferenz in (s)
   
    pd = t[T_8peaks] - t[T_7peaks]
    print ("T1T2 Delta t (s)= ", pd)
    Mwpd = ufloat(np.mean(pd), stats.sem(pd))
    print("Mwpd = ", np.mean(pd), " +- ", stats.sem(pd))
   #Amplituden in (K)
#########################berechnung Amplituden A_nah
    A_nah = [0]*7
    i = 0
    while(i<=6):
        A_nah[i] = 0.5 * (T_8[T_8peaks][i+1] - 0.5 * (T_8[T_8peaks][i+1] - T_8[T_8lows][i]) - T_8[T_8lows][i])
        i = i + 1
#########################
    A_nah = np.array(A_nah)
    print("A_nah = ", A_nah)


#########################berechnung Amplituden A_fern
    A_fern = [0]*7
    i = 0
    while(i<=6):
        A_fern[i] = 0.5 * (T_7[T_7peaks][i+1] - 0.5 * (T_7[T_7peaks][i+1] - T_7[T_7lows][i]) - T_7[T_7lows][i])
        i = i + 1
#########################
    A_fern = np.array(A_fern)
    print("A_fern = ", A_fern)

    print("")
    print("MwA_nah = ", np.mean(A_nah), " +- ", stats.sem(A_nah))
    print("MwA_fern = ", np.mean(A_fern), " +- ", stats.sem(A_fern))

    #ln(anteil)

    #ln(anteil)
    lnan = np.log(A_fern/A_nah)
    print("ln(A_nah / A_fern) ", lnan)

    Mwln = ufloat(np.mean(lnan), stats.sem(lnan))
    print("Mwln(A_nah/A_fern) = ", Mwln)

    #berechnung der wärmeleitfähigkeit k
    k = (r_E * c_E * (dx)**2)/(2 * Mwpd * Mwln)
    print(k)
    ax.legend(markerscale = 2)
    ax.set(xlabel=r"$t/\unit{\second}$ ", ylabel=r"$T/\unit{\kelvin}$");
    fig.savefig("build/EdelstahlPlot.pdf")
Edelstahl()