


"""     """ #Curve fit

#includs curve fit
import matplotlib.pyplot as plt
import numpy as np
#import scipy.optimize
#import uncertainties as unc
#import uncertainties.unumpy as unp
#
#
#def ucurve_fit(f, x, y, **kwargs):
#    if np.any(unp.std_devs(y) == 0):
#        sigma = None
#    else:
#        sigma = unp.std_devs(y)
#
#    popt, pcov = scipy.optimize.curve_fit(
#        f, x, unp.nominal_values(y), sigma=sigma, absolute_sigma=True, **kwargs
#    )
#
#    return unc.correlated_values(popt, pcov)
#
#
#def f(x, a, b):
#    return a * x + b
#
#
#
#
#y = f(x, 1, 1) 
#
#
#
## Solution
#x, y_0 = np.genfromtxt("daten.txt", unpack=True)
##y = unp.uarray(y_0, y_err)
#params = ucurve_fit(f, x, y)
#print("a * x + b")
#for char, p in zip("ab", params):
#    print(f"{char} = {p}")
#
#fig = plt.figure(layout="constrained")
#ax = fig.add_subplot()
##ax.errorbar(x, unp.nominal_values(y), yerr=y_err, fmt=".", label="Daten")
#ax.plot(x, f(x, *unp.nominal_values(params)), label="Fit")
#ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], [0, "π", "2π", "3π"])
#ax.legend()
##plt.savefig("loesung.pdf")
#fig.savefig("build/plot.pdf")
## end solution
## def ucurve_fit(f, x, y, **kwargs):
##     …
##     … = scipy.optimize.curve_fit(…, **kwargs)
##     … """ """
#


def dreieck():
        #Lineare Regression
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16

    # load data
    x, y = np.genfromtxt("Daten/dreieck.txt", unpack=True)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    ax.plot(x, y, "k.", label="example data")
    ax.set(xlabel=r"$t \,/\, \mathrm{s}$", ylabel=r"$s \,/\, \mathrm{m}$");

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)

    errors = np.sqrt(np.diag(covariance_matrix))

    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.3f} ± {error:.3f}")




    x_plot = np.linspace(0, 20)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    ax.plot(x, y, "k.", label="Messwerte")
    ax.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Lineare Regression",
        linewidth=1,
        color="tab:orange",
    )

    ax.legend()
    ax.set(xlabel=r"$\Delta x$", ylabel=r"$\symbf{F}(N)$");



    fig.savefig("build/dreieck.pdf")
dreieck()

def saegezahn():
    #Lineare Regression
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16

    # load data
    x, y = np.genfromtxt("Daten/säge.txt", unpack=True)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    ax.plot(x, y, "k.", label="example data")
    ax.set(xlabel=r"$t \,/\, \mathrm{s}$", ylabel=r"$s \,/\, \mathrm{m}$");

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)

    errors = np.sqrt(np.diag(covariance_matrix))

    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.3f} ± {error:.3f}")




    x_plot = np.linspace(0, 20)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    ax.plot(x, y, "k.", label="Messwerte")
    ax.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Lineare Regression",
        linewidth=1,
        color="tab:orange",
    )

    ax.legend()
    ax.set(xlabel=r"$\Delta x$", ylabel=r"$\symbf{F}(N)$");



    fig.savefig("build/saegezahn.pdf")
saegezahn()