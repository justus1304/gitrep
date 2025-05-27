import matplotlib.pyplot as plt
import numpy as np

theta, R = np.genfromtxt("daten/bragg.txt", unpack = True)
# Maximum finden
max_R = np.max(R)
max_theta = theta[np.argmax(R)]

fig, ax = plt.subplots()

# Messdaten plotten (verbunden mit Linien und Punkten)
ax.plot(theta, R, '-o', color='blue', markersize=5, label='Bragg-Kurve')

# Diagramm gestalten
ax.set_title("Bragg-Reflexion", fontsize=14)
ax.set_xlabel("Winkel θ [°]", fontsize=12)
ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
print("Theta min/max:", np.min(theta), np.max(theta))
print("R min/max:", np.min(R), np.max(R))
ax.set_xlim(26.0, 30.0)
ax.set_ylim(0, 150)

ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

fig.savefig("build/bragg.pdf")


# x = np.linspace(0, 10, 1000)
# y = x ** np.sin(x)

# fig, (ax1, ax2) = plt.subplots(1, 2, layout="constrained")
# ax1.plot(x, y, label="Kurve")
# ax1.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
# ax1.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
# ax1.legend(loc="best")

# ax2.plot(x, y, label="Kurve")
# ax2.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
# ax2.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
# ax2.legend(loc="best")

# fig.savefig("build/plot.pdf")
theta, R = np.genfromtxt("daten/wertejust.txt", unpack = True)
# Maximum finden
max_R = np.max(R)
max_theta = theta[np.argmax(R)]

fig, ax = plt.subplots()

# Messdaten plotten (verbunden mit Linien und Punkten)
ax.plot(theta, R, '-o', color='blue', markersize=5, label='Bragg-Kurve')

# Diagramm gestalten
ax.set_title("Bragg-Reflexion", fontsize=14)
ax.set_xlabel("Winkel θ [°]", fontsize=12)
ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
print("Theta min/max:", np.min(theta), np.max(theta))
print("R min/max:", np.min(R), np.max(R))
ax.set_xlim(0, 30.0)
ax.set_ylim(0, 3000)

ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

fig.savefig("build/wertejust.pdf")









theta, R = np.genfromtxt("daten/wertejust.txt", unpack = True)
# Maximum finden
max_R = np.max(R)
max_theta = theta[np.argmax(R)]

fig, ax = plt.subplots()

# Messdaten plotten (verbunden mit Linien und Punkten)
ax.plot(theta, R, '-o', color='blue', markersize=5, label='Bragg-Kurve')

# Diagramm gestalten
ax.set_title("Bragg-Reflexion", fontsize=14)
ax.set_xlabel("Winkel θ [°]", fontsize=12)
ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
print("Theta min/max:", np.min(theta), np.max(theta))
print("R min/max:", np.min(R), np.max(R))
ax.set_xlim(19, 23.0)
ax.set_ylim(0, 2200)

ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

fig.savefig("build/zoom.pdf")