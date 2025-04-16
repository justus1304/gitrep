import matplotlib.pyplot as plt
import numpy as np

# Figure erstellen
fig, ax = plt.subplots(figsize=(10, 6))  # Größe anpassbar

# Daten laden und plotten (jede Datei einzeln)
# KL_1
x1, y1 = np.loadtxt("Daten/KL_1.txt", unpack=True)
ax.plot(x1, y1, "x", markersize=5, label=r"$I_\mathrm{H} = 1{,}8\,$ A")

# KL_2
x2, y2 = np.loadtxt("Daten/KL_2.txt", unpack=True)
ax.plot(x2, y2, "x", markersize=5, label=r"$I_\mathrm{H} = 2{,}0\,$ A")

# KL_3
x3, y3 = np.loadtxt("Daten/KL_3.txt", unpack=True)
ax.plot(x3, y3, "x", markersize=5, label=r"$I_\mathrm{H} = 2{,}1\,$ A")

# KL_4
x4, y4 = np.loadtxt("Daten/KL_4.txt", unpack=True)
ax.plot(x4, y4, "x", markersize=5, label=r"$I_\mathrm{H} = 2{,}3\,$ A")

# KL_5
x5, y5 = np.loadtxt("Daten/KL_5.txt", unpack=True)
ax.plot(x5, y5, "x", markersize=5, label=r"$I_\mathrm{H} = 2{,}5\,$ A")

# Achsenbeschriftungen und Legende
ax.set_xlabel("Spannung U [V]", fontsize=20)
ax.set_ylabel("Strom I [mA]", fontsize=20)
ax.legend(framealpha=1, fontsize=20)  # Legende mit Transparenz
ax.tick_params(axis='both', which='major', labelsize=17) # Skalierungszahlen
ax.grid(True, linestyle="--", alpha=0.5)  # Gitterlinien

# Speichern
fig.savefig("build/mw_plot.pdf")