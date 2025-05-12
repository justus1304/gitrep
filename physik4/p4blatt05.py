import numpy as np
import matplotlib.pyplot as plt

# Parameter (willkürlich gewählt, da keine konkreten Werte gegeben)
V0 = 1.0
L = 1.0
hbar = 1.0
m = 1.0
# Werte für x
x_vals = np.linspace(-0.5, 2, 500)

# Fall 1: E = 2V0 (E > V0)
E1 = 2 * V0
k1 = np.sqrt(2 * m * (E1 - V0) / hbar**2)
k3_1 = np.sqrt(2 * m * E1 / hbar**2)
ratio1 = k1 / k3_1

# Wellenfunktion für Fall 1
def psi1(x):
    if x < 0:
        return 0 + 0j
    elif 0 <= x <= L:
        return 1j * 2 * np.sin(k1 * x)
    else:
        return 2 * (1j * np.sin(k1 * L) + ratio1 * np.cos(k1 * L))

# Berechnung für Fall 1
psi1_vals = np.array([psi1(x) for x in x_vals])
real1 = np.real(psi1_vals)
imag1 = np.imag(psi1_vals)
abs_sq1 = np.abs(psi1_vals)**2

# Fall 2: E = V0/2 (E < V0)
E2 = V0 / 2
k2 = np.sqrt(2 * m * (V0 - E2) / hbar**2)
k3_2 = np.sqrt(2 * m * E2 / hbar**2)
ratio2 = k2 / (1j * k3_2)  # Hier ist k1/(ik3) = k2/(ik3_2)

# Wellenfunktion für Fall 2
def psi2(x):
    if x < 0:
        return 0 + 0j
    elif 0 <= x <= L:
        return 2 * np.sinh(k2 * x)
    else:
        return 2 * (np.sinh(k2 * L) - ratio2 * np.cosh(k2 * L))

# Berechnung für Fall 2
psi2_vals = np.array([psi2(x) for x in x_vals])
real2 = np.real(psi2_vals)
imag2 = np.imag(psi2_vals)
abs_sq2 = np.abs(psi2_vals)**2




# Plots
fig = plt.figure(figsize=(12, 8))

# Fall 1: E = 2V0
# Real- und Imaginärteil
plt.subplot(2, 2, 1)
plt.plot(x_vals, real1, label="$Re(\Psi(x))$")
plt.plot(x_vals, imag1, label="$Im(\Psi(x))$")
plt.title("Fall 1: E = 2V0 (Real- und Imaginärteil)")
plt.xlabel(r"$x$")
plt.ylabel(r"$\Psi(x)$")
plt.legend(loc="best")
plt.grid()
# Betragsquadrat
plt.subplot(2, 2, 2)
plt.plot(x_vals, abs_sq1, label=r"$|\Psi(x)|^2$")
plt.title("Fall 1: E = 2V0 (Betragsquadrat)")
plt.xlabel(r"$x$")
plt.ylabel(r"$|\Psi(x)|^2$")
plt.legend()
plt.grid()



# Fall 2: E = V0/2
# Real- und Imaginärteil
plt.subplot(2, 2, 3)
plt.plot(x_vals, real2, label="$Re(\Psi(x))$")
plt.plot(x_vals, imag2, label="$Im(\Psi(x))$")
plt.title("Fall 2: E = V0/2 (Real- und Imaginärteil)")
plt.xlabel(r"$x$")
plt.ylabel(r"$\Psi(x)$")
plt.legend()
plt.grid()
# Betragsquadrat
plt.subplot(2, 2, 4)
plt.plot(x_vals, abs_sq2, label=r"$|\Psi(x)|^2$")
plt.title("Fall 2: E = V0/2 (Betragsquadrat)")
plt.xlabel(r"$x$")
plt.ylabel(r"$|\Psi(x)|^2$")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

fig.savefig("plot2.pdf")