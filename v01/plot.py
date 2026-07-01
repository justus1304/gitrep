import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat
# ==========================================
# DATEINAME HIER EINTRAGEN
# ==========================================
datei_name = 'daten/verzoegerung1.txt'

try:
    # Daten einlesen
    data = np.loadtxt(datei_name)
    x_raw = data[:, 0]  # Erste Spalte: Zeitverzögerung in ns
    y_raw = data[:, 1]  # Zweite Spalte: Counts in 20s
    
    # CRITICAL FIX: Daten nach x-Werten aufsteigend sortieren!
    sort_idx = np.argsort(x_raw)
    x_delay = x_raw[sort_idx]
    y_counts = y_raw[sort_idx]
    
    print(f"Datei '{datei_name}' erfolgreich geladen und sortiert.")
except Exception as e:
    print(f"Fehler beim Laden der Datei: {e}")
    # Symmetrische Fallback-Daten zum Testen
    x_delay = np.array([-30, -20, -10, -5, 0, 5, 10, 20, 30])
    y_counts = np.array([10,  40,  120, 155, 158, 155, 120,  40,  10])

# ==========================================
# BERECHNUNG VON MITTIGEM PLATEAU UND FWHM
# ==========================================
max_counts = np.max(y_counts)

# Plateau als Bereich innerhalb der obersten 2% definieren
plateau_threshold = 0.98 * max_counts
idx_plateau = np.where(y_counts >= plateau_threshold)[0]
delay_at_plateau_center = np.mean(x_delay[idx_plateau])

# Halbwertsbreite (FWHM) berechnen
half_max = max_counts / 2.0

# Da die Daten jetzt sortiert sind, funktionieren die Flanken-Indizes sauber:
idx_left = np.where(x_delay < delay_at_plateau_center)[0]
idx_right = np.where(x_delay >= delay_at_plateau_center)[0]

if len(idx_left) > 0 and len(idx_right) > 0:
    # Links interpolieren
    x_left = np.interp(half_max, y_counts[idx_left], x_delay[idx_left])
    # Rechts interpolieren (für interp müssen x-Werte steigen, also spiegeln wir die Arrays)
    x_right = np.interp(half_max, y_counts[idx_right][::-1], x_delay[idx_right][::-1])
    fwhm = x_right - x_left
else:
    x_left, x_right, fwhm = 0, 0, 0

# ==========================================
# PLOT ERSTELLEN
# ==========================================
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=100)

# FEHLERBERECHNUNG: Wurzel aus den Counts (Poisson-Statistik)
y_errors = np.sqrt(y_counts)

# Messdaten mit Fehlerbalken plotten (anstelle von ax.plot)
ax.errorbar(x_delay, y_counts
            , yerr=y_errors, fmt='bo', capsize=3, elinewidth=1.2,
            label='Counts in 20s mit $\sqrt{N}$-Fehler', markersize=5)

ax.axhline(half_max, color='r', linestyle='--', alpha=0.7, label=f'Halbe Höhe ({half_max:.1f} Counts)')

if fwhm > 0:
    # FWHM Linie einzeichnen
    ax.plot([x_left, x_right], [half_max, half_max], 'r|-', lw=2.5, markersize=12, label='FWHM Linie')

def counts(x):
    return max_counts + 0*x

# Plateau-Mitte markieren
ax.axvline(delay_at_plateau_center, color='g', linestyle=':', alpha=0.5)
x = np.linspace(delay_at_plateau_center - 5, delay_at_plateau_center + 5, 100)
ax.plot(x, counts(x), '-', markersize=9, 
        label=f'Plateau-Mitte ({delay_at_plateau_center:.1f} ns)')

# Achsenbeschriftungen und Layout
ax.set_xlabel(r'Zeitverzögerung $\Delta t$ / ns', fontsize=11)
ax.set_ylabel('Counts in 20 s', fontsize=11)
#ax.set_title('Koinzidenzkurve (Verzögerungsleitung vor Diskriminator)', fontsize=12, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='best', fontsize=10)

fig.tight_layout()

# Speichern
fig.savefig('build/koinzidenzkurve_myonen_korrigiert.pdf', bbox_inches='tight')

print(f"\n--- Korrigierte Auswertung ---")
print(f"Schnittpunkt Links:  {x_left:.2f} ns")
print(f"Schnittpunkt Rechts: {x_right:.2f} ns")
print(f"FWHM (Halbwertsbreite): {fwhm:.2f} ns")



fig, ax1 = plt.subplots(figsize=(8, 5.5), dpi=100)

time, chanel1, r1, chanel2, r2 = np.loadtxt('daten/chanel.txt', unpack=True)
time2 = np.delete(time, 7)
chanel12 = np.delete(chanel1, 7)
chanel22 = np.delete(chanel2, 7)
r12 = np.delete(r1, 7)
r22 = np.delete(r2, 7)
print((chanel1*r1+chanel2*r2)/(r1+r2))

x = np.linspace(0, 512, 100)
#def linear(x, a, b):
#    return a*x + b

params, covariance = np.polyfit((chanel12*r12+chanel22*r22)/(r12+r22 ),time2 , 1, cov=True)
print(f"Fit-Parameter: a = {params[0]:.4f} +- {np.sqrt(covariance[0, 0]):.4f}, b = {params[1]:.4f} +- {np.sqrt(covariance[1, 1]):.4f}")
ax1.plot(x, np.polyval(params, x), 'r-', label=f'Lineare Regression: y = {params[0]:.4f}x + {params[1]:.4f}')

ax1.plot((chanel1*r1+chanel2*r2)/(r1+r2),time,  'o', label='Mittelwert der Kanäle')
ax1.set_ylabel('Zeit / ns', fontsize=11)
ax1.set_xlabel('Chanel des VKA', fontsize=11)
#ax1.set_title('Zeitimpulsbreite aufgetragen gegen die Chanelnummer', fontsize=12, fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='best', fontsize=10)
fig.tight_layout()
fig.savefig('build/kalibrierung.pdf', bbox_inches='tight')


###Lebensdauer berechnen
R = np.genfromtxt('daten/verteilung.txt', unpack=True)
c = []
for i in range(len(R)):
    c.append(i*0.0217)

fig, ax2 = plt.subplots(figsize=(8, 5.5), dpi=100)

def exp(x,a,b,c):
    return a*np.exp(-b*x)+c

print (len(c), len(R))

params, cov = curve_fit(exp, c, R, p0=(415, 0.5, 4), maxfev=10000)
print(' Regression zum bestimmen der mittleren Lebensdauer der Myonen')
print(f"Fit-Paramenp.sqrt(cov[0, 0])ter: a = {params[0]:.4f} +- {np.sqrt(cov[0, 0]):.4f}, b = {params[1]:.4f} +- {np.sqrt(cov[1, 1]):.4f}, c = {params[2]:.4f} +- {np.sqrt(cov[2, 2]):.4f}")
x = np.linspace(0, 12, 100)
#ax2.plot(c, R, '.', label='Messwerte')
ax2.errorbar(c, R, yerr=np.sqrt(R), fmt='.', capsize=1, elinewidth=0.5, label='Messwerte mit $\sqrt{N}$-Fehler', markersize=2)
ax2.plot(x, exp(x, *params), 'r-', label=f'Exponentiale Regression: y = {params[0]:.4f}*exp(-{params[1]:.4f}*x) + {params[2]:.4f}', markersize=6,lw=5)
ax2.set_ylabel('Counts', fontsize=11)
ax2.set_xlabel('Zeit / ns', fontsize=11)
#ax2.set_title('Lebensdauer der Myonen', fontsize=12, fontweight='bold')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='best', fontsize=10)
fig.tight_layout()
fig.savefig('build/lebensdauer.pdf', bbox_inches='tight')

print ('tau = 1/b = ', 1/ufloat(params[1],np.sqrt(cov[1, 1])) , 'ns')

###untergrundrate berechnen 
t_gesammt = 254135 #s

R = (ufloat(365,np.sqrt(365))/20) #1/s
N = R * t_gesammt
deltat = 2*10**(-5) #s

e = deltat*R*unp.exp(-deltat*R)
print(e)

print(e*N)

print(e*N/512)