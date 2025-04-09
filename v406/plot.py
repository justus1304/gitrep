import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
#import uncertainties.unumpy as unp
from uncertainties import ufloat
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

#Zu Fitende Funktion
def g(A, x, b):
    #return A**2 * (np.sinc(b * x))**2 * (np.cos(c * x))**2
    return A**2 * (np.sinc(b * x))**2

def teil1():
    # Solution
    x, I = np.genfromtxt("Daten/ESfix.txt", unpack=True)
    #x = x*10**(-3)
    #I = I*10**(-6)
    x = x/1.26
    xa = np.linspace(-0.02,0.02)
    
    #Ucurve fit ausführen
    params, covariance_matrix = curve_fit(g, x, I,p0 = (0.00015,1000))
    #err = np.sqrt(np.diag(cov))
    print("a*((x**b))")
    for char, p in zip("Ab", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(x, I, "k.",label = "Messwerte")
    
    ax.plot(xa, g(xa, *params), label="Fit")
    
    ax.legend()
    #Achsenbeschriftungen für den Plot
    ax.set(xlabel=r"$x (\unit{\milli\meter})$", ylabel=r"$I(\unit{\micro\ampere})$");
    ax.grid(True)
    #x achsen abstände (wahlweise)
    #ax.set_xticks([0, np.pi, 2 * np.pi], [0, "$\pi$", "$2\pi$"])

    fig.savefig("build/teil1.pdf")
    
teil1()  
