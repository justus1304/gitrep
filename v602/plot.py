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
    ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
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
    ax.plot(theta[158:][:-95], R[158:][:-95], '-', color='red', markersize=1, label="$K_a - Lienie$")
    ax.plot(theta[180:][:-70], R[180:][:-70], '-', color='yellow', markersize=1, label="$K_b - Lienie$")
    
    # Diagramm gestalten
    
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
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
    ax.plot(x, f(x,max_R2/2), '-', color='yellow', markersize=5, label='Höhe 2. halbwertsbrite')

    # Diagramm gestalten
   
    ax.set_xlabel("Winkel θ [°]", fontsize=12)
    ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
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
    ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(10.0, 12.0)
    ax.set_ylim(0, 140)

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
    ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(16.3, 18.3)
    ax.set_ylim(0, 40)

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
    ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
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
    ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(8.8, 10.8)
    ax.set_ylim(0, 100)

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
    ax.set_ylabel("Reflexionsintensität R [a.u.]", fontsize=12)
    print("Theta min/max:", np.min(theta), np.max(theta))
    print("R min/max:", np.min(R), np.max(R))
    ax.set_xlim(12, 14.2)
    ax.set_ylim(0, 40)

    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.savefig("build/brom.pdf")
brom()    