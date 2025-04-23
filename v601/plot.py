import matplotlib.pyplot as plt
import numpy as np


def f1():
    x, y =np.genfromtxt("Daten/m1.txt", unpack = True)
    fig, (ax1) = plt.subplots(1,  layout="constrained")
    ax1.plot(x, y, "k.",label = "Differnzenquotient des Messpunktes")
    ax1.set_xlabel(r"$U / \unit{\volt}$")
    ax1.set_ylabel(r"$I / U / \unit{\nano\ampere\per\volt}$")
    ax1.legend(loc="best")
    fig.savefig("build/plot.pdf")
f1()

def f1():
    x, y =np.genfromtxt("Daten/m2.txt", unpack = True)
    fig, (ax1) = plt.subplots(1,  layout="constrained")
    ax1.plot(x, y, "k.",label = "Differnzenquotient des Messpunktes")
    ax1.set_xlabel(r"$U / \unit{\volt}$")
    ax1.set_ylabel(r"$A / \unit{\nano\ampere}$")
    ax1.legend(loc="best")
    fig.savefig("build/plot2.pdf")
f1()





#def teil2():
#    # Solution
#    r, U = np.genfromtxt("Daten/Teil2.txt", unpack=True)
#
#    
#
#    
#    
#    xa = np.linspace(0,50)
#    
#    params = ucurve_fit(g, r, U)
#    #err = np.sqrt(np.diag(cov))
#    print("a*((x**b))")
#    for char, p in zip("abc", params):
#        print(f"{char} = {p}")
#
#    fig = plt.figure(layout="constrained")
#    ax = fig.add_subplot()
#    ax.plot(r, U, "k.",label = "Messwerte")
#    
#    ax.plot(xa, g(xa, *unp.nominal_values(params)), label="Fit")
#    
#    ax.legend()
#    ax.set(xlabel=r"$r (\unit{\centi\meter})$", ylabel=r"$U (\unit{\volt}$)");
#    
#    fig.savefig("build/teil2.pdf")
#    
#teil2()  