import matplotlib.pyplot as plt
import numpy as np

#Liniare regression Runder Stab Einseitig
plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["font.size"] = 16
# daten aus txt laden
x,a,b = np.genfromtxt("Daten/rSeinseit.txt", unpack=True)
#x aus differenz bilden(Aufgabenspezifisch)
y = a - b
fig, ax = plt.subplots(1, 1, layout="constrained")

params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.3f} ± {error:.3f}")

#x-Achse anzeigebereich
x_plot = np.linspace(225, 525)
# ??
fig, ax = plt.subplots(1, 1, layout="constrained")
#label der Messwerte
ax.plot(x, y, "kx", label="Messwerte",markersize=10,)
ax.grid(True)
#ploten der Ausgleichsgeraden
ax.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label="Lineare Regression",
    #Dicke der linie
    linewidth=1.5,
    #Farbe
    color="tab:blue",
)
#Legende anzeigen lassen (labels)
ax.legend()
#Achsenbeschriftungen
ax.set(xlabel=r"$x / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
fig.savefig("build/plotrSeinseit.pdf")


#Liniare regression Eckiger
plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["font.size"] = 16
# daten aus txt laden
x,a,b = np.genfromtxt("Daten/eSeinseit.txt", unpack=True)
#x aus differenz bilden(Aufgabenspezifisch)
y = a - b
fig, a = plt.subplots(1, 1, layout="constrained")

params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.3f} ± {error:.3f}")

#x-Achse anzeigebereich
x_plot = np.linspace(225, 525)
# ??
fig, ay = plt.subplots(1, 1, layout="constrained")
#label der Messwerte
ay.plot(x, y, "kx", label="Messwerte",markersize=10,)
ay.grid(True)
#ploten der Ausgleichsgeraden
ay.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label="Lineare Regression",
    #Dicke der linie
    linewidth=1.5,
    #Farbe
    color="tab:blue",
)
#Legende anzeigen lassen (labels)
ay.legend()
#Achsenbeschriftungen
ay.set(xlabel=r"$x / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
fig.savefig("build/ploteSeinseit.pdf")







""" # begin solution


# The solution starts here
x, a,b,c,d = np.genfromtxt("datenrSbeidseit.txt", unpack=True)
yr = c-d 
yl = a-b 


def f(x, a, b, c):
    return a * (x + b) ** 2 + c


parameters, covariance_matrix = np.polyfit(x, y, deg=2, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, unc in zip("abc", parameters, uncertainties):
    print(f"{name} = {value:.3f} ± {unc:.3f}")

fig = plt.figure(layout="constrained")
ax = fig.add_subplot()

ax.errorbar(x, y, yerr=e_y, fmt="k.", label="data")

t = np.linspace(-10, 10, 500)
ax.plot(t, f(t, *parameters), label="Fit")
ax.plot(t, t**2, "--", label="Original")

ax.set_xlim(t[0], t[-1])
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$f(t)$")
ax.legend()

plt.savefig("loesung.pdf")
# end solution

 """

























































































#Liniare regression Eckiger
plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["font.size"] = 16
# daten aus txt laden
x,a,b,c,d = np.genfromtxt("Daten/rSbeidseit.txt", unpack=True)
#x aus differenz bilden(Aufgabenspezifisch)
yr = c - d
yl = a - b
xl = x * -1
fig, a = plt.subplots(1, 1, layout="constrained")

params, covariance_matrix = np.polyfit(x, yr, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.3f} ± {error:.3f}")



#x-Achse anzeigebereich
x_plot = np.linspace(-200, 200)
# ??
fig, arechts = plt.subplots(1, 1, layout="constrained")
#label der Messwerte
arechts.plot(xl, yr, "kx", label="Messwerte",markersize=10,)
arechts.grid(True)
#ploten der Ausgleichsgeraden
arechts.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label="Lineare Regression",
    #Dicke der linie
    linewidth=1.5,
    #Farbe
    color="tab:blue",
)

#label der Messwerte
arechts.plot(x, yl, "kx", markersize=10,)


#Legende anzeigen lassen (labels)
arechts.legend()
#Achsenbeschriftungen
arechts.set(xlabel=r"$x / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
fig.savefig("build/plotbeidseitig.pdf")