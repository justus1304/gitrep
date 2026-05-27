import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat, unumpy

# ## Invertierender Linearverstärker a)
# # Gemeinsame Eingangsspannung
# U_e = 1.05

# def process_measurement(name, suffix, n_plateau, n_fit_end):
#     # Daten einlesen
#     f_kHz, U_out = np.genfromtxt(f"Daten/L{suffix}.txt", unpack=True)
#     f_Hz = f_kHz * 1e3
#     V = U_out / U_e

#     # Leerlaufverstärkung
#     V0 = np.mean(V[:n_plateau])
#     print(f"{name} Leerlaufverstärkung V_{suffix} = {V0:.4f}")

#     # Steigung im Abfallbereich
#     steigung, achsenabschnitt = np.polyfit(
#         np.log10(f_Hz[-n_fit_end:]),
#         np.log10(V[-n_fit_end:]),
#         1
#     )

#     # Grenzfrequenz
#     V_grenz = V0 / np.sqrt(2)
#     log_V_grenz = np.log10(V_grenz)
#     log_f_g = (log_V_grenz - achsenabschnitt) / steigung
#     f_g_Hz = 10 ** log_f_g
#     f_g_kHz = f_g_Hz / 1000
#     print(f"{name} Grenzfrequenz f_g{suffix} = {f_g_kHz:.2f} kHz")

#     # Bandbreitenprodukt
#     B = V0 * f_g_kHz
#     print(f"{name} Bandbreite B_{suffix} = {B:.2f} kHz\n")

#     # Plot
#     fig, ax = plt.subplots(1, 1, layout="constrained")
#     ax.loglog(f_Hz, V, "k.", label="Messwerte")

#     # Plateau
#     f_plot = np.array([min(f_Hz), max(f_Hz)])
#     ax.loglog(f_plot, [V0, V0], 'b--', label='Plateau', linewidth=2)

#     # Abfallgerade
#     f_fit = np.logspace(
#         np.log10(min(f_Hz[-n_fit_end:])),
#         np.log10(max(f_Hz)),
#         100
#     )
#     V_fit = 10 ** (steigung * np.log10(f_fit) + achsenabschnitt)
#     ax.loglog(f_fit, V_fit, 'r-', label='Abfall (Gerade)', linewidth=2)

#     ax.set_title(f"Messung {suffix}")
#     ax.set_xlabel("f / Hz")
#     ax.set_ylabel("Verstärkung V")
#     ax.grid(True, which='both', linestyle='--', alpha=0.5)
#     ax.legend()

#     fig.savefig(f"build/L{suffix}.pdf")
#     plt.close(fig)  # Speicher freigeben

# # Messungen ausführen
# process_measurement("Erste", "1", n_plateau=8, n_fit_end=4)
# process_measurement("Zweite", "2", n_plateau=6, n_fit_end=5)
# process_measurement("Dritte", "3", n_plateau=6, n_fit_end=3)
# process_measurement("Vierte", "4", n_plateau=6, n_fit_end=3)
# print("Alle Messungen verarbeitet. PDFs im Ordner 'build/'")


# Gemeinsame Eingangsspannung
U_e = 1.05

######################## Invertierender Linearverstärker b) ########################
# plt.rcParams["figure.figsize"] = (10,8)
# plt.rcParams["font.size"] = 16

# def phase(name, suffix):
#     f_kHz, phi = np.genfromtxt(f"Daten/LP{suffix}.txt", unpack=True)
#     f_Hz = f_kHz * 1e3

#     fig, ax = plt.subplots(1,1, layout="constrained")
#     ax.semilogx(f_Hz, phi, "k.", label="Messwerte")
    
#     ax.set_xlabel("f / Hz")
#     ax.set_ylabel(r"$\varphi / °$")
#     ax.grid(True, which='both', linestyle='--', alpha=0.7)
#     ax.legend()
#     fig.savefig(f"build/LP{suffix}.pdf")

# # Messungen ausführen
# phase("Erste", "1")
# phase("Zweite", "2")
# phase("Dritte", "3")
# phase("Vierte", "4")
# print("Alle Phasengänge geplottet. PDFs im Ordner 'build/'")


plt.rcParams["figure.figsize"] = (10,8)
plt.rcParams["font.size"] = 16

# Messung 1
f_kHz1, phi1 = np.genfromtxt("Daten/LP1.txt", unpack=True)
f_Hz1 = f_kHz1 * 1e3
# Fehler für die Phasenmessung
phi_err1 = np.zeros_like(phi1)
phi_err1[:6] = 2    # erste 6 Werte: Fehler 2°
phi_err1[6:] = 10   # letzte 3 Werte: Fehler 10°
# Plot mit Fehlerbalken
fig, ax1 = plt.subplots(1, 1, layout="constrained")
ax1.errorbar(f_Hz1, phi1, yerr=phi_err1, fmt='k.', capsize=3, label="Messwerte", markersize=8)
# Achsenbeschriftungen, Gitter und Legende
ax1.set_title("Messung 1")
ax1.set_xlabel("f / Hz")
ax1.set_ylabel(r"$\varphi / °$")
ax1.set_xscale('log')
ax1.grid(True, which='both', linestyle='--', alpha=0.7)
ax1.legend()
fig.savefig("build/LP1.pdf")
plt.close(fig)

# Messung 2
f_kHz2, phi2 = np.genfromtxt("Daten/LP2.txt", unpack=True)
f_Hz2 = f_kHz2 * 1e3
# Fehler für die Phasenmessung
phi_err2 = np.zeros_like(phi2)
phi_err2[:4] = 2   
phi_err2[4:] = 10
# Plot mit Fehlerbalken
fig, ax2 = plt.subplots(1, 1, layout="constrained")
ax2.errorbar(f_Hz2, phi2, yerr=phi_err2, fmt='k.', capsize=3, label="Messwerte", markersize=8)
# Achsenbeschriftungen, Gitter und Legende
ax2.set_title("Messung 2")
ax2.set_xlabel("f / Hz")
ax2.set_ylabel(r"$\varphi / °$")
ax2.set_xscale('log')
ax2.grid(True, which='both', linestyle='--', alpha=0.7)
ax2.legend()
fig.savefig("build/LP2.pdf")
plt.close(fig)

# Messung 3
f_kHz3, phi3 = np.genfromtxt("Daten/LP3.txt", unpack=True)
f_Hz3 = f_kHz3 * 1e3
# Fehler für die Phasenmessung
phi_err3 = np.zeros_like(phi3)
phi_err3[:6] = 3   
phi_err3[6:] = 10
# Plot mit Fehlerbalken
fig, ax3 = plt.subplots(1, 1, layout="constrained")
ax3.errorbar(f_Hz3, phi3, yerr=phi_err3, fmt='k.', capsize=3, label="Messwerte", markersize=8)
# Achsenbeschriftungen, Gitter und Legende
ax3.set_title("Messung 3")
ax3.set_xlabel("f / Hz")
ax3.set_ylabel(r"$\varphi / °$")
ax3.set_xscale('log')
ax3.grid(True, which='both', linestyle='--', alpha=0.7)
ax3.legend()
fig.savefig("build/LP3.pdf")
plt.close(fig)

# Messung 4
f_kHz4, phi4 = np.genfromtxt("Daten/LP4.txt", unpack=True)
f_Hz4 = f_kHz4 * 1e3
# Fehler für die Phasenmessung
phi_err4 = np.zeros_like(phi4)
phi_err4[:5] = 3   
phi_err4[5:] = 10
# Plot mit Fehlerbalken
fig, ax4 = plt.subplots(1, 1, layout="constrained")
ax4.errorbar(f_Hz4, phi4, yerr=phi_err4, fmt='k.', capsize=3, label="Messwerte", markersize=8)
# Achsenbeschriftungen, Gitter und Legende
ax4.set_title("Messung 4")
ax4.set_xlabel("f / Hz")
ax4.set_ylabel(r"$\varphi / °$")
ax4.set_xscale('log')
ax4.grid(True, which='both', linestyle='--', alpha=0.7)
ax4.legend()
fig.savefig("build/LP4.pdf")
plt.close(fig)



## Umkehr-Integrator
# Daten einlesen
f_kHz_ui, U_out_ui_values = np.genfromtxt(f"Daten/ui.txt", unpack=True)
f_Hz_ui = f_kHz_ui * 1e3

U_e = ufloat(1.05, 0.02)
U_out_ui = unumpy.uarray(U_out_ui_values, 0.02)
V_ui = U_out_ui / U_e

x_log = np.log10(f_Hz_ui)
y_log = np.log10(unumpy.nominal_values(V_ui))

params, covariance_matrix = np.polyfit(x_log, y_log, deg=1, cov=True)
m_ui = params[0]  # Steigung (erwartet: -1)
n_ui = params[1]  # Achsenabschnitt
uncertainties = np.sqrt(np.diag(covariance_matrix))

# Ausgabe
print("FIT im doppelt-logarithmischen Diagramm:")
print(f"(UI) Steigung m = {m_ui:.4f} ± {uncertainties[0]:.4f}")
print(f"(UI) Achsenabschnitt n = {n_ui:.4f} ± {uncertainties[1]:.4f}")
print(f"(UI) Proportionalität: V = {10**n_ui:.4f} * f^{m_ui:.4f}")

# Fehlerbalken
V_ui_nom_all = unumpy.nominal_values(V_ui)
V_ui_err_all = unumpy.std_devs(V_ui)

# Plot
x_plot = np.logspace(np.min(np.log10(f_Hz_ui)), np.max(np.log10(f_Hz_ui)), 100)
y_plot = 10**(m_ui * np.log10(x_plot) + n_ui)
fig, ax = plt.subplots(1, 1, layout="constrained")
#ax.loglog(f_Hz_ui, V_ui, "k.", label="Messwerte")
ax.errorbar(f_Hz_ui, V_ui_nom_all, yerr=V_ui_err_all, fmt='k.', capsize=3, label='Messwerte')
ax.loglog(x_plot, y_plot, 'r-', label=f'Ausgleichsgerade', linewidth=2)

ax.set_xlabel("f / Hz")
ax.set_ylabel("Verstärkung V")
ax.grid(True, which='both', linestyle='--', alpha=0.5)
ax.legend()
fig.savefig(f"build/UI.pdf")



## Umkehr-Differenzierer
f_kHz_ud, U_out_ud_mV_values = np.genfromtxt(f"Daten/ud.txt", unpack=True)
U_out_ud = U_out_ud_mV_values *1e3
f_Hz_ud = f_kHz_ud * 1e3
V_ud = U_out_ud / U_e

U_e = ufloat(1.05, 0.02)
U_out_ud = unumpy.uarray(U_out_ud_mV_values, 0.02)
V_ud = U_out_ud / U_e

x_log = np.log10(f_Hz_ud)
y_log = np.log10(unumpy.nominal_values(V_ud))

params, covariance_matrix = np.polyfit(x_log, y_log, deg=1, cov=True)
m_ud = params[0]  # Steigung (erwartet: -1)
n_ud = params[1]  # Achsenabschnitt
uncertainties = np.sqrt(np.diag(covariance_matrix))

# Fehlerbalken
V_ud_nom_all = unumpy.nominal_values(V_ud)
V_ud_err_all = unumpy.std_devs(V_ud)

# Ausgabe
print("FIT im doppelt-logarithmischen Diagramm:")
print(f"(UD) Steigung m = {m_ud:.4f} ± {uncertainties[0]:.4f}")
print(f"(UD) Achsenabschnitt n = {n_ud:.4f} ± {uncertainties[1]:.4f}")
print(f"(UD) Proportionalität: V = {10**n_ud:.4f} * f^{m_ud:.4f}")

# Plot
x_plot = np.logspace(np.min(np.log10(f_Hz_ud)), np.max(np.log10(f_Hz_ud)), 100)
y_plot = 10**(m_ud * np.log10(x_plot) + n_ud)
fig, ax = plt.subplots(1, 1, layout="constrained")
#ax.loglog(f_Hz_ud, V_ud, "k.", label="Messwerte")
ax.errorbar(f_Hz_ud, V_ud_nom_all, yerr=V_ud_err_all, fmt='k.', capsize=3, label='Messwerte')
ax.loglog(x_plot, y_plot, 'r-', label=f'Ausgleichsgerade', linewidth=2)

ax.set_xlabel("f / Hz")
ax.set_ylabel("Verstärkung V")
ax.grid(True, which='both', linestyle='--', alpha=0.5)
ax.legend()
fig.savefig(f"build/UD.pdf")