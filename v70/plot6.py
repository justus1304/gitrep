import matplotlib.pyplot as plt
import numpy as np

# Plot-Style für wissenschaftliche Protokolle einstellen
plt.rcParams.update({
    "font.size": 11,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "grid.alpha": 0.5,
    "grid.linestyle": "--"
})

# =============================================================================
# 1. MESSWERTE IN LITER PRO SEKUNDE (L/s) AUS DEINEM PROTOKOLL
# =============================================================================

# --- DREHSCHIEBERPUMPE (DP) ---
# Evakuierungsmethode (3 Bereiche, Werte im Text in m³/h -> Umrechnung durch 3.6)
dp_eva_S = np.array([4.9, 1.71, 0.70]) / 3.6
dp_eva_S_err = np.array([0.5, 0.17, 0.07]) / 3.6
# Zugehörige Druckbereiche (vollständig durchgezogen von p_start bis p_end)
dp_eva_p_start = np.array([1006.0, 2.9, 0.36])
dp_eva_p_end = np.array([2.9, 0.36, 0.076])

# Leckratenmethode (4 Messungen, im Text bereits in L/s angegeben)
dp_leck_p = np.array([0.20, 6.30, 56.4, 86.0])
# x-Fehler basierend auf der Gerätespezifikation des TPG-202 aus dem Protokoll
dp_leck_p_err = np.array([0.02, 0.63, 3.6, 3.6])
dp_leck_S = np.array([0.48, 1.59, 1.24, 1.53])
dp_leck_S_err = np.array([0.15, 0.50, 0.39, 0.48])


# --- TURBOMOLEKULARPUMPE (TP) ---
# Evakuierungsmethode (2 Bereiche, im Text bereits in L/s angegeben)
tp_eva_S = np.array([15.4, 0.41])
tp_eva_S_err = np.array([1.6, 0.05])
# Zugehörige Druckbereiche
tp_eva_p_start = np.array([5.01e-3, 2.44e-5])
tp_eva_p_end = np.array([1.29e-3, 4.52e-6])

# Leckratenmethode (4 Messungen, im Text bereits in L/s angegeben)
tp_leck_p = np.array([5.04e-5, 6.96e-5, 1.03e-4, 1.91e-4])
# x-Fehler basierend auf der 30%-Messungenauigkeit der PKR-360-Sensoren
tp_leck_p_err = tp_leck_p * 0.30
tp_leck_S = np.array([20.1, 39.2, 26.5, 28.1])
tp_leck_S_err = np.array([6.4, 12.4, 8.4, 8.9])


# =============================================================================
# 2. ERSTELLUNG DER PLOTS
# =============================================================================

# --- PLOT 1: Drehschieberpumpe ---
fig1, ax1 = plt.subplots(figsize=(7, 5))

# Leckrate als diskrete Messpunkte plotten (mit xerr UND yerr)
ax1.errorbar(
    dp_leck_p, dp_leck_S, 
    xerr=dp_leck_p_err, yerr=dp_leck_S_err, 
    fmt="s", color="navy", capsize=4, elinewidth=1.2, zorder=3,
    label="Leckratenmethode zu vier gleichgewchtsdrücken"
)

# Evakuierungsbereiche als voll durchgezogene Balken über den gesamten Bereich plotten
for i in range(3):
    lbl = "Evakuierungsmethode" if i == 0 else ""
    # Horizontale Linie über das gesamte Druckintervall des Bereichs ziehen
    ax1.plot([dp_eva_p_start[i], dp_eva_p_end[i]], [dp_eva_S[i], dp_eva_S[i]], color="crimson", lw=2.5, zorder=2, label=lbl)
    # Unsicherheitsband über den gesamten Bereich schattieren
    ax1.fill_between([dp_eva_p_start[i], dp_eva_p_end[i]], dp_eva_S[i] - dp_eva_S_err[i], dp_eva_S[i] + dp_eva_S_err[i], color="crimson", alpha=0.15, zorder=1)

# Herstellerangabe umgerechnet in L/s (4.6/3.6 bis 5.5/3.6)
ax1.axhspan(4.6/3.6, 5.5/3.6, color="gray", alpha=0.12, linestyle="--", label="Herstellerangabe $S$ ($4.6 - 5.5$ m$^3$/h)")

# Achsen-Konfiguration (X-Achse logarithmisch)
ax1.set_xscale("log")
ax1.set_xlabel("Druck $p$ / mbar")
ax1.set_ylabel("Effektives Saugvermögen $S_{eff}$ / (L/s)")

ax1.grid(True, which="both")
ax1.legend(loc="lower right")
plt.tight_layout()
plt.savefig("saugvermoegen_drehschieberpumpe_final.pdf")
plt.close()


# --- PLOT 2: Turbomolekularpumpe ---
fig2, ax2 = plt.subplots(figsize=(7, 5))

# Leckrate als diskrete Messpunkte plotten (mit xerr UND yerr)
ax2.errorbar(
    tp_leck_p, tp_leck_S, 
    xerr=tp_leck_p_err, yerr=tp_leck_S_err, 
    fmt="s", color="navy", capsize=4, elinewidth=1.2, zorder=3,
    label="Leckratenmethode zu vier Gleichgewichtsdrücken"
)

# Evakuierungsbereiche als voll durchgezogene Balken über den gesamten Bereich plotten
for i in range(2):
    lbl = "Evakuierungsmethode" if i == 0 else ""
    ax2.plot([tp_eva_p_start[i], tp_eva_p_end[i]], [tp_eva_S[i], tp_eva_S[i]], color="crimson", lw=2.5, zorder=2, label=lbl)
    ax2.fill_between([tp_eva_p_start[i], tp_eva_p_end[i]], tp_eva_S[i] - tp_eva_S_err[i], tp_eva_S[i] + tp_eva_S_err[i], color="crimson", alpha=0.15, zorder=1)

# Herstellerangabe (77 L/s für N2)
ax2.axhline(77.0, color="black", linestyle="--", alpha=0.6, label="Herstellerangabe $S$ ($77$ L/s)")

# Achsen-Konfiguration (X-Achse logarithmisch)
ax2.set_xscale("log")
ax2.set_xlabel("Druck $p$ / mbar")
ax2.set_ylabel("Effektives Saugvermögen $S_{eff}$ / (L/s)")

ax2.grid(True, which="both")
ax2.legend(loc="upper left")
plt.tight_layout()
plt.savefig("saugvermoegen_turbopumpe_final.pdf")
plt.close()

print("Die Grafiken wurden erfolgreich mit x- und y-Fehlerbalken generiert!")