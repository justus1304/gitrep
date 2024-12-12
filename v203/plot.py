import matplotlib.pyplot as plt
import numpy as np

from uncertainties import ufloat

import uncertainties.unumpy as unp
from scipy.stats import sem


def liniareRegression():
    #Liniare regression Runder Stab Einseitig
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    x , y = np.genfromtxt("Daten/hmesswerte.txt", unpack=True)
    #x aus differenz bilden(Aufgabenspezifisch)
    y0 = 967
    x = (x + 273.15)
    x = 1/x
    y = y * (10**5)
 
    y = np.log(y/y0)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.4f} ± {error:.4f}")

    #x-Achse anzeigebereich
    x_plot = np.linspace(0.0026, 0.0035)
    # ??
    fig, ax = plt.subplots(1, 1, layout="constrained")
    #label der Messwerte
    ax.plot(x, y, "kx", label="Messwerte",markersize=4,)
    ax.grid(True)
    #ploten der Ausgleichsgeraden
    ax.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Lineare Regression",
        #Dicke der linie
        linewidth=1.5,
        #Farbe
        color="tab:red",
    )
    ax.set_xlim(0.0026,0.0035)
    #Legende anzeigen lassen (labels)
    ax.legend()
    ax.set_xlim(0.0026, 0.00345)
    #Achsenbeschriftungen
    ax.set(xlabel=r"$\frac{1}{T} \unit{\per\kelvin}$ ", ylabel=r"$\ln\left(\frac{p}{p_0}\right)$");
    fig.savefig("build/linreg.pdf")


liniareRegression()
def ausgleichspolynom():
        # begin solution
    

    

    # The solution starts here
    x, y = np.genfromtxt("Daten/teil2.txt", unpack=True)
    
    x = (x + 273.15)
    
    y = y * (10**5)

    def f(x, a, b, c, d):
        return a*x**3+b*x**2+c*x+d


    parameters, covariance_matrix = np.polyfit(x, y, deg=3, cov=True)
    uncertainties = np.sqrt(np.diag(covariance_matrix))

    for name, value, unc in zip("abcd", parameters, uncertainties):
        print(f"{name} = {value:.3f} ± {unc:.3f}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()

    ax.errorbar(x, y, yerr=0, fmt="k.", label="Messwerte")

    t = np.linspace(380, 480, 490)
    ax.plot(t, f(t, *parameters), label="Fit")
    

    ax.set_xlim(t[0], t[-1])
    ax.set_xlabel(r"$T/\unit{\kelvin}$")
    ax.set_ylabel(r"$p/\unit{\pascal}$")
    ax.legend()

    plt.savefig("build/ausgleichspolynom.pdf")
    # end solution


ausgleichspolynom()




def minusWurzel():
    # begin solution
    a = ufloat(-1.057 , 0.737)
    b = ufloat(1531.298 , 959.786)
    c = ufloat(-714342.798 , 415959.850)
    d = ufloat(108512685.516 , 59968812.507)


    a = -1.057 
    b = 1531.298 
    c = -714342.798 
    d = 108512685.516 

    #a = -0.069
    #b = 119.646
    #c = -77106.92
    #d = 22020141.506
    #e = -2352273515.481

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
    #f(x) = a*x**3+b*x**2
    ax.plot(x, x*(((R*x)/(2*(a*x**3+b*x**2+c*x+d)))-np.sqrt(((R*x)/(2*(a*x**3+b*x**2+c*x+d)))**2 -(k/(a*x**3+b*x**2+c*x+d)))) * (3*a*x**2+2*b*x+c) , "--", label="Original")
    #ax.plot(x, x*(((R*x)/(2*(a*x**4+b*x**3+c*x**2+d*x+e)))-np.sqrt(((R*x)/(2*(a*x**4+b*x**3+c*x**2+d*x+e)))**2 -(k/(a*x**4+b*x**3+c*x**2+d*x+e)))) * (4*a*x**3+3*b*x**2+2*c*x+d) , "--", label="Original")

    #ax.set_xlim(t[0], t[-1])
    ax.set_xlabel(r"$T/\unit{\kelvin}$")
    ax.set_ylabel(r"$L_-/\unit{\per\mol}$")
    ax.legend()

    plt.savefig("build/minus.pdf")
    # end solution
minusWurzel()




def plusWurzel():
    # begin solution
    #a = ufloat(-1.057 , 0.737)
    #b = ufloat(1531.298 , 959.786)
    #c = ufloat(-714342.798 , 415959.850)
    #d = ufloat(108512685.516 , 59968812.507)


    #a = -3.999
    #b = 5474.980
    #c = -2474994.276
    #d = 370252765.725

    a = -1.057 
    b = 1531.298 
    c = -714342.798 
    d = 108512685.516 

    #a = -0.069
    #b = 119.646
    #c = -77106.92
    #d = 22020141.506
    #e = -2352273515.481

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

    x = np.linspace(380,490)
    
    ax.plot(x, x*(((R*x)/(2*(a*x**3+b*x**2+c*x+d)))+np.sqrt(((R*x)/(2*(a*x**3+b*x**2+c*x+d)))**2 -(k/(a*x**3+b*x**2+c*x+d)))) * (3*a*x**2+2*b*x+c) , "--", label="Original")
    #ax.plot(x, x*(((R*x)/(2*(a*x**4+b*x**3+c*x**2+d*x+e)))+np.sqrt(((R*x)/(2*(a*x**4+b*x**3+c*x**2+d*x+e)))**2 -(k/(a*x**4+b*x**3+c*x**2+d*x+e)))) * (4*a*x**3+3*b*x**2+2*c*x+d) , "--", label="Original")

    #ax.set_xlim(t[0], t[-1])
    ax.set_xlabel(r"$T/\unit{\kelvin}$")
    ax.set_ylabel(r"$L_+/\unit{\per\mol}$")
    ax.legend()

    plt.savefig("build/plus.pdf")
    # end solution
plusWurzel()