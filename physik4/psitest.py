import numpy as np
import matplotlib.pyplot as plt
from scipy.special import airy

# Konstanten (in atomaren Einheiten, vereinfacht)
hbar = 1.0      # Planck-Konstante (kann z. B. auf 1 gesetzt werden)
m = 1.0         # Masse des Teilchens (z. B. Elektronenmasse)
F = 1.0         # Stärke des linearen Potentials (willkürlich gewählt)

# Skalenlänge x0 berechnen
x0 = (hbar**2 / (2 * m * F))**(1/3)  # Charakteristische Längenskala

# Nullstellen der Airy-Funktion Ai(xi) (für die ersten 3 Zustände)
xi_zeros = [-2.338, -4.088, -5.521]  # Erste 3 Nullstellen von Ai(xi)

# Wellenfunktion für den n-ten Zustand plotten (z. B. n = 0, 1, 2)
n = 0  # Quantenzahl (0 = Grundzustand)
xi_n = xi_zeros[n]  # n-te Nullstelle von Ai(xi)
En = -F * x0 * xi_n  # Energie des n-ten Zustands

# x-Bereich definieren (von 0 bis 5 * x0)
x = np.linspace(0, 5 * x0, 500)

# Argument der Airy-Funktion berechnen
xi = (x - En/F) / x0

# Airy-Funktion Ai(xi) berechnen (psi(x) = Ai(xi))
psi, _, _, _ = airy(xi)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, psi, label=f"n = {n}, E = {En:.2f}")
plt.axhline(0, color='black', linestyle='--', alpha=0.5)
plt.axvline(0, color='black', linestyle='-', alpha=0.5)
plt.xlabel("x (in Einheiten von x0)")
plt.ylabel("ψ(x)")
plt.title(f"Wellenfunktion im linearen Potential (n = {n})")
plt.legend()
plt.grid(True)
plt.show()