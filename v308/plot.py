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
    #ax.set(xlabel=r"$\Omega$", ylabel=r"$\frac{U_{Br}}{U_{s}}$");
    fig.savefig("build/plot.pdf")

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
