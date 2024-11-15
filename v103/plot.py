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








import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp


def ucurve_fit(f, x, y, **kwargs):
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = scipy.optimize.curve_fit(
        f, x, unp.nominal_values(y), sigma=sigma, absolute_sigma=True, **kwargs
    )

    return unc.correlated_values(popt, pcov)


def f(x, a, b, c):
    #return a * np.cos(x * b) + c
    return a*(b*x**2 - (1/3) * x**3) + c


# Solution
x, d0links, dxlinks, d0rechts, dxrechts = np.genfromtxt("Daten/rSbeidseit.txt", unpack=True)
yl = d0links - dxlinks
yr = d0rechts - dxrechts
xl = x*(-1)
xr = x


xltemp = [0]*10
i = len(xl) - 1
m = 0
while i>=0:
    xltemp[m] = xl[i]
    i = i - 1
    m = m + 1
    print(i,m)
    

yltemp = [0]*10
i = len(yl) - 1
m = 0
while i>=0:
    yltemp[m] = yl[i]
    i = i - 1
    m = m + 1
    print(i,m)




x = np.append(xltemp, xr)
y = np.append(yltemp, yr)


print(x)
y_err = 0

params = ucurve_fit(f, x, y, maxfev=10000)
print("a * cos(x * b) + c")
for char, p in zip("abc", params):
    print(f"{char} = {p}")

fig = plt.figure(layout="constrained")
ax = fig.add_subplot()
ax.errorbar(x, unp.nominal_values(y), yerr=y_err, fmt=".", label="Daten")
ax.plot(x, f(x, *unp.nominal_values(params)), label="Fit")
#ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], [0, "π", "2π", "3π"])
ax.legend()
plt.savefig("build/loesung.pdf")
# end solution
# def ucurve_fit(f, x, y, **kwargs):
#     …
#     … = scipy.optimize.curve_fit(…, **kwargs)
#     …
















""" # The solution starts here
x, d0links, dxlinks, d0rechts, dxrechts = np.genfromtxt("Daten/rSbeidseit.txt", unpack=True)
yl = d0links - dxlinks
yr = d0rechts - dxrechts
xl = x*(-1)
xr = x


xltemp = [0]*10
i = len(xl) - 1
m = 0
while i>=0:
    xltemp[m] = xl[i]
    i = i - 1
    m = m + 1
    print(i,m)
    

yltemp = [0]*10
i = len(yl) - 1
m = 0
while i>=0:
    yltemp[m] = yl[i]
    i = i - 1
    m = m + 1
    print(i,m)




x = np.append(xltemp, xr)
y = np.append(yltemp, yr)


def f(x, a, b, c):
    #return a * (x + b) ** 2 + c
    return a*(b*x**2 - (1/3) * x**3) + c


parameters, covariance_matrix = np.polyfit(x, y, deg=2, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, unc in zip("abc", parameters, uncertainties):
    print(f"{name} = {value:.3f} ± {unc:.3f}")

fig = plt.figure(layout="constrained")
ax = fig.add_subplot()

ax.errorbar(x, y, yerr=0, fmt="k.", label="data")

t = np.linspace(-200, 200, 10000)
ax.plot(t, f(t, *parameters), label="Fit")
#ax.plot(t, t**2, "--", label="Original")

ax.set_xlim(t[0], t[-1])
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$f(t)$")
ax.legend()

plt.savefig("loesung.pdf")
# end solution """












































































