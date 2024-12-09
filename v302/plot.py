import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem


plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["font.size"] = 16

w0 = 1 / ((1000*663)*10**(-9))
v0 = w0 / (2*np.pi)
print(v0)
#UbrUs = (1/9)*(w**2*R**2*C**2-1)**2 / ((1-w**2*R**2*C**2)**2+9*w**2*R**2*C**2)

x, y = np.genfromtxt("daten/wienrob.txt", unpack=True)

fig, ax = plt.subplots(1, 1, layout="constrained")

print(x)


x_plot = np.linspace(0, 0.6)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.set_yscale("log")
ax.plot(x/v0, np.sqrt((1/9)*((((x*2*np.pi)/w0)**2-1)**2 / ((1-((x*2*np.pi)/w0)**2)**2+9*((x*2*np.pi)/w0)**2))), label = "Errechnete Funktion")
ax.plot(x/v0, 0.001*y, "k.", label="Messwerte")


ax.legend()
ax.set(xlabel=r"$\Omega$", ylabel=r"$\frac{U_{Br}}{U_{s}}$");



fig.savefig("build/plot.pdf")

