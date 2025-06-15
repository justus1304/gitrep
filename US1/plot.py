import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e, e
from uncertainties import ufloat
from scipy.optimize import curve_fit

def acryl():
    x = np.linspace(0,0.00005,10000)
    print()
    print("Schallgeschwindigkeit Acryl")

    n,t_a,t_alu,h_a,h_alu = np.genfromtxt("daten/big.txt",unpack = True)
    t_a = t_a * 10**(-6)
    h_a = h_a * 0.01
    fig, ax =plt.subplots()
    ax.plot((1/2)*t_a,h_a,"k.",label = 'Messwerte')

    params,cov = np.polyfit((1/2)*t_a, h_a, 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
    print(f"Steigung: {m:.4f} ± {m_err:.4f}")
    print(f"Achsenabschnitt: {b:.4f} ± {b_err:.4f}")
    ax.plot(x,m * x + b, label = 'regresion')
    #ax.set(xlabel='$t/ \unit{\second}$',ylabel='$h/ \unit{\meter}$')
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    #ax.errorbar(U, N, yerr=np.sqrt(N), fmt='.', capsize=5, label='Messung')
    #ax.errorbar(U, N, xerr=0.2, fmt='.', capsize=5, label='Messung')
    fig.savefig("build/schallgeschwindigkeit_acryl.pdf")

acryl()

def acryl():
    x = np.linspace(0,0.00005,10000)

    print()
    print("Schallgeschwindigkeit Alu")
    n,t_a,t_alu,h_a,h_alu = np.genfromtxt("daten/big.txt",unpack = True)
    t_alu = t_alu * 10**(-6)
    h_alu = h_alu * 0.01
    fig, ax =plt.subplots()
    ax.plot((1/2)*t_alu,h_alu,"k.",label = 'Messwerte')

    params,cov = np.polyfit((1/2)*t_alu, h_alu, 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
    print(f"Steigung: {m:.4f} ± {m_err:.4f}")
    print(f"Achsenabschnitt: {b:.4f} ± {b_err:.4f}")
    ax.plot(x,m * x + b, label = 'regresion')
    #ax.set(xlabel='$t/ \unit{\second}$',ylabel='$h/ \unit{\meter}$')
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    #ax.errorbar(U, N, yerr=np.sqrt(N), fmt='.', capsize=5, label='Messung')
    #ax.errorbar(U, N, xerr=0.2, fmt='.', capsize=5, label='Messung')
    fig.savefig("build/schallgeschwindigkeit_alu.pdf")

acryl()


def acryl2():
    x = np.linspace(0,0.13,10000)

    print()
    print("Amplituden 2Mhz")
    n,in2,out2,in1,out1 = np.genfromtxt("daten/amplituden.txt",unpack = True)
    n,t_a,t_alu,h_a,h_alu = np.genfromtxt("daten/big.txt",unpack = True)
    h_alu = h_alu * 0.01
    h_a = h_a * 0.01
    fig, ax =plt.subplots()
    ax.plot(h_a,np.log(out2/in2),"k.",label = 'Messwerte')

    params,cov = np.polyfit(h_a, np.log(out2/in2), 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
    print(f"Steigung1: {m:.4f} ± {m_err:.4f}")
    print(f"Achsenabschnitt: {b:.4f} ± {b_err:.4f}")
    ax.plot(x,m * x + b, label = 'regresion')
    #ax.set(xlabel='$t/ \unit{\second}$',ylabel='$h/ \unit{\meter}$')
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    #ax.errorbar(U, N, yerr=np.sqrt(N), fmt='.', capsize=5, label='Messung')
    #ax.errorbar(U, N, xerr=0.2, fmt='.', capsize=5, label='Messung')
    fig.savefig("build/amplituden_alu2mhz.pdf")

acryl2()

def acryl2bearbeitet():
    x = np.linspace(0,0.13,10000)

    print()
    print("Amplituden 2Mhz ohne 1,2,9")
    n,in2,out2,in1,out1,h_a = np.genfromtxt("daten/amplituden_bearbeitet.txt",unpack = True)
    
    h_a = h_a * 0.01
    fig, ax =plt.subplots()
    ax.plot(h_a,np.log(out2/in2),"k.",label = 'Messwerte')

    params,cov = np.polyfit(h_a, np.log(out2/in2), 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
    print(f"Steigung1: {m:.4f} ± {m_err:.4f}")
    print(f"Achsenabschnitt: {b:.4f} ± {b_err:.4f}")
    ax.plot(x,m * x + b, label = 'regresion')
    #ax.set(xlabel='$t/ \unit{\second}$',ylabel='$h/ \unit{\meter}$')
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    #ax.errorbar(U, N, yerr=np.sqrt(N), fmt='.', capsize=5, label='Messung')
    #ax.errorbar(U, N, xerr=0.2, fmt='.', capsize=5, label='Messung')
    fig.savefig("build/amplituden_alu2mhzbearbeitet.pdf")

acryl2bearbeitet()


def acryl1():
    x = np.linspace(0,0.13,10000)
    print()
    print("Amplituden 1Mhz")
    n,in2,out2,in1,out1 = np.genfromtxt("daten/amplituden.txt",unpack = True)
    n,t_a,t_alu,h_a,h_alu = np.genfromtxt("daten/big.txt",unpack = True)
    h_alu = h_alu * 0.01
    h_a = h_a * 0.01
    fig, ax =plt.subplots()
    ax.plot(h_a,np.log(out1/in1),"k.",label = 'Messwerte')

    params,cov = np.polyfit(h_a, np.log(out1/in1), 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
    print(f"Steigung1: {m:.4f} ± {m_err:.4f}")
    print(f"Achsenabschnitt: {b:.4f} ± {b_err:.4f}")
    ax.plot(x,m * x + b, label = 'regresion')
    #ax.set(xlabel='$t/ \unit{\second}$',ylabel='$h/ \unit{\meter}$')
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    #ax.errorbar(U, N, yerr=np.sqrt(N), fmt='.', capsize=5, label='Messung')
    #ax.errorbar(U, N, xerr=0.2, fmt='.', capsize=5, label='Messung')
    fig.savefig("build/amplituden_alu1mhz.pdf")

acryl1()

def acryl1bearbeitet():
    print()
    print("Amplituden 1Mhz ohne 1,2,3,7")
    
    x = np.linspace(0,0.13,10000)

    n,in2,out2,in1,out1,h_a = np.genfromtxt("daten/amplituden_1mhzbearbeitet.txt",unpack = True)
    
    h_a = h_a * 0.01
    fig, ax =plt.subplots()
    ax.plot(h_a,np.log(out2/in2),"k.",label = 'Messwerte')

    params,cov = np.polyfit(h_a, np.log(out2/in2), 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
    print(f"Steigung1: {m:.4f} ± {m_err:.4f}")
    print(f"Achsenabschnitt: {b:.4f} ± {b_err:.4f}")
    ax.plot(x,m * x + b, label = 'regresion')
    #ax.set(xlabel='$t/ \unit{\second}$',ylabel='$h/ \unit{\meter}$')
    ax.legend()
    ax.grid(True)
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    #ax.errorbar(U, N, yerr=np.sqrt(N), fmt='.', capsize=5, label='Messung')
    #ax.errorbar(U, N, xerr=0.2, fmt='.', capsize=5, label='Messung')
    fig.savefig("build/amplituden_alu1mhzbearbeitet.pdf")

acryl1bearbeitet()

def f(x,a,b,c):
    return a * x**2+b*x+c

def fuellstand():
    V,t = np.genfromtxt("daten/wasser.txt",unpack = True)
    # Perform curve fitting
    popt, pcov = curve_fit(f, V, t,p0 = [-1,11,8])
    x = np.linspace(0,200,1000)
    # Plot the results
    fig, ax =plt.subplots()
    # Parameter ausgeben
    print("Optimale Parameter:")
    
    perr = np.sqrt(np.diag(pcov))
    print("\nStandardfehler der Parameter:")
    print("\nParameter mit Unsicherheiten:")
    print(f"a = {popt[0]:.3f} ± {perr[0]:.3f}")
    print(f"b = {popt[1]:.3f} ± {perr[1]:.3f}")
    print(f"c = {popt[2]:.3f} ± {perr[2]:.3f}")
    param_names = ['a', 'b', 'c']  # Anpassen an Ihre Funktion!
    print("\nZusammenfassung der Fit-Ergebnisse:")
    for name, value, error in zip(param_names, popt, perr):
        print(f"{name} = {value:.3f} ± {error:.3f}")
    ax.plot(V, t, 'bo', label='Messwerte')
    ax.plot(x, f(x, *popt), 'r-', label='Fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    ax.grid(True)
    ax.legend()
    fig.savefig("build/fuellstand.pdf")
fuellstand()