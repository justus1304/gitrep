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
def g(phi1, A, b):
    #return A**2 * (np.sinc(b * x))**2 * (np.cos(c * x))**2
    return A**2 * (np.sinc(b * phi1))**2
    #return A**2 * b**2 * ((600*10**(-9))/(np.pi * b * phi1))**2 * (np.sin((np.pi * b * phi1) / (600*10**(-9))))**2

def f(x, A, b, s, d):
    return A**2 * (np.sinc(b * (x-d)))**2 * (np.cos(s * (x-d)))**2 
    #return 4 * (np.cos( (np.pi * 1.26 * np.sin(phi) ) /633*10**(-9) ) )**2 * (633*10**(-9) / (np.pi * b * np.sin(phi)))**2 * (np.sin((np.pi * b * np.sin(phi)) / 633*10**(-9)))**2


def teil1():
    # Solution
    x, I = np.genfromtxt("Daten/ESfix.txt", unpack=True)
    x = x*10**(0)
    I = I*10**(0)
    phi1 = x/1.26
    xa = np.linspace(-25,25, 2000)
    #phi1 = np.full_like(x,0)
    #for i in range(len(x)):
    #    phi1[i] = np.arctan((x[i])/1.26)
    #Ucurve fit ausführen
    params, covariance_matrix = curve_fit(g, phi1, I,p0 = (0.15,0.1))
    #params, covariance_matrix = curve_fit(g, phi1, I,p0 = (26,77))
    #err = np.sqrt(np.diag(cov))
    print("a*((x**b))")
    for char, p in zip("Ab", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(phi1, I, "k.",label = "Messwerte")
    
    ax.plot(xa, g(xa, *params), label="Fit")
    
    ax.legend()
    #Achsenbeschriftungen für den Plot
    ax.set(xlabel=r"$x (\unit{\milli\meter})$", ylabel=r"$I(\unit{\micro\ampere})$");
    ax.grid(True)
    #x achsen abstände (wahlweise)
    #ax.set_xticks([0, np.pi, 2 * np.pi], [0, "$\pi$", "$2\pi$"])

    fig.savefig("build/teil1.pdf")
    
teil1()  


def teil2():
    # Solution
    x, I = np.genfromtxt("Daten/DSNeu.txt", unpack=True)
    x = x*10**(0) #- 25
    I = I*10**(0)
    #phi2 = x/1.26
    phi2 = np.full_like(x,0)
    for i in range(len(x)):
        phi2[i] = np.arctan((x[i]) / 1.26)
    xa = np.linspace(-25,25,200000)
    #phi1 = np.full_like(x,0)
    #for i in range(len(x)):
    #    phi1[i] = np.arctan((x[i])/1.26)
    #Ucurve fit ausführen
    params, covariance_matrix = curve_fit(f, x, I,p0 = (60,1,1, -0.1))
    #params, covariance_matrix = curve_fit(f, phi2, I,p0 = (5 * 10**(-7),1, 1))
    #err = np.sqrt(np.diag(cov))
    print("a*((x**b))")
    for char, p in zip("Absd", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.bar(x, I, width=0.00001, color='red')
    ax.plot(x, I, "kx",label = "Messwerte", markersize=2)
    
    ax.plot(xa, f(xa, *params), label="Fit")
    
    ax.legend()
    #Achsenbeschriftungen für den Plot
    ax.set(xlabel=r"$x (\unit{\milli\meter})$", ylabel=r"$I(\unit{\micro\ampere})$");
    ax.grid(True)
    #x achsen abstände (wahlweise)
    #ax.set_xticks([0, np.pi, 2 * np.pi], [0, "$\pi$", "$2\pi$"])

    fig.savefig("build/teil2.pdf")
teil2()  
