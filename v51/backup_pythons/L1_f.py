import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat, unumpy

## Erste Linearverstärkermessung
f_kHz, U_out_values = np.genfromtxt("Daten/L1.txt", unpack=True)
f_Hz = f_kHz * 1e3

U_e = ufloat(1.05, 0.02)
U_out = unumpy.uarray(U_out_values, 0.01)
V = U_out/U_e

V0 = sum(V[:8]) / len(V[:8])
print(f'Erste Leerlaufverstärkung V0 = {V0:.2f}')

x = np.log10(f_Hz[-4:])
y = unumpy.nominal_values(V[-4:])
V_err = unumpy.std_devs(V[-4:])
y_err = V_err / (y * np.log(10))  # Fehler in log10

def gerade(x, m, b):
    return m * x + b

params, covariance_matrix = curve_fit(gerade, x, y)
m,b = params
dm, db = np.sqrt(np.diag(covariance_matrix))
m_ufloat = ufloat(m, dm)
b_ufloat = ufloat(b, db)

# Grenzfrequenz
V_grenz = V0 / np.sqrt(2)
log10_f_g = (unumpy.log10(V_grenz) - b_ufloat) / m_ufloat
f_g_kHz = 10 ** log10_f_g / 1000
print(f'Erste Grenzfrequenz f_g1 = {f_g_kHz:.2f} kHz')
# Bandbreitenprodukt
B = V0 * f_g_kHz
print(f'Erste Bandbreite ist B1 = {B:.2f} kHz')

# Plot
fig, ax1 = plt.subplots(1, 1, layout="constrained")
# Plateau
f_plot = np.array([min(f_Hz), max(f_Hz)])
ax1.loglog(f_plot, [V0.nominal_value, V0.nominal_value], 'b--', label=f'Plateau', linewidth=2)
# Abfall
f_fit = np.logspace(np.log10(min(f_Hz[-4:])), np.log10(max(f_Hz)), 100)
V_fit = 10 ** (m * np.log10(f_fit) + b)
ax1.loglog(f_fit, V_fit, 'r-', label='Abfall (Gerade)', linewidth=2)

ax1.set_title("Messung 1")
ax1.set_xlabel("f / Hz")
ax1.set_ylabel("Verstärkung V")
ax1.grid(True, which='both', linestyle='--', alpha=0.5)
ax1.legend()

fig.savefig("build/L1_f.pdf")



# V0_werte = V[:8]
# V0 = sum(V0_werte) / len(V0_werte)
# print(f'Leerlaufverstärkung V0 = {V0:.2f}')

# V0 = np.mean(V[:8])
# print('Erste Leerlaufverstärkung ist V1 = ', V0)
# steigung, achsenabschnitt = np.polyfit(np.log10(f_Hz[-4:]), np.log10(V[-4:]), 1)
# # Grenzfrequenz berechnen
# V_grenz = V0 / np.sqrt(2)
# log_V_grenz = np.log10(V_grenz)
# log_f_g = (log_V_grenz - achsenabschnitt) / steigung
# f_g_Hz = 10 ** log_f_g / 1000
# print('Erste Grenzfrequenz ist f1_g = ', f_g_Hz)
# # Bandbreitenprodukt
# B = V0 * f_g_Hz
# print('Erste Bandbreite ist B1 = ', B)

# fig, ax1 = plt.subplots(1, 1, layout="constrained")
# ax1.loglog(f_Hz, V, "k.", label="Messwerte")

# # Plateau
# f_plot = np.array([min(f_Hz), max(f_Hz)])
# ax1.loglog(f_plot, [V0, V0], 'b--', label=f'Plateau', linewidth=2)
# # Abfall
# f_fit = np.logspace(np.log10(min(f_Hz[-4:])), np.log10(max(f_Hz)), 100)
# V_fit = 10 ** (steigung * np.log10(f_fit) + achsenabschnitt)
# ax1.loglog(f_fit, V_fit, 'r-', label='Abfall (Gerade)', linewidth=2)

# ax1.set_title("Messung 1")
# ax1.set_xlabel("f / Hz")
# ax1.set_ylabel("Verstärkung V")
# ax1.grid(True, which='both', linestyle='--', alpha=0.5)
# ax1.legend()

# fig.savefig("build/L1.pdf")


