import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp

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



def ucurve_fit(f, x, y, **kwargs):
    try:
        sigma = unp.std_devs(y) if np.any(unp.std_devs(y) != 0) else None
    except AttributeError:
        sigma = None
    popt, pcov = scipy.optimize.curve_fit(f, x, unp.nominal_values(y), sigma=sigma, absolute_sigma=True, **kwargs)
    return unc.correlated_values(popt, pcov)

def g(x, a, b):
    return a * x**b 

def langmuir():
    # Daten laden (I in mA, U in V)
    U, I = np.genfromtxt("Daten/KL_5.txt", unpack=True)

    # Fit: I = a * U^b
    params = ucurve_fit(g, U, I)  # U auf x-Achse, I auf y-Achse
    print("Fit-Parameter: a * U^b")
    print(f"a = {params[0]}, b = {params[1]}")

    # Plot
    U_fit = np.linspace(min(U), 110, 100)
    I_fit = g(U_fit, *unp.nominal_values(params))

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(U, I, "k.", label="Messwerte")
    ax.plot(U_fit, I_fit, label="Fit")
    ax.set(xlabel=r"$U (\unit{\volt})$", ylabel=r"$I (\unit{\ampere})$")
    ax.legend()
    fig.savefig("build/langmuir.pdf")

langmuir()



def f(x, a, b):
    return  a * np.exp((-1.602e-19 * x) / (1.381e-23 * b))

def afak():
    U, I = np.genfromtxt("Daten/afak1.txt", unpack=True)

    params = ucurve_fit(f, U, I, p0 =(3*10**(3),1000))  # U auf x-Achse, I auf y-Achse
    print("Fit-Parameter: e")
    print(f"a1 = {params[0]}, b1 = {params[1]}")

    # Plot
    U_fit = np.linspace(min(U), max(U), 100)
    I_fit = f(U_fit, *unp.nominal_values(params))

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(U, I, "k.", label="Messwerte")
    ax.plot(U_fit, I_fit, label="Fit")
    ax.set(xlabel=r"$U (\unit{\volt})$", ylabel=r"$I (\unit{\milli\ampere})$")
    ax.legend()
    fig.savefig("build/f.pdf")

afak()