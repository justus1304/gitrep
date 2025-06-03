import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import nominal_values as noms, std_devs as stds
import scipy.constants as const
import scipy.optimize
import sympy
import uncertainties as unc
from uncertainties import ufloat
from scipy.constants import h,c
def bragg():
    theta, R = np.genfromtxt("daten/bragg.txt", unpack = True)
    # Maximum finden
    max_R = np.max(R)
    max_theta = theta[np.argmax(R)]

    fig, ax = plt.subplots()

    # Messdaten plotten (verbunden mit Linien und Punkten)
    ax.plot(theta, R, '-o', color='blue', markersize=1, label='Bragg-Kurve')

    # Diagramm gestalten
   
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel(r"$\text{Reflexionsintensität } R\, / \frac{\text{Imp}}{s}$", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(26.0, 30.0)
    ax.set_ylim(0, 150)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/bragg.pdf")
bragg()

def spektrum():
    theta, R = np.genfromtxt("daten/wertejust.txt", unpack = True)
    # Maximum finden
    max_R = np.max(R)
    max_theta = theta[np.argmax(R)]

    fig, ax = plt.subplots()

    # Messdaten plotten (verbundax.set_title("Bragg-Reflexion", fontsize=14)en mit Linien und Punkten)
    ax.plot(theta, R, 'x', color='black', markersize=7,markeredgewidth=0.3, label='Messwerte')
    ax.plot(theta[20:][:-115], R[20:][:-115], '-', color='blue', markersize=1, label='Bremsberg')
    ax.plot(theta[158:][:-95], R[158:][:-95], '-', color='red', markersize=1, label="$K_a - Linie$")
    ax.plot(theta[180:][:-70], R[180:][:-70], '-', color='yellow', markersize=1, label="$K_b - Linie$")
    
    # Diagramm gestalten
    
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel(r"$\text{Reflexionsintensität } R\, / \frac{\text{Imp}}{s}$", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(0, 30.0)
    ax.set_ylim(0, 3000)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/wertejust.pdf")
spektrum()

def minl(t,d):
    return 2*d*unp.sin(t)
def maxe(l):
    return (h*c)/l
def E(t,d):
    return maxe(minl(t*np.pi/180, d))
def f(x,R):
    return 0*x+R

def bog(g):
    return g*np.pi /180

def zoom():
    theta, R = np.genfromtxt("daten/wertejust.txt", unpack = True)
    # Maximum finden
    max_R = np.max(R)
    max_theta = theta[np.argmax(R)]
    print("1. Maximum= ", max_R)
     # Maximum  zwei finden
    max_R2 = np.max(R[:-90])
    max_theta2 = theta[np.argmax(R[:-90])]
    print("2. Maximum= ", max_R2)
    fig, ax = plt.subplots()
    x = np.linspace(19,23,1000)

    # Messdaten plotten (verbunden mit Linien und Punkten)
    ax.plot(theta, R, '-x', color='red', markersize=5, label='Messwerte')
    ax.plot(x, f(x,max_R/2), '-', color='blue', markersize=5, label='Höhe 1. Halbwertsbreite')
    ax.plot(x, f(x,max_R2/2), '-', color='yellow', markersize=5, label='Höhe 2. Halbwertsbreite')

    # Diagramm gestalten
   
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel(r"$\text{Reflexionsintensität } R\, / \frac{\text{Imp}}{s}$", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(19, 23.0)
    ax.set_ylim(0, 2200)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/zoom.pdf")
    tg = ufloat(5.7, 0.1)
    #mimimale wellenlänge max energie
    print("minl =", minl(bog(tg),201.4*10**(0)))
    print("maxE =",maxe(minl(bog(tg),201.4*10**(0))/1000))
    print(h,c)
zoom()

def aufloesung():
    print(E(5.7, 201.4*10**(-12)))
aufloesung()


def strontium():
    theta, R = np.genfromtxt("daten/strontium.txt", unpack = True)
    # Maximum finden
    max_R = np.max(R)
    max_theta = theta[np.argmax(R)]
    x = np.linspace(10,12,1000)
    fig, ax = plt.subplots()
    mittelwert = np.mean(R)
    # Messdaten plotten (verbunden mit Linien und Punkten)
    ax.plot(theta, R, '-x', color='blue', markersize=1, label='Meswerte')
    ax.plot(x, f(x,mittelwert), '-', color='red', markersize=1, label='Mittelwert')

    # Diagramm gestalten
   
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel(r"$\text{Reflexionsintensität } R\, / \frac{\text{Imp}}{s}$", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(10.0, 12.0)
    ax.set_ylim(17, 50)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/strontium.pdf")
strontium()    

def gallium():
    theta, R = np.genfromtxt("daten/gallium.txt", unpack = True)
    # Maximum finden
    max_R = np.max(R)
    max_theta = theta[np.argmax(R)]
    x = np.linspace(16.3,18.3,1000)
    fig, ax = plt.subplots()
    mittelwert = np.mean(R)
    print(mittelwert)
    # Messdaten plotten (verbunden mit Linien und Punkten)
    ax.plot(theta, R, '-x', color='blue', markersize=1, label='Meswerte')
    ax.plot(x, f(x,mittelwert), '-', color='red', markersize=1, label='Mittelwert')
    ax.plot(2)
    # Diagramm gestalten
   
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel(r"$\text{Reflexionsintensität } R\, / \frac{\text{Imp}}{s}$", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(16.3, 18.3)
    ax.set_ylim(11, 25)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/gallium.pdf")
gallium()    


def zink():
    theta, R = np.genfromtxt("daten/zink.txt", unpack = True)
    # Maximum finden
    max_R = np.max(R)
    max_theta = theta[np.argmax(R)]
    x = np.linspace(17.6,19.6,1000)
    fig, ax = plt.subplots()
    mittelwert = np.mean(R)
    print(mittelwert)
    # Messdaten plotten (verbunden mit Linien und Punkten)
    ax.plot(theta, R, '-x', color='blue', markersize=1, label='Meswerte')
    ax.plot(x, f(x,mittelwert), '-', color='red', markersize=1, label='Mittelwert')
    ax.plot(2)
    # Diagramm gestalten
   
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel(r"$\text{Reflexionsintensität } R\, / \frac{\text{Imp}}{s}$", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(17.6, 19.6)
    ax.set_ylim(0, 40)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/zink.pdf")
zink()    


def zr():
    theta, R = np.genfromtxt("daten/zr.txt", unpack = True)
    # Maximum finden
    max_R = np.max(R)
    max_theta = theta[np.argmax(R)]
    x = np.linspace(8.8,10.8,1000)
    fig, ax = plt.subplots()
    mittelwert = np.mean(R)
    print(mittelwert)
    # Messdaten plotten (verbunden mit Linien und Punkten)
    ax.plot(theta, R, '-x', color='blue', markersize=1, label='Meswerte')
    ax.plot(x, f(x,mittelwert), '-', color='red', markersize=1, label='Mittelwert')
    ax.plot(2)
    # Diagramm gestalten
   
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel(r"$\text{Reflexionsintensität } R\, / \frac{\text{Imp}}{s}$", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(8.8, 10.8)
    ax.set_ylim(40, 80)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/zr.pdf")
zr()    


def brom():
    theta, R = np.genfromtxt("daten/brom.txt", unpack = True)
    # Maximum finden
    max_R = np.max(R)
    max_theta = theta[np.argmax(R)]
    x = np.linspace(12,14.2,1000)
    fig, ax = plt.subplots()
    mittelwert = np.mean(R)
    print(mittelwert)
    # Messdaten plotten (verbunden mit Linien und Punkten)
    ax.plot(theta, R, '-x', color='blue', markersize=1, label='Meswerte')
    ax.plot(x, f(x,mittelwert), '-', color='red', markersize=1, label='Mittelwert')
    ax.plot(2)
    # Diagramm gestalten
    
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    #ax.set_ylabel("\text{Reflexionsintensität R $\left| \frac{Imp}{s} \right|$}", fontsize=12)
    ax.set_ylabel(r"$\text{Reflexionsintensität } R\, / \frac{\text{Imp}}{s}$", fontsize=12)

    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(12, 14.2)
    ax.set_ylim(6, 18)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/brom.pdf")
brom()


def linreg():
    #Lineare Regression
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16

    # load data
    x, y = np.genfromtxt("daten/ryd.txt", unpack=True)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    ax.plot(x, y, "k.", label="example data")
    ax.set(xlabel=r"$t \,/\, \mathrm{s}$", ylabel=r"$s \,/\, \mathrm{m}$");

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.3f} ± {error:.3f}")
    x_plot = np.linspace(0, 38)
    fig, ax = plt.subplots(1, 1, layout="constrained")
    ax.plot(x, y, "k.", label="Messwerte")
    ax.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Lineare Regression",
        linewidth=1,
        color="tab:orange",
    )
    ax.set(xlim=(24, 38))
    ax.set(ylim=(97, 135))
    ax.grid(True)
    ax.legend()
    ax.set(xlabel=r"\text{$z_{eff}$}", ylabel=r"$\sqrt{E_K} / \sqrt{\unit{\eV}}$");
    fig.savefig("build/ryd.pdf") 
linreg()





# from scipy.stats import linregress
# # Deine experimentellen Daten (Beispieldaten – ersetze mit deinen Werten!)
# sigma_values = np.array([3.5, 3.26, 3.41, 4.26, 3.62])  # Beispiel-Abschirmkonstanten
# E_K_values = np.array([16.19, 10.46, 13.58, 9.74, 17.99])  # Beispiel-Kantenenergien [eV]
# Z = 29  # Kernladungszahl des Elements (z. B. Kupfer)

# # Berechne x und y
# z_eff = Z - sigma_values  # x = Z_eff
# y = np.sqrt(E_K_values)   # y = sqrt(E_K)

# # Lineare Regression
# slope, intercept, r_value, p_value, std_err = linregress(z_eff, y)

# # Plot
# plt.figure(figsize=(8, 6))
# plt.scatter(z_eff, y, color='red', label='Experimentelle Daten')
# plt.plot(z_eff, slope * z_eff + intercept, 'b-', label=f'Fit: y = {slope:.2f}x + {intercept:.2f}\n$R^2$ = {r_value**2:.3f}')

# # Beschriftungen
# plt.xlabel('$Z_\mathrm{eff} = Z - \sigma$', fontsize=12)
# plt.ylabel('$\sqrt{E_K}$ [$\sqrt{\mathrm{eV}}$]', fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.savefig("build/ryd.pdf")

# # Ausgabe der Fit-Parameter
# print(f"Steigung (m): {slope:.2f}")
# print(f"Achsenabschnitt (b): {intercept:.2f}")
# print(f"Bestimmtheitsmaß (R²): {r_value**2:.3f}")
# print(f"Standardfehler: {std_err:.2f}")