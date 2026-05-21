import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
#import pandas as pd
from uncertainties import unumpy as unp  # Add this line
from scipy.optimize import curve_fit
import pandas as pd
from uncertainties import correlated_values

def winkel_einlesen(dateiname):
    df = pd.read_csv(f'{dateiname}', sep=',')

    # 2. Nur die letzten 4 Spalten auswählen
    # df.iloc[Zeilen, Spalten] -> ':' steht für alle Zeilen, '-4:' für die letzten 4 Spalten
    df_letzte_vier = df.iloc[:, -4:]

    # 3. Bei Bedarf direkt in ein NumPy-Array umwandeln
    array_letzte_vier = df_letzte_vier.to_numpy()
    return array_letzte_vier

arr2= winkel_einlesen("daten/N2.8dotiert")
arr1 = winkel_einlesen("daten/N1.2Dotiert")
arr3 = winkel_einlesen("daten/hochrein")
print (arr1[0][1])
def differenz(dateiname):
    arr = winkel_einlesen(dateiname)
    diff = []
    for x in range (8):
        diff.append(arr[x][0] - arr[x][1])
    return diff

#print(differenz("daten/N2.8dotiert"))


print(arr1)

import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 1. PHYSIKALISCHE KONSTANTEN (SI-EINHEITEN)
# =========================================================================
e0 = 1.602176634e-19        # Elementarladung [C]
epsilon0 = 8.8541878128e-12  # Influenzkonstante [F/m]
c = 299792458               # Lichtgeschwindigkeit [m/s]
me = 9.1093837e-31          # Freie Elektronenmasse [kg]
n = 3.3                     # Brechungsindex von GaAs
#B = 0.4                     # HIER dein maximales Magnetfeld eintragen [T]

# Die 9 Wellenlängen des Versuchs im nahen Infrarot
wavelengths_um = np.array([1.06, 1.29, 1.45, 1.72, 1.96, 2.156, 2.34, 2.51, 2.65])
lambda_m = wavelengths_um * 1e-6
lambda_sq = lambda_m**2

# =========================================================================
# 2. PROBENPARAMETERN (DICKEN & DOTIERUNGEN)
# =========================================================================
# Probe 1
N1_cm3 = 1.2e18             # Donatorenkonzentration [cm^-3]
N1 = N1_cm3 * 1e6           # [m^-3]
L1 = 1.36 / 1000            # Dicke in Meter (1.36 mm) 

# Probe 2
N2_cm3 = 2.8e18             # Donatorenkonzentration [cm^-3]
N2 = N2_cm3 * 1e6           # [m^-3]
L2 = 1.29 / 1000            # Dicke in Meter (1.29 mm) 

# Reine Probe (Hochrein)
L_rein = 5.11 / 1000        # Dicke in Meter (5.11 mm) 

# =========================================================================
# 3. MESSWERTE EINTRAGEN (Format: [Grad1, Min/Sek1, Grad2, Min/Sek2])
# =========================================================================
# HIER BITTE NOCH DEINE ECHTEN MESSWERTE FÜR DIE 1.2er PROBE EINTRAGEN:
daten_p1 = arr1
daten_p2 = arr2
daten_rein = arr3
#daten_p1 = np.array([
#    [15.4, 0, 11.9, 0],  # 1.06 µm
#    [16.1, 0, 12.2, 0],  # 1.29 µm
#    [16.8, 0, 12.5, 0],  # 1.45 µm
#    [17.5, 0, 12.8, 0],  # 1.72 µm
#    [18.6, 0, 13.1, 0],  # 1.96 µm
#    [19.8, 0, 13.4, 0],  # 2.156 µm
#    [21.2, 0, 13.6, 0],  # 2.34 µm
#    [22.9, 0, 13.8, 0],  # 2.51 µm
#    [24.8, 0, 14.0, 0]   # 2.65 µm
#])
#
## DEINE ECHTEN MESSWERTE FÜR DIE 2.8er PROBE (bereits hinterlegt)
#daten_p2 = np.array([
#    [338, 32, 327, 15],  # 1.06 µm
#    [337,  0, 328, 10],  # 1.29 µm
#    [336,  9, 327, 15],  # 1.45 µm
#    [337, 56, 328, 12],  # 1.72 µm
#    [342, 36, 331, 11],  # 1.96 µm
#    [344, 40, 332, 58],  # 2.156 µm
#    [10,   0,   1, 34],  # 2.34 µm
#    [32,   5,  14, 13],  # 2.51 µm
#    [76,  59,  63, 29]   # 2.65 µm
#])
#
## HIER BITTE NOCH DEINE ECHTEN MESSWERTE FÜR DIE HOCHREINE PROBE EINTRAGEN:
#daten_rein = np.array([
#    [10, 0, 9, 0],  # 1.06 µm
#    [10, 0, 9, 0],  # 1.29 µm
#    [10, 0, 9, 0],  # 1.45 µm
#    [10, 0, 9, 0],  # 1.72 µm
#    [10, 0, 9, 0],  # 1.96 µm
#    [10, 0, 9, 0],  # 2.156 µm
#    [10, 0, 9, 0],  # 2.34 µm
#    [10, 0, 9, 0],  # 2.51 µm
#    [10, 0, 9, 0]   # 2.65 µm
#])

# =========================================================================
# 4. BERECHNUNGS-FUNKTIONEN
# =========================================================================
def berechne_winkel_rad(daten_matrix):
    w1_deg = daten_matrix[:, 0] + (daten_matrix[:, 1] / 60)
    w2_deg = daten_matrix[:, 2] + (daten_matrix[:, 3] / 60)
    # Modulo fängt den 360-Grad-Sprung ab
    diff_deg = np.mod(w1_deg - w2_deg + 180, 360) - 180
    return np.radians(diff_deg / 2)

# Halbe Drehwinkel in Radiant bestimmen [cite: 77]
theta_p1_rad = berechne_winkel_rad(daten_p1)
theta_p2_rad = berechne_winkel_rad(daten_p2)
theta_rein_rad = berechne_winkel_rad(daten_rein)

# Faraday-Rotation pro Einheitslänge [rad/m] berechnen
# Wichtig: Jede Probe wird zuerst durch ihre EIGENE Dicke geteilt, bevor man subtrahiert! [cite: 115, 119]
theta_frei_p1 = (theta_p1_rad / L1) - (theta_rein_rad / L_rein) 
theta_frei_p2 = (theta_p2_rad / L2) - (theta_rein_rad / L_rein) 

def g(x,a,b):
    return a*x + b

# 1. Erstelle eine Maske, die überall True ist, außer bei Index 4
maske = np.ones(len(arr1), dtype=bool)
maske[3] = False  # Das 5. Element (Index 4) wird auf False gesetzt
maske[4] = False  # Das 6. Element (Index 5) wird auf False gesetzt
maske2 = np.ones(len(arr2), dtype=bool)
maske2[3] = False  # Das 5. Element (Index 4
maske2[4] = False  # Das 6. Element (Index 5) wird auf False gesetzt
maske2[0] = False  # Das 2. Element (Index 1) wird auf False gesetzt
# Linearer Fit für beide Proben
params1, fehler1 = np.polyfit(lambda_sq[maske2], theta_frei_p1[maske2], 1,cov=True)
params2, fehler2 = np.polyfit(lambda_sq[maske], theta_frei_p2[maske], 1,cov=True)
# Fehler extrahieren
Steigung1 = ufloat(params1[0], np.sqrt(fehler1[0][0]))
Achsenabschnitt1 = ufloat(params1[1], np.sqrt(fehler1[1][1]))
Steigung2 = ufloat(params2[0], np.sqrt(fehler2[0][0]))
Achsenabschnitt2 = ufloat(params2[1], np.sqrt(fehler2[1][1]))

#werte ausgeben
print("steigung1 = ", Steigung1)
print("achsenabschnitt1 = ", Achsenabschnitt1)
print("steigung2 = ", Steigung2)
print("achsenabschnitt2 = ", Achsenabschnitt2)








def f(x, a, b, c):
    return a * x**2 + b * x + c


x, B = np.genfromtxt(
    "daten/feld.txt",
    delimiter=',',
    comments='#',
    autostrip=True,
    unpack=True
)      
def linear(x, m, c):
    return m * x + c
# 1. Fit ausführen
koeffs, covariance = curve_fit(f, x, B)

# 2. ALLE Koeffizienten auf einmal ALS KORRELIERTE EINHEIT einlesen
# Dadurch kennt uncertainties die Kovarianzmatrix und gleicht die Fehler ab!
a_corr, b_corr, c_corr = correlated_values(koeffs, covariance)
print("Gefundene Koeffizienten für den quadratischen Fit:", a_corr, b_corr, c_corr)

fig, (ax1, ax2) = plt.subplots(2,1,figsize=(8, 10))
ax1.plot(lambda_sq, theta_frei_p1, 'o', label='Probe 1 (N=1.2e18 cm^-3)')
y = np.linspace(min(lambda_sq), max(lambda_sq), 100)
ax1.plot(y, linear(y, *params1), label='Linearer Fit Probe 1', color='blue')
ax1.set_xlabel(r'$\lambda^2$ [m$^2$]', fontsize=12)
ax1.set_ylabel(r'$\theta_{frei}$ [rad/m]', fontsize=12)
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_title('Faraday-Rotation pro Einheitslänge aufgetragen gegen die  Wellenlänge zum Quadrat', fontsize=14, fontweight='bold')

ax2.plot(lambda_sq, theta_frei_p2, 'o', label='Probe 2 (N=2.8e18 cm^-3)')
ax2.plot(y, linear(y, *params2), label='Linearer Fit Probe 2', color='orange')
ax2.set_xlabel(r'$\lambda^2$ [m$^2$]', fontsize=12)
ax2.set_ylabel(r'$\theta_{frei}$ [rad/m]', fontsize=12)
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_title('Faraday-Rotation pro Einheitslänge aufgetragen gegen die  Wellenlänge zum Quadrat', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig('build/faraday_rotation.png', dpi=300)

fig, ax = plt.subplots(figsize=(8, 6))
x_fit = np.linspace(min(x), max(x), 100)
# Für den Plot nutzen wir die reinen Zahlenwerte (.n), da matplotlib keine ufloats plotten kann
ax.plot(x_fit, f(x_fit, *koeffs), color='red', 
        label='f(x) = {a:.2f}x^2 + {b:.2f}x + {c:.2f}'.format(a=a_corr.n, b=b_corr.n, c=c_corr.n))

# Ableitung berechnen für Nulldurchgang (rein mit Zahlenwerten für die Grafik)
ax.plot(x, linear(x, 2*koeffs[0], koeffs[1]), 
        label="g'(x) = {a:.2f}x + {b:.2f}".format(a=2*koeffs[0], b=koeffs[1]), color='green', linestyle='-')

# Scheitelpunkt berechnen (Exakt mit Fehlern)
def nullstelle(a, b):
    return -b / (2 * a)

# x-Position des Maximums mit korrektem Fehler
B_maxy_corr = nullstelle(a_corr, b_corr) 

# B_max mit dem mathematisch echten, winzigen Fehler
B_max = f(B_maxy_corr, a_corr, b_corr, c_corr)
print(f"B_max (korreliert) = {B_max} mT")

# Für die vertikale Linie im Plot den Nominalwert nutzen
ax.axvline(x=B_maxy_corr.n, color='blue', linestyle='--', label='Null Durchgang')

# Restlicher Plot-Code bleibt gleich...
ax.plot(x, B, marker='o', linestyle='none', color='green', label='Messdaten')
ax.set_xlabel('Position x [mm]', fontsize=12)
ax.set_ylabel('Magnetfeld B [mT]', fontsize=12)
ax.set_title('Magnetfeldverteilung entlang der Probe', fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.5)

ax.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.savefig('build/magnetfeldverteilung.png', dpi=300)



### Ich hab B_max, theta_frei_p1
# Die Funktion muss die Dichte N als Argument annehmen, damit sie flexibel ist!
def effektive_masse(steigung, B, N_dichte):
    zaehler = e0**3 * N_dichte * B
    nenner = 8 * np.pi**2 * epsilon0 * c**3 * n * steigung
    return unp.sqrt(zaehler / nenner)

# Aufruf im Skript (Zeile 245/246):
# Hier übergibst du jetzt explizit N1 für Probe 1 und N2 für Probe 2!
m_star_p1 = effektive_masse(Steigung1, B_max/1000, N1)
m_star_p2 = effektive_masse(Steigung2, B_max/1000, N2)

print("Effektive Masse für Probe 1:", m_star_p1)
print("Effektive Masse für Probe 2:", m_star_p2)

print("Verhältnis m*/me Probe 1:", (m_star_p1 / me) * 100, "%")
print("Verhältnis m*/me Probe 2:", (m_star_p2 / me) * 100, "%")

def tab(t1,t2,t3):
    print("\n" + "="*85)
    print(f"{'λ [µm]':<8} | {'θ_p1 [rad]':<20} | {'θ_rein [rad]':<20} | {'θ_frei_p1 [rad/m]':<20}")
    print("="*85)

    # Schleife mit wissenschaftlicher Formatierung (:.2e) für die uncertainties-Objekte
    for wl, t_p1, t_rein, t_frei in zip(wavelengths_um, t1, t2, t3):
        # ':.2e' zwingt uncertainties dazu, den Wert im Format (Masse +/- Fehler)e-X auszugeben
        print(f"{wl:<8.2f} & {t_p1:.2e} & {t_rein:.2e} & {t_frei:.2e}")

    print("="*85)

tab(theta_p1_rad, theta_rein_rad, theta_frei_p1)
tab(theta_p2_rad, theta_rein_rad, theta_frei_p2)