




import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp

from scipy.optimize import curve_fit
plt.rcParams['figure.figsize']=[8,5]
plt.rcParams['figure.constrained_layout.use']=True
plt.rcParams['legend.frameon']=False
plt.rcParams["xtick.minor.visible"]=True
plt.rcParams["ytick.minor.visible"]=True
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
    return a * x**b




#def rechteck():
#    # Solution
#    u, z ,x = np.genfromtxt("Daten/viereck.txt", unpack=True)
#    #x = np.array([10, 30, 50, 70, 90, 110, 130, 150, 170, 190]) # kHz
#    z = np.array([17.8, 9.01, 4.61, 1.81, -0.19, -1.79, -3.39, -4.59, -6.19, -8.19]) # dB
#    y = 10**(z/20)*0,775
#    
#    par, cov = curve_fit(f, x, y)
#    err = np.sqrt(np.diag(cov))
#
#    initial_guess = [
#    initial_guess
#    1, 1, 1]  # Initial guesses for a, b, c
#    popt, pcov = curve_fit(model, x_data, y_data, p0=initial_guess)
#
#    
#    fig = plt.figure(layout="constrained")
#    ax = fig.add_subplot()
#
#    ax.plot(x, coeff(x, *par), c='olivedrab', label='rect fit')
#    ax.plot(f, U, 'kx', ms=3.21, label='rect data')
#
#    ax.legend()
#    ax.set(xlabel=r"$n$", ylabel=r"$\unit{\volt}$");
#    print(f'a = {par[0]:.2f} +- {err[0]:.2f}')
#    print(f'b = {par[1]:.2f} +- {err[1]:.2f}')
    fig.savefig("build/viereck.pdf")
#    
#rechteck()  



def rechteck():
    # Solution
    u, z ,x = np.genfromtxt("Daten/viereck.txt", unpack=True)

    #x = np.array([10, 30, 50, 70, 90, 110, 130, 150, 170, 190]) # kHz
    #z = np.array([17.8, 9.01, 4.61, 1.81, -0.19, -1.79, -3.39, -4.59, -6.19, -8.19]) # dB
    y = 10**(z/20)*0,775

    y = 0.775 * 10**(z/20)
    print("Rechteck =", y)
    xa = np.linspace(0,190)
    
    params = ucurve_fit(f, u, y,p0 = (4,-1))
    #err = np.sqrt(np.diag(cov))
    print("a*((x**b))")
    for char, p in zip("ab", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(u, y, "k.",label = "Messwerte")
    
    ax.plot(xa, f(xa, *unp.nominal_values(params)), label="Fit")
    
    ax.legend()
    ax.set(xlabel=r"$f \unit{\hertz}$", ylabel=r"$\unit{\volt}$");
    
    fig.savefig("build/viereck.pdf")
    
rechteck()  


########################################################################################



def dreieck():
    # Solution
    u, z ,x = np.genfromtxt("Daten/dreieck.txt", unpack=True)
    y = 0.775 * 10**(z/20)
    print("Dreieck =", y)
    xa = np.linspace(0,190)
    #y = unp.uarray(y_0, y_err)
    params = ucurve_fit(f, u, y)
    print("a*(1/(x**b))")
    for char, p in zip("ab", params):
        print(f"{char} = {p}")
    

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(u, y, "k.",label = "Messwerte")
    #ax.errorbar(x, unp.nominal_values(y), yerr=y_err, fmt=".", label="Daten")
    ax.plot(xa, f(xa, *unp.nominal_values(params)), label="Fit")
    #ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], [0, "π", "2π", "3π"])
    ax.legend()
    ax.set(xlabel=r"$f \unit{\hertz}$", ylabel=r"$\unit{\volt}$");
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
    xa = np.linspace(0,190)
    #y = unp.uarray(y_0, y_err)
    params = ucurve_fit(f, u, y)
    print("a*((x**b))")
    for char, p in zip("ab", params):
        print(f"{char} = {p}")

    fig = plt.figure(layout="constrained")
    ax = fig.add_subplot()
    ax.plot(u, y, "k.",label = "Messwerte")
    #ax.errorbar(x, unp.nominal_values(y), yerr=y_err, fmt=".", label="Daten")
    ax.plot(xa, f(xa, *unp.nominal_values(params)), label="Fit")
    #ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], [0, "π", "2π", "3π"])
    ax.legend()
    ax.set(xlabel=r"$f \unit{\hertz}$", ylabel=r"$\unit{\volt}$");
    #plt.savefig("loesung.pdf")
    fig.savefig("build/saege.pdf")
    # end solution
    # def ucurve_fit(f, x, y, **kwargs):
    #     …
    #     … = scipy.optimize.curve_fit(…, **kwargs)
    #     … """ """
saege()  





#def rechteckCurveFit():
#    params, covariance_matrix = curve_fit(sigmoid, x, y, p0=(-1, 40, 1))
#
#
#    uncertainties = np.sqrt(np.diag(covariance_matrix))
#
#    for name, value, uncertainty in zip("abc", params, uncertainties):
#        print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")
#    ax.cla()
#    x_plot = np.linspace(0, 50, 1000)
#
#    ax.plot(x, y, "o", label="Messwerte")
#    ax.plot(x_plot, sigmoid(x_plot, *params), "-", label="Sigmoid Fit")
#
#    ax.legend()
#    ax.set(xlabel=r"Temperatur / °C", ylabel=r"$GP$")
#    fig
#
#    
#rechteckCurveFit()  




