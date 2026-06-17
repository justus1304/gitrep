import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
from uncertainties import ufloat
from scipy.optimize import curve_fit

x1, y1 = np.genfromtxt("mw_merged.txt", unpack=True)

def f(h,a,b,c):
    return a*h+b*h**2+c*h**3

params1, covariance_matrix1 = curve_fit(f, x1, y1)
uncertainties1 = np.sqrt(np.diag(covariance_matrix1))

print("Fit-Parameter (a, b, c):")
for i, (name, value, err) in enumerate(zip(['a', 'b', 'c'], params1, uncertainties1)):
    print(f"{name} = {value:.6f} ± {err:.6f}")

# Plot erstellen
fig, ax = plt.subplots(1,1, layout="constrained")
# Messpunkte
ax.plot(x1, y1, "o", label="Messwerte")
# Fit Kurven
x_plot = np.linspace(0, 10, 1000)
ax.plot(x_plot, f(x_plot, *params1), "-", label="Fit der Messwerte")

ax.grid(True, alpha=0.3)
ax.legend()
ax.set(xlabel=r"Höhe / km", ylabel=r"Ionenpaare / $cm^3 s$")
fig.savefig("mw_merged.pdf")
