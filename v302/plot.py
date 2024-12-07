import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

#Liniare regression
plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["font.size"] = 16


#####funktion aus [12]
R = 
UbrUs = (1/9)*(w**2*R**2*C**2-1)**2 / ((1-w**2*R**2*C**2)**2+9*w**2*R**2*C**2)

x, y = np.genfromtxt("daten/wienrob.txt", unpack=True)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, y, "k.", label="example data")
ax.set(xlabel=r"$t \,/\, \mathrm{s}$", ylabel=r"$s \,/\, \mathrm{m}$");

params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.3f} ± {error:.3f}")




x_plot = np.linspace(0, 0.6)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.set_yscale("log")
ax.plot(x, y, "k.", label="Messwerte")
ax.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label="Lineare Regression",
    linewidth=1,
    color="tab:orange",
)

ax.legend()
ax.set(xlabel=r"$a²(cm²)$", ylabel=r"$\symbf{T²}(s²)$");



fig.savefig("build/plot.pdf")

