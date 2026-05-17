import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

## Vierte Linearverstärkermessung
f_kHz, U_out = np.genfromtxt("Daten/L4.txt", unpack=True)
f_Hz = f_kHz * 1e3
U_e = 1.05
V = U_out/U_e

V0 = np.mean(V[:6])
print('Vierte Leerlaufverstärkung ist V4 = ', V0)
steigung, achsenabschnitt = np.polyfit(np.log10(f_Hz[-3:]), np.log10(V[-3:]), 1)
# Grenzfrequenz berechnen
V_grenz = V0 / np.sqrt(2)
log_V_grenz = np.log10(V_grenz)
log_f_g = (log_V_grenz - achsenabschnitt) / steigung
f_g_Hz = 10 ** log_f_g
f_g_kHz = f_g_Hz / 1000
print(f'Vierte Grenzfrequenz ist f4_g = {f_g_kHz:.2f} kHz')
# Bandbreitenprodukt
B = V0 * f_g_kHz
print(f'Vierte Bandbreite ist B4 = {B:.2f} kHz')

fig, ax1 = plt.subplots(1, 1, layout="constrained")
ax1.loglog(f_Hz, V, "k.", label="Messwerte")

# Plateau
f_plot = np.array([min(f_Hz), max(f_Hz)])
ax1.loglog(f_plot, [V0, V0], 'b--', label=f'Plateau', linewidth=2)
# Abfall
f_fit = np.logspace(np.log10(min(f_Hz[-3:])), np.log10(max(f_Hz)), 100)
V_fit = 10 ** (steigung * np.log10(f_fit) + achsenabschnitt)
ax1.loglog(f_fit, V_fit, 'r-', label='Abfall (Gerade)', linewidth=2)

ax1.set_title("Messung 4")
ax1.set_xlabel("f / Hz")
ax1.set_ylabel("Verstärkung V")
ax1.grid(True, which='both', linestyle='--', alpha=0.5)
ax1.legend()

fig.savefig("build/L4.pdf")

