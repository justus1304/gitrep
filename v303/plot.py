import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp

from scipy.optimize import curve_fit

def ucurve_fit(f, x, y, **kwargs):
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = scipy.optimize.curve_fit(
        f, x, unp.nominal_values(y), sigma=sigma, absolute_sigma=True, **kwargs
    )

    return unc.correlated_values(popt, pcov)


def f(x, a, b, c, d):
    return a * np.cos(b*x + c) + d 

def g(x, a, b, c):
    return a*(1/(x**b)) + c 

def teil1():
    # Solution
    phi, U = np.genfromtxt("Daten/Teil1.txt", unpack=True)

    

    phi = ((2*np.pi)/360) * phi
    
    xa = np.linspace(0,2*np.pi,1000)
    
    params = ucurve_fit(f, phi, U)
    #err = np.sqrt(np.diag(cov))
    print("a*((x**b))")
    for char, p in zip("abcd", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(phi, U, "k.",label = "Messwerte")
    
    ax.plot(xa, f(xa, *unp.nominal_values(params)), label="Fit")
    
    ax.legend()
    ax.set(xlabel=r"$\phi (\unit{\radian})$", ylabel=r"$U(\unit{\volt})$");
    ax.set_xticks([0, np.pi, 2 * np.pi], [0, "$\pi$", "$2\pi$"])
    fig.savefig("build/teil1.pdf")
    
teil1()  


def teil2():
    # Solution
    r, U = np.genfromtxt("Daten/Teil2.txt", unpack=True)

    

    
    
    xa = np.linspace(0,50)
    
    params = ucurve_fit(g, r, U)
    #err = np.sqrt(np.diag(cov))
    print("a*((x**b))")
    for char, p in zip("abc", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(r, U, "k.",label = "Messwerte")
    
    ax.plot(xa, g(xa, *unp.nominal_values(params)), label="Fit")
    
    ax.legend()
    ax.set(xlabel=r"$r (\unit{\centi\meter})$", ylabel=r"$U (\unit{\volt}$)");
    
    fig.savefig("build/teil2.pdf")
    
teil2()  