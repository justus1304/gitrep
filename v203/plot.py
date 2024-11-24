import matplotlib.pyplot as plt
import numpy as np

from uncertainties import ufloat

import uncertainties.unumpy as unp
from scipy.stats import sem

#
#def liniareRegression():
#    #Liniare regression Runder Stab Einseitig
#    plt.rcParams["figure.figsize"] = (6, 4)
#    plt.rcParams["font.size"] = 16
#    # daten aus txt laden
#    x , y = np.genfromtxt("Daten/hmesswerte.txt", unpack=True)
#    #x aus differenz bilden(Aufgabenspezifisch)
#    y0 = 967
#    x = (x + 273.15)
#    x = 1/x
#    y = y * (10**5)
# 
#    y = np.log(y/y0)
#
#    fig, ax = plt.subplots(1, 1, layout="constrained")
#
#    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
#    errors = np.sqrt(np.diag(covariance_matrix))
#    for name, value, error in zip("ab", params, errors):
#        print(f"{name} = {value:.4f} ± {error:.4f}")
#
#    #x-Achse anzeigebereich
#    x_plot = np.linspace(0.0026, 0.0034)
#    # ??
#    fig, ax = plt.subplots(1, 1, layout="constrained")
#    #label der Messwerte
#    ax.plot(x, y, "kx", label="Messwerte",markersize=4,)
#    ax.grid(True)
#    #ploten der Ausgleichsgeraden
#    ax.plot(
#        x_plot,
#        params[0] * x_plot + params[1],
#        label="Lineare Regression",
#        #Dicke der linie
#        linewidth=1.5,
#        #Farbe
#        color="tab:red",
#    )
#    #Legende anzeigen lassen (labels)
#    ax.legend()
#    #Achsenbeschriftungen
#    ax.set(xlabel=r"$\frac{1}{L} \unit{\per\celsius}$ ", ylabel=r"$\ln\left(\frac{L}{R}\right)$");
#    fig.savefig("build/linreg.pdf")
#
#
#liniareRegression()






#def ausgleichspolynom():
#        # begin solution
#    
#
#    
#
#    # The solution starts here
#    x, y = np.genfromtxt("Daten/teil2.txt", unpack=True)
#    x = (x + 273.15)
#    
#    y = y * (10**5)
#
#    def f(x, a, b, c, d):
#        return a*x**3+b*x**2+c*x+d
#
#
#    parameters, covariance_matrix = np.polyfit(x, y, deg=3, cov=True)
#    uncertainties = np.sqrt(np.diag(covariance_matrix))
#
#    for name, value, unc in zip("abcd", parameters, uncertainties):
#        print(f"{name} = {value:.3f} ± {unc:.3f}")
#
#    fig = plt.figure(layout="constrained")
#    ax = fig.add_subplot()
#
#    ax.errorbar(x, y, yerr=0, fmt="k.", label="data")
#
#    t = np.linspace(380, 490, 490)
#    ax.plot(t, f(t, *parameters), label="Fit")
#    
#
#    ax.set_xlim(t[0], t[-1])
#    ax.set_xlabel(r"$T/\unit{\kelvin}$")
#    ax.set_ylabel(r"$p/\unit{\pascal}$")
#    ax.legend()
#
#    plt.savefig("build/ausgleichspolynom.pdf")
#    # end solution
#
#
#ausgleichspolynom()




def minusWurzel():
    # begin solution
    #a = ufloat(-1.057 , 0.737)
    #b = ufloat(1531.298 , 959.786)
    #c = ufloat(-714342.798 , 415959.850)
    #d = ufloat(108512685.516 , 59968812.507)


    a = -1.057 
    b = 1531.298 
    c = -714342.798 
    d = 108512685.516 

    R = 8.314
    k = 0.9
    # The solution starts here
    #p = (a*x**3+b*x**2+c*x+d)

   

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    #x = 440
    #print((R*x/2*(a*x**3+b*x**2+c*x+d))-np.sqrt((R*x/2*(a*x**3+b*x**2+c*x+d))**2 -(k/(a*x**3+b*x**2+c*x+d))))
    #print(np.sqrt((R*x/2*(a*x**3+b*x**2+c*x+d))**2 -(k/(a*x**3+b*x**2+c*x+d))))
    #print((R*x/2*(a*x**3+b*x**2+c*x+d)))
    #print(np.sqrt((R*x/(2*(a*x**3+b*x**2+c*x+d)))**2 + 30000000000000000))

    x = np.linspace(380, 490)
    
    ax.plot(x, x*(((R*x)/(2*(a*x**3+b*x**2+c*x+d)))-np.sqrt(((R*x)/(2*(a*x**3+b*x**2+c*x+d)))**2 -(k/(a*x**3+b*x**2+c*x+d)))) * (3*a*x**2+2*b*x+c) , "--", label="Original")

    #ax.set_xlim(t[0], t[-1])
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$f(t)$")
    ax.legend()

    plt.savefig("build/minus.pdf")
    # end solution
minusWurzel()