import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

## Invertierender Linearverstärker a)
# Gemeinsame Eingangsspannung
U_e = 1.05

def process_measurement(name, suffix, n_plateau, n_fit_end):
    # Daten einlesen
    f_kHz, U_out = np.genfromtxt(f"Daten/L{suffix}.txt", unpack=True)
    f_Hz = f_kHz * 1e3
    V = U_out / U_e

    # Leerlaufverstärkung
    V0 = np.mean(V[:n_plateau])
    print(f"{name} Leerlaufverstärkung V_{suffix} = {V0:.4f}")

    # Steigung im Abfallbereich
    steigung, achsenabschnitt = np.polyfit(
        np.log10(f_Hz[-n_fit_end:]),
        np.log10(V[-n_fit_end:]),
        1
    )

    # Grenzfrequenz
    V_grenz = V0 / np.sqrt(2)
    log_V_grenz = np.log10(V_grenz)
    log_f_g = (log_V_grenz - achsenabschnitt) / steigung
    f_g_Hz = 10 ** log_f_g
    f_g_kHz = f_g_Hz / 1000
    print(f"{name} Grenzfrequenz f_g{suffix} = {f_g_kHz:.2f} kHz")

    # Bandbreitenprodukt
    B = V0 * f_g_kHz
    print(f"{name} Bandbreite B_{suffix} = {B:.2f} kHz\n")

    # Plot
    fig, ax = plt.subplots(1, 1, layout="constrained")
    ax.loglog(f_Hz, V, "k.", label="Messwerte")

    # Plateau
    f_plot = np.array([min(f_Hz), max(f_Hz)])
    ax.loglog(f_plot, [V0, V0], 'b--', label='Plateau', linewidth=2)

    # Abfallgerade
    f_fit = np.logspace(
        np.log10(min(f_Hz[-n_fit_end:])),
        np.log10(max(f_Hz)),
        100
    )
    V_fit = 10 ** (steigung * np.log10(f_fit) + achsenabschnitt)
    ax.loglog(f_fit, V_fit, 'r-', label='Abfall (Gerade)', linewidth=2)

    ax.set_title(f"Messung {suffix}")
    ax.set_xlabel("f / Hz")
    ax.set_ylabel("Verstärkung V")
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    ax.legend()

    fig.savefig(f"build/L{suffix}.pdf")
    plt.close(fig)  # Speicher freigeben

# Messungen ausführen
process_measurement("Erste", "1", n_plateau=8, n_fit_end=4)
process_measurement("Zweite", "2", n_plateau=6, n_fit_end=5)
process_measurement("Dritte", "3", n_plateau=6, n_fit_end=3)
process_measurement("Vierte", "4", n_plateau=6, n_fit_end=3)
print("Alle Messungen verarbeitet. PDFs im Ordner 'build/'")



## Invertierender Linearverstärker b)
plt.rcParams["figure.figsize"] = (10,8)
plt.rcParams["font.size"] = 16

def phase(name, suffix):
    f_kHz, phi = np.genfromtxt(f"Daten/LP{suffix}.txt", unpack=True)
    f_Hz = f_kHz * 1e3

    fig, ax = plt.subplots(1,1, layout="constrained")
    ax.semilogx(f_Hz, phi, "k.", label="Messwerte")
    
    ax.set_xlabel("f / Hz")
    ax.set_ylabel(r"$\varphi / °$")
    ax.grid(True, which='both', linestyle='--', alpha=0.7)
    ax.legend()
    fig.savefig(f"build/LP{suffix}.pdf")

# Messungen ausführen
phase("Erste", "1")
phase("Zweite", "2")
phase("Dritte", "3")
phase("Vierte", "4")
print("Alle Phasengänge geplottet. PDFs im Ordner 'build/'")




## Umkehr-Integrator
# Daten einlesen
f_kHz_ui, U_out_ui = np.genfromtxt(f"Daten/ui.txt", unpack=True)
f_Hz_ui = f_kHz_ui * 1e3
V_ui = U_out_ui / U_e

x_log = np.log10(f_Hz_ui)
y_log = np.log10(V_ui)

params, covariance_matrix = np.polyfit(x_log, y_log, deg=1, cov=True)
m_ui = params[0]  # Steigung (erwartet: -1)
n_ui = params[1]  # Achsenabschnitt
uncertainties = np.sqrt(np.diag(covariance_matrix))

# Ausgabe
print("FIT im doppelt-logarithmischen Diagramm:")
print(f"Steigung m = {m_ui:.4f} ± {uncertainties[0]:.4f}")
print(f"Achsenabschnitt n = {n_ui:.4f} ± {uncertainties[1]:.4f}")
print(f"Proportionalität: V = {10**n_ui:.4f} * f^{m_ui:.4f}")

# Plot
x_plot = np.logspace(np.min(np.log10(f_Hz_ui)), np.max(np.log10(f_Hz_ui)), 100)
y_plot = 10**(m_ui * np.log10(x_plot) + n_ui)
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.loglog(f_Hz_ui, V_ui, "k.", label="Messwerte")
ax.loglog(x_plot, y_plot, 'r-', label=f'Ausgleichsgerade', linewidth=2)

ax.set_xlabel("f / Hz")
ax.set_ylabel("Verstärkung V")
ax.grid(True, which='both', linestyle='--', alpha=0.5)
ax.legend()
fig.savefig(f"build/UI.pdf")



## Umkehr-Differenzierer
f_kHz_ud, U_out_ud_mV = np.genfromtxt(f"Daten/ud.txt", unpack=True)
U_out_ud = U_out_ud_mV *1e3
f_Hz_ud = f_kHz_ud * 1e3
V_ud = U_out_ud / U_e

x_log = np.log10(f_Hz_ud)
y_log = np.log10(V_ud)

params, covariance_matrix = np.polyfit(x_log, y_log, deg=1, cov=True)
m_ud = params[0]  # Steigung (erwartet: -1)
n_ud = params[1]  # Achsenabschnitt
uncertainties = np.sqrt(np.diag(covariance_matrix))

# Ausgabe
print("FIT im doppelt-logarithmischen Diagramm:")
print(f"(UD) Steigung m = {m_ud:.4f} ± {uncertainties[0]:.4f}")
print(f"(UD) Achsenabschnitt n = {n_ud:.4f} ± {uncertainties[1]:.4f}")
print(f"(UD) Proportionalität: V = {10**n_ud:.4f} * f^{m_ud:.4f}")

# Plot
x_plot = np.logspace(np.min(np.log10(f_Hz_ud)), np.max(np.log10(f_Hz_ud)), 100)
y_plot = 10**(m_ud * np.log10(x_plot) + n_ud)
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.loglog(f_Hz_ud, V_ud, "k.", label="Messwerte")
ax.loglog(x_plot, y_plot, 'r-', label=f'Ausgleichsgerade', linewidth=2)

ax.set_xlabel("f / Hz")
ax.set_ylabel("Verstärkung V")
ax.grid(True, which='both', linestyle='--', alpha=0.5)
ax.legend()
fig.savefig(f"build/UD.pdf")