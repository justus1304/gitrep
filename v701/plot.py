import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e, e
from uncertainties import ufloat
from scipy.stats import poisson, norm
#Energie berechnen
def energie(channel,druck):
    E_max = 4
    channel_max = 1159
    channel_dif = channel / channel_max 
    E = E_max * channel_dif
    return E

def eff_length(x_0, p):
    p_0 = 1.01
    x = x_0 * (p / p_0)
    return x

def f(m,x,b):
    return m * x + b

def mittelwert(a):
    x = 0
    for i in range(len(a-1)):
        x = x + a[i]
    
    return x / len(a)
def standartabweichung(a):
    mw = mittelwert(a)
    a = a-mw 
    a = a**2
    x = 0
    for i in range(len(a-1)):
        x = x + a[i]
    return np.sqrt(x / len(a))


def abstand_4():
    print("Abstand: 4cm")
    x = np.linspace(0.00,0.036,10000)
    x_0 = 0.04 #m
#Daten Einlesen
    p,n,c = np.genfromtxt("daten/x0ist4.txt",unpack = True)
#Einheiten umrechnen mbar in bar 
    p = p*10**(-3)

    fig, ax =plt.subplots()
#plotten der Messwerte
    ax.plot(eff_length(x_0,p),energie(c,p),"k.",label = 'Energien')
#liniare ausgleichhsrechnung
    params,cov = np.polyfit(eff_length(x_0,p),energie(c,p), 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))
#wert und Fehler ausgeben 
    print(f"Steigung: {m:.7f} ± {m_err:.7f}")
    print(f"Achsenabschnitt: {b:.7f} ± {b_err:.7f}")
    print(-ufloat(b,b_err)/ufloat(m,m_err))
#Ausgleichsrechnung ploten 
    ax.plot(x,m * x + b,label = 'regression')
    
    ax.set_xlabel(r"Effektive Weglänge $ /\unit{\meter}$")
    ax.set_ylabel(r"Energie$/\unit{\mega\electronvolt}$")
    ax.legend()
    ax.grid(True)
#Senkrechte linie falls benoetigt
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/abstand4.pdf")
#Ausfuehren der funktion
abstand_4()


def abstand_7():
    print("Abstand: 7cm")
    x = np.linspace(0.00,0.036,10000)
    x_0 = 0.07 #m

    p,n,c = np.genfromtxt("daten/x0ist7.txt",unpack = True)
    p = p*10**(-3)

    fig, ax =plt.subplots()

    ax.plot(eff_length(x_0,p),energie(c,p),"k.",label = 'Energien')

    params,cov = np.polyfit(eff_length(x_0,p),energie(c,p), 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))

    print(f"Steigung: {m:.7f} ± {m_err:.7f}")
    print(f"Achsenabschnitt: {b:.7f} ± {b_err:.7f}")
    print(-ufloat(b,b_err)/ufloat(m,m_err))

    ax.plot(x,m * x + b,label = 'regrssion')
    
    ax.set_xlabel(r"Effektive Weglänge $ /\unit{\meter}$")
    ax.set_ylabel(r"Energie$/\unit{\mega\electronvolt}$")
    ax.legend()
    ax.grid(True)
#Senkrechte linie falls benoetigt
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/abstand7.pdf")
#Ausfuehren der funktion
abstand_7()



def anzahl_4():
    print("Anzahl, Abstand: 4cm ")
    x = np.linspace(0.045,0.064,10000)
    x_0 = 0.07 #m

    p,n,c = np.genfromtxt("daten/x0ist4.txt",unpack = True)
    p = p*10**(-3)

    fig, ax =plt.subplots()

    ax.plot(eff_length(x_0,p),n,"k.",label = 'Pulszahl')

    params,cov = np.polyfit(eff_length(x_0,p)[14:],n[14:], 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))

    print(f"Steigung: {m:.7f} ± {m_err:.7f}")
    print(f"Achsenabschnitt: {b:.7f} ± {b_err:.7f}")
    print(-ufloat(b,b_err)/ufloat(m,m_err))
#ploten der ausgleichsgerade 
    ax.plot(x,m * x + b, label = 'regression')
#ploten auf halber maximaler hoehe
    ax.plot(x,f(0,x,np.max(n)/2),label = 'Halbe maximale pulszahl')
    
    sp = (np.max(n)/2-ufloat(b,b_err)) / ufloat(m,m_err)
    print("schnittpunkt : " ,sp,np.max(n)/2)
#ploten des Schnittpunktes
    ax.plot(sp.nominal_value,f(m,sp.nominal_value,b),'rx',label = 'Schnittpunkt')
    ax.set_xlabel(r"Effektive Weglänge $ /\unit{\meter}$")
    ax.set_ylabel(r"Impulse pro 120s")
    ax.legend()
    ax.grid(True)
#Senkrechte linie falls benoetigt
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/anzahl4.pdf")
#Ausfuehren der funktion
anzahl_4()

def anzahl_7():
    print("Anzahl, Abstand: 7cm ")
    x = np.linspace(0.020,0.036,10000)
    x_0 = 0.07 #m

    p,n,c = np.genfromtxt("daten/x0ist7.txt",unpack = True)
    p = p*10**(-3)

    fig, ax =plt.subplots()

    ax.plot(eff_length(x_0,p),n,"k.",label = 'Pulszahl')

    params,cov = np.polyfit(eff_length(x_0,p)[6:],n[6:], 1,cov=True) 
    m, b = params 
    m_err, b_err = np.sqrt(np.diag(cov))

    print(f"Steigung: {m:.7f} ± {m_err:.7f}")
    print(f"Achsenabschnitt: {b:.7f} ± {b_err:.7f}")
    print(-ufloat(b,b_err)/ufloat(m,m_err))
#ploten der ausgleichsgerade 
    ax.plot(x,m * x + b, label = 'regression')
#ploten auf halber maximaler hoehe
    ax.plot(x,f(0,x,np.max(n)/2),label = 'Halbe maximale pulszahl')
    sp = (np.max(n)/2-ufloat(b,b_err)) / ufloat(m,m_err) 
    print("schnittpunkt : " ,sp,np.max(n)/2)
#ploten des Schnittpunktes
    ax.plot(sp.nominal_value,f(m,sp.nominal_value,b),'rx',label = 'Schnittpunkt')
    ax.set_xlabel(r"Effektive Weglänge $ /\unit{\meter}$")
    ax.set_ylabel(r"Impulse pro 200s")
    ax.legend()
    ax.grid(True)
#Senkrechte linie falls benoetigt
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/anzahl7.pdf")
#Ausfuehren der funktion
anzahl_7()

def histogramm_1():
    # Beispiel-Daten erzeugen

    daten = np.genfromtxt("daten/100mw.txt")
    daten2 = daten + np.sqrt(daten)
    daten3 = daten - np.sqrt(daten)
    fig, ax =plt.subplots()
    # Histogramm zeichnen
    ax.hist(daten, bins=10, facecolor='none',histtype='step', edgecolor='black', linewidth=1.7,label='Messwerte')
    ax.hist(daten2, bins=10, facecolor='none',histtype='step', edgecolor='red', linewidth=1.7, linestyle = '--',label = 'Messwerte + $\sqrt{N}$')
    ax.hist(daten3, bins=10, facecolor='none',histtype='step', edgecolor='yellow', linewidth=1.7, linestyle = '--',label = 'Messwerte - $\sqrt{N}$')
    x = np.linspace(1700,2000,1000)
    y = norm.pdf(x,mittelwert(daten),standartabweichung(daten))
    
    gauss = np.random.normal(loc=mittelwert(daten), scale=standartabweichung(daten), size=len(daten))
    poisson = np.random.poisson(lam=mittelwert(daten), size=len(daten))
    ax.hist(gauss, bins=10, facecolor='none',histtype='step', edgecolor='blue', linewidth=1.7, linestyle = '-',label = 'Gauß')
    ax.hist(poisson, bins=10, facecolor='none',histtype='step', edgecolor='red', linewidth=1.7, linestyle = '-',label = 'Poisson')
    
    #ax.hist(daten2, bins=10, edgecolor='blue')
    print("mittelwert = ", ufloat(mittelwert(daten),standartabweichung(daten)/np.sqrt(len(daten))))
    print("varianz = ", standartabweichung(daten))
    # Achsenbeschriftungen und Titel
    ax.set_xlabel('Anzahl')
    
   
    # Anzeigen
    ax.legend()
    ax.grid(True)
#Senkrechte linie falls benoetigt
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/histogram_1.pdf")
histogramm_1()


def histogramm_2():
    # Beispiel-Daten erzeugen

    daten = np.genfromtxt("daten/100mw.txt")
    daten2 = daten + np.sqrt(daten)
    daten3 = daten - np.sqrt(daten)
    fig, ax =plt.subplots()
    # Histogramm zeichnen
    ax.hist(daten, bins=5, facecolor='none',histtype='step', edgecolor='black', linewidth=1.7,label='Messwerte')
    ax.hist(daten2, bins=5, facecolor='none',histtype='step', edgecolor='red', linewidth=1.7, linestyle = '--',label = 'Messwerte + $\sqrt{N}$')
    ax.hist(daten3, bins=5, facecolor='none',histtype='step', edgecolor='yellow', linewidth=1.7, linestyle = '--',label = 'Messwerte - $\sqrt{N}$')
    x = np.linspace(1700,2000,1000)
    y = norm.pdf(x,mittelwert(daten),standartabweichung(daten))
    
    gauss = np.random.normal(loc=mittelwert(daten), scale=standartabweichung(daten), size=len(daten))
    poisson = np.random.poisson(lam=mittelwert(daten), size=len(daten))
    ax.hist(gauss, bins=5, facecolor='none',histtype='step', edgecolor='blue', linewidth=1.7, linestyle = '-',label = 'Gauß')
    ax.hist(poisson, bins=5, facecolor='none',histtype='step', edgecolor='red', linewidth=1.7, linestyle = '-',label = 'Poisson')
    
    #ax.hist(daten2, bins=10, edgecolor='blue')
    print("mittelwert = ", ufloat(mittelwert(daten),standartabweichung(daten)/np.sqrt(len(daten))))
    print("varianz = ", standartabweichung(daten))
    # Achsenbeschriftungen und Titel
    ax.set_xlabel('Anzahl')
    
   
    # Anzeigen
    ax.legend()
    ax.grid(True)
#Senkrechte linie falls benoetigt
    #ax.axvline(x = 560,color = 'red', linestyle='--')
    fig.savefig("build/histogram_2.pdf")
histogramm_2()