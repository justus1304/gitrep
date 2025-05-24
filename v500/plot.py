import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e, e
from uncertainties import ufloat



def violettUI():
    x = np.linspace(-2,20,10000)
#Daten Einlesen
    U1,I_max = np.genfromtxt("Daten/teil1voll.txt",unpack = True)
    U2,I_min = np.genfromtxt("Daten/teil1halb.txt",unpack = True)
#Einheiten umrechnen
    I_max = I_max * 10**(-6)
    I_min = I_min * 10**(-6)
    fig, ax =plt.subplots()
#plotten der Messwerte
    ax.plot(U1,I_max,"k.",label = 'Violett(Voll)')
    ax.plot(U2,I_min,"k.",label = 'Violett(Halb)')
    ax.set_xlabel(r"$U/\unit{\volt}$")
    ax.set_ylabel(r"$I/\unit{\milli\ampere}$")
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/violettUI.pdf")
#Ausfuehren der funktion
violettUI()

def violettUsqrtI():
    print("Violett")
    x = np.linspace(-1.2,0.5,10000)
#Daten Einlesen
    U1,I_max = np.genfromtxt("Daten/teil1voll.txt",unpack = True)
#Einheiten umrechnen
    I_max = np.sqrt(I_max * 10**(-6))
    fig, ax =plt.subplots()
#plotten der Messwerte
    ax.plot(U1[:-6],I_max[:-6],"k.",label = 'Violett(Voll)')
#liniare ausgleichhsrechnung
    params,cov = np.polyfit(U1[:-6],I_max[:-6], 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
#wert und Fehler ausgeben 
    print(f"Steigung: {m:.7f} ± {m_err:.7f}")
    print(f"Achsenabschnitt: {b:.7f} ± {b_err:.7f}")
    print(-ufloat(b,b_err)/ufloat(m,m_err))
#Ausgleichsrechnung ploten 
    ax.plot(x,m * x + b)
    
    ax.set_xlabel(r"$U/\unit{\volt}$")
    ax.set_ylabel(r"$\sqrt{I}/\unit{\milli\ampere}$")
    ax.legend()
    ax.grid(True)
#Senkrechte linie falls benoetigt
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/violettUsqrtI.pdf")
#Ausfuehren der funktion
violettUsqrtI()

def gelb():
    print("gelb")
#Daten Einlesen
    U1,I_max = np.genfromtxt("Daten/gelb.txt",unpack = True)
    x = np.linspace(U1[0],U1[len(U1)-1],10000)
#Einheiten umrechnen
    I_max = np.sqrt(I_max * 10**(-6))
    fig, ax =plt.subplots()
#plotten der Messwerte
    ax.plot(U1,I_max,"k.",label = 'Messwerte Gelb')
#liniare ausgleichsrechnung
    params,cov = np.polyfit(U1,I_max, 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
#wert und Fehler ausgeben 
    print(f"Steigung: {m:.7f} ± {m_err:.7f}")
    print(f"Achsenabschnitt: {b:.7f} ± {b_err:.7f}")
    print(-ufloat(b,b_err)/ufloat(m,m_err))
#Ausgleichsrechnung ploten 
    ax.plot(x,m * x + b)
    
    ax.set_xlabel(r"$U/\unit{\volt}$")
    ax.set_ylabel(r"$\sqrt{I}/\unit{\milli\ampere}$")
    ax.legend()
    ax.grid(True)
#Senkrechte linie falls benoetigt
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/gelb.pdf")
#Ausfuehren der funktion
gelb()

def gruen():
    print("gruen")
    U1,I_max = np.genfromtxt("Daten/gruen.txt",unpack = True)
    x = np.linspace(U1[0],U1[len(U1)-1],10000)

    I_max = np.sqrt(I_max * 10**(-6))
    fig, ax =plt.subplots()
    ax.plot(U1,I_max,"k.",label = 'Messwerte gruen')
    params,cov = np.polyfit(U1,I_max, 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
    print(f"Steigung: {m:.7f} ± {m_err:.7f}")
    print(f"Achsenabschnitt: {b:.7f} ± {b_err:.7f}")
    print(-ufloat(b,b_err)/ufloat(m,m_err))
    ax.plot(x,m * x + b)
    ax.set_xlabel(r"$U/\unit{\volt}$")
    ax.set_ylabel(r"$\sqrt{I}/\unit{\milli\ampere}$")
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/gruen.pdf")
#Ausfuehren der funktionb
gruen()

def tuerkies():
    print("tuerkies")
    U1,I_max = np.genfromtxt("Daten/tuerkies.txt",unpack = True)
    x = np.linspace(U1[0],U1[len(U1)-1],10000)

    I_max = np.sqrt(I_max * 10**(-6))
    fig, ax =plt.subplots()
    ax.plot(U1,I_max,"k.",label = 'Messwerte tuerkies')
    params,cov = np.polyfit(U1,I_max, 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
    print(f"Steigung: {m:.7f} ± {m_err:.7f}")
    print(f"Achsenabschnitt: {b:.7f} ± {b_err:.7f}")
    print(-ufloat(b,b_err)/ufloat(m,m_err))
    ax.plot(x,m * x + b)
    ax.set_xlabel(r"$U/\unit{\volt}$")
    ax.set_ylabel(r"$\sqrt{I}/\unit{\milli\ampere}$")
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/tuerkies.pdf")
#Ausfuehren der funktionb
tuerkies()