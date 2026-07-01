import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x, y = np.genfromtxt("Radius_Mag.txt", unpack = True)
y_Tesla = y / 10000

# Plot
fig, ax = plt.subplots(1,1, layout="constrained")
# Messwerte
ax.plot(x, y_Tesla, "o", label="Messwerte")

# Linien einzeichnen
R_plot = np.logspace(0, 18, 100)  # von 1 m bis 10^18 m (deckt alle Quellen ab)

# Konstante für Protonen: B*R = 10^20 eV / c
E_Joule = 1e20 * 1.602e-19
c = 3e8
BR_proton = E_Joule / c  # in T*m
B_proton = BR_proton / R_plot
# Für Eisen: B*R = 10^20 eV / (Z*c)
Z_eisen = 26
BR_eisen = E_Joule / (Z_eisen * c)
B_eisen = BR_eisen / R_plot

# Geraden
ax.plot(R_plot, B_proton, "r--", label=r"Protonen")
ax.plot(R_plot, B_eisen, "b--", label=r"Eisenkerne")

ax.set_xscale('log')
ax.set_yscale('log')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set(xlabel=r"Radius R / m", ylabel=r"Magnetfeldstärke B / T")
fig.savefig("B4Nr20.pdf")