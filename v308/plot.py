import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
mu0 = 4*np.pi*(10)**(-7)
##Kleine Spule 
def kleineSpule():
    x,y = np.genfromtxt("Daten/mvsklein.txt" ,unpack=True)
    
    fig, ax = plt.subplots(1, 1, layout="constrained")

    x_plot = np.linspace(0, 0.6)
    
    ax.plot(x, y, "k.", label="Messwerte")
    ax.legend()
    ax.set(xlabel=r"$x(\unit{\centi\meter}$)", ylabel=r"$B(\unit{\milli\tesla})$");
    fig.savefig("build/plot1.pdf")

    ##mittelwert berechnen
    a,b = np.genfromtxt("Daten/mvsklein.txt" ,unpack=True, skip_header = 6, skip_footer = 5)
    #Mittelwert
    My = np.mean(b)
    #fehler Mittelwert
    FMy = sem(b)
    print("Magnetfeldstärke kleine Spule = (", My ,", ", FMy, ")")
    I = 1 #A
    n = 100
    l = 0.08

    print("Theoretischer Wert Magnetfeldstärke kleine Spule = ", (mu0*n*I)/(l))

kleineSpule()

#große Spule
def großeSpule():
    x,y = np.genfromtxt("Daten/mvsgroß.txt" ,unpack=True)
    
    fig, ax = plt.subplots(1, 1, layout="constrained")

    x_plot = np.linspace(0, 0.6)
    
    ax.plot(x, y, "k.", label="Messwerte")
    ax.legend()
    ax.set(xlabel=r"$x(\unit{\centi\meter}$)", ylabel=r"$B(\unit{\milli\tesla})$");
    fig.savefig("build/plot2.pdf")

    ##mittelwert berechnen
    a,b = np.genfromtxt("Daten/mvsgroß.txt" ,unpack=True, skip_header = 6, skip_footer = 5)
    #Mittelwert
    My = np.mean(b)
    #fehler Mittelwert
    FMy = sem(b)
    print("Magnetfeldstärke große Spule = (", My ,", ", FMy, ")")
    I = 1 #A
    n = 300
    l = 0.19

    print("Theoretischer Wert Magnetfeldstärke große Spule = ", (mu0*n*I)/(l))

großeSpule()


##Hysterese
def hysterese():
    x,y = np.genfromtxt("Daten/kurve.txt" ,unpack=True, skip_footer=18)
    I = x #Ampere
    r = 0.135 #meter
    n = 595 #Windungen 
    z = (n*x)/(2*np.pi*r)
    fig, ax = plt.subplots(1, 1, layout="constrained")
    x_plot = np.linspace(0, 0.6)
    ax.plot(z, y, "b.", label="Messwerte")

    x,y = np.genfromtxt("Daten/kurve.txt" ,unpack=True, skip_header=7, skip_footer=10)
    I = x #Ampere
    r = 0.135 #meter
    n = 595 #Windungen 
    z = (n*x)/(2*np.pi*r)
    #fig, ax = plt.subplots(1, 1, layout="constrained")
    x_plot = np.linspace(0, 0.6)
    ax.plot(z, y, "k.", label="Messwerte")

    x,y = np.genfromtxt("Daten/kurve.txt" ,unpack=True, skip_header=17, skip_footer=0)
    I = x #Ampere
    r = 0.135 #meter
    n = 595 #Windungen 
    z = (n*x)/(2*np.pi*r)
    #fig, ax = plt.subplots(1, 1, layout="constrained")
    x_plot = np.linspace(0, 0.6)
    ax.plot(z, y, "r.", label="Messwerte")
    
    ax.legend()
    ax.set(xlabel=r"$x(\unit{\centi\meter}$)", ylabel=r"$B(\unit{\milli\tesla})$");
    fig.savefig("build/plot3.pdf")

    ###mittelwert berechnen
    #a,b = np.genfromtxt("Daten/mvsgroß.txt" ,unpack=True, skip_header = 6, skip_footer = 5)
    ##Mittelwert
    #My = np.mean(b)
    ##fehler Mittelwert
    #FMy = sem(b)
    #print("Magnetfeldstärke große Spule = (", My ,", ", FMy, ")")
    #I = 1 #A
    #n = 300
    #l = 0.19

    #print("Theoretischer Wert Magnetfeldstärke große Spule = ", (mu0*n*I)/(l))

hysterese()

#########################################################################################
def spulenpaar():
    xw,yw = np.genfromtxt("Daten/hhgroßaI.txt" ,unpack=True)
    
    d = 190 # millimeter
    R = (125/2) # millimeter
    I = 1# Ampere
    n = 100#windungen
    yw = yw * (1)
    xw = xw*(10)
    xw = xw - (d/2) + (33/2)
    x_plot = np.linspace(0, 0.6)
    x = -50
    y = ((I*R**2)/2) *(1/(((x)**2+R**2)**(3/2))+1/((-(x)**2+R**2)**(3/2)))
    print(y)
    fig, ax = plt.subplots(1, 1, layout="constrained")

    x = np.linspace(-80, 180)
    ax.plot(x,  ((n*I*R**2)/2)*(1/(((x)**2+R**2)**(3/2))+1/(((-x)**2+R**2)**(3/2))), "k-", label="Theoriekurve")
    ax.plot(xw, yw, "r.", label="gemessene Magnetfeldstärke")
    ax.grid(True)
    ax.legend()
    ax.set(xlabel=r"$x(\unit{\milli\meter}$)", ylabel=r"$B(\unit{\milli\tesla})$");
    fig.savefig("build/plot4.pdf")




spulenpaar()

def spulenpaarkurz():
    xw,yw = np.genfromtxt("Daten/hhkleinaI.txt" ,unpack=True)
    
    d = 80 # millimeter
    R = (125/2) # millimeter
    I = 1# Ampere
    n = 100#windungen
    yw = yw * (1)
    xw = xw*(1)
    xw = xw - (d/2) + (33/2)
    x_plot = np.linspace(0, 0.6)
    
    fig, ax = plt.subplots(1, 1, layout="constrained")

    x = np.linspace(-80, 180)
    ax.plot(x,  ((n*I*R**2)/2)*(1/(((x)**2+R**2)**(3/2))+1/(((-x)**2+R**2)**(3/2))), "k-", label="Theoriekurve")
    ax.plot(xw, yw, "r.", label="gemessene Magnetfeldstärke")
    ax.grid(True)
    ax.legend()
    ax.set(xlabel=r"$x(\unit{\milli\meter}$)", ylabel=r"$B(\unit{\milli\tesla})$");
    fig.savefig("build/plot5.pdf")




spulenpaarkurz()