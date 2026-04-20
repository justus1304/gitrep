import matplotlib.pyplot as plt
import numpy as np


def f1():
    x, y =np.genfromtxt("Daten/m1.txt", unpack = True)
    fig, (ax1) = plt.subplots(1,  layout="constrained")
    ax1.plot(x, y, "k.",label = "Steigung des Messpunktes")
    plt.plot([7.3, 7.3], [0, y[11]], 'k--', label='Maximale Steigung')  # gestrichelte schwarze Linie
    ax1.set_xlabel(r"$U / \unit{\volt}$")
    ax1.set_ylabel(r"$I / U / \unit{\nano\ampere\per\volt}$")
    ax1.legend(loc="best")
    fig.savefig("build/plot.pdf")
f1()

def f1():
    x, y =np.genfromtxt("Daten/m2.txt", unpack = True)
    fig, (ax1) = plt.subplots(1,  layout="constrained")
    ax1.plot(x, y, "k.",label = "Steigung des Messpunktes")
    ax1.set_xlabel(r"$U / \unit{\volt}$")
    ax1.set_ylabel(r"$I / U / \unit{\nano\ampere\per\volt}$")
    ax1.legend(loc="best")
    fig.savefig("build/plot2.pdf")
f1()



def linreg():
    #Lineare Regression
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16

    # load data
    x, y = np.genfromtxt("Daten/m3.txt", unpack=True)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    ax.plot(x, y, "k.", label="example data")
    ax.set(xlabel=r"$t \,/\, \mathrm{s}$", ylabel=r"$s \,/\, \mathrm{m}$");

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.3f} ± {error:.3f}")
    ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
    x_plot = np.linspace(0, 9)
    fig, ax = plt.subplots(1, 1, layout="constrained")
    ax.plot(x, y, "k.", label="Position Maxima")
    ax.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Lineare Regression",
        linewidth=1,
        color="tab:orange",
    )
    ax.grid(True)
    ax.legend()
    ax.set(xlabel=r"$n$-tes Maximum", ylabel=r"$U_\text{gegen} / \unit{\volt}$");
    fig.savefig("build/plot3.pdf") 
linreg()