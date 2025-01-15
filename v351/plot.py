



import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp


#includs curve fit

def ucurve_fit(f, x, y, **kwargs):
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = scipy.optimize.curve_fit(
        f, x, unp.nominal_values(y), sigma=sigma, absolute_sigma=True, **kwargs
    )

    return unc.correlated_values(popt, pcov)


def f(x, a, b):
    return a*((x**b))







def rechteck():
    # Solution
    u, z ,x = np.genfromtxt("Daten/viereck.txt", unpack=True)
    y = 10**(z/20)
    print("Rechteck =", y)
    xa = np.linspace(0,15)
    
    params = ucurve_fit(f, x, y,p0 = (4,-1))
    print("a*((x**b))")
    for char, p in zip("ab", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(x, y, "k.",label = "Messwerte")
    
    ax.plot(xa, f(xa, *unp.nominal_values(params)), label="Fit")
    
    ax.legend()
    ax.set(xlabel=r"$n$", ylabel=r"$\unit{\volt}$");
    
    fig.savefig("build/viereck.pdf")
    
rechteck()  


########################################################################################



def dreieck():
    # Solution
    u, z ,x = np.genfromtxt("Daten/dreieck.txt", unpack=True)
    y = 10**(z/20)
    print("Dreieck =", y)
    xa = np.linspace(0,15)
    #y = unp.uarray(y_0, y_err)
    params = ucurve_fit(f, x, y)
    print("a*(1/(x**b))")
    for char, p in zip("ab", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(x, y, "k.",label = "Messwerte")
    #ax.errorbar(x, unp.nominal_values(y), yerr=y_err, fmt=".", label="Daten")
    ax.plot(xa, f(xa, *unp.nominal_values(params)), label="Fit")
    #ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], [0, "π", "2π", "3π"])
    ax.legend()
    ax.set(xlabel=r"$n$", ylabel=r"$\unit{\volt}$");
    #plt.savefig("loesung.pdf")
    fig.savefig("build/dreieck.pdf")
    # end solution
    # def ucurve_fit(f, x, y, **kwargs):
    #     …
    #     … = scipy.optimize.curve_fit(…, **kwargs)
    #     … """ """
dreieck()  


#############################################################


def saege():
    # Solution
    u, z ,x = np.genfromtxt("Daten/saege.txt", unpack=True)
    y = 10**(z/20)
    print("Saege =", y)
    xa = np.linspace(0,15)
    #y = unp.uarray(y_0, y_err)
    params = ucurve_fit(f, x, y)
    print("a*((x**b))")
    for char, p in zip("ab", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(x, y, "k.",label = "Messwerte")
    #ax.errorbar(x, unp.nominal_values(y), yerr=y_err, fmt=".", label="Daten")
    ax.plot(xa, f(xa, *unp.nominal_values(params)), label="Fit")
    #ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], [0, "π", "2π", "3π"])
    ax.legend()
    ax.set(xlabel=r"$n$", ylabel=r"$\unit{\volt}$");
    #plt.savefig("loesung.pdf")
    fig.savefig("build/saege.pdf")
    # end solution
    # def ucurve_fit(f, x, y, **kwargs):
    #     …
    #     … = scipy.optimize.curve_fit(…, **kwargs)
    #     … """ """
saege()  