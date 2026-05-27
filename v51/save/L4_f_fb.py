import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat, unumpy

## Vierte Linearverstärkermessung
f_kHz, U_out_values = np.genfromtxt("Daten/L4.txt", unpack=True)
f_Hz = f_kHz * 1000

U_e = ufloat(1.05, 0.02)
U_out = unumpy.uarray(U_out_values, 0.2)
V = U_out/U_e

# Leerlaufverstärkung
V0 = sum(V[:6]) / len(V[:6])
print(f'Vierte Leerlaufverstärkung V0 = {V0:.2f}')

x = np.log10(f_kHz[-3:])
y = np.log10(unumpy.nominal_values(V[-3:]))
V_err = unumpy.std_devs(V[-3:])
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
f_g_kHz = 10 ** log10_f_g
print(f'Vierte Grenzfrequenz f_g1 = {f_g_kHz:.2f} kHz')
# Bandbreitenprodukt
B = V0 * f_g_kHz
print(f'Vierte Bandbreite ist B1 = {B:.2f} kHz')


# Plot
fig, ax1 = plt.subplots(1, 1, layout="constrained")
#ax1.loglog(f_Hz, unumpy.nominal_values(V), "k.", label="Messwerte")

# Fehlerbalken
V_nom_all = unumpy.nominal_values(V)
V_err_all = unumpy.std_devs(V)
ax1.errorbar(
    f_Hz,
    V_nom_all,
    yerr=V_err_all,
    fmt='k.',
    capsize=3,
    label='Messwerte'
)

# Plateau
f_plot_Hz = np.array([min(f_Hz), max(f_Hz)])
ax1.loglog(f_plot_Hz, [V0.nominal_value, V0.nominal_value], 'b--', label=f'Plateau', linewidth=2)

# Abfall
f_fit_kHz = np.logspace(np.log10(min(f_kHz[-3:])), np.log10(max(f_kHz)), 100)
f_fit_Hz = f_fit_kHz * 1000
V_fit = 10 ** (m * np.log10(f_fit_kHz) + b)
# f_fit_Hz = np.logspace(np.log10(min(f_Hz[-3:])), np.log10(max(f_Hz)), 100)
# V_fit = 10 ** (m * np.log10(f_fit_Hz) + b)
ax1.loglog(f_fit_Hz, V_fit, 'r-', label='Abfall (Gerade)', linewidth=2)

ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.set_title("Messung 4")
ax1.set_xlabel("f / Hz")
ax1.set_ylabel("Verstärkung V")
ax1.grid(True, which='both', linestyle='--', alpha=0.5)
ax1.legend()

fig.savefig("build/L4_f_fb.pdf")
