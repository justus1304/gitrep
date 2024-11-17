import matplotlib.pyplot as plt
import numpy as np

def lrRunder():
    #Liniare regression Runder Stab Einseitig
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    x,a,b = np.genfromtxt("Daten/rSeinseit.txt", unpack=True)
    #x aus differenz bilden(Aufgabenspezifisch)
    y = a - b
    x = x * 0.001
    y = y * 0.001
    print (x)
    print (y)
    

    x = (0.6*x**2 + (1/3) * x**3)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.4f} ± {error:.4f}")

    #x-Achse anzeigebereich
    x_plot = np.linspace(0.025, 0.2)
    # ??
    fig, ax = plt.subplots(1, 1, layout="constrained")
    #label der Messwerte
    ax.plot(x, y, "kx", label="Messwerte",markersize=10,)
    ax.grid(True)
    #ploten der Ausgleichsgeraden
    ax.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Lineare Regression",
        #Dicke der linie
        linewidth=1.5,
        #Farbe
        color="tab:blue",
    )
    #Legende anzeigen lassen (labels)
    ax.legend()
    #Achsenbeschriftungen
    ax.set(xlabel=r"$Lx^2-x^3/3 / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
    fig.savefig("build/plotrSeinseit.pdf")


lrRunder()


def lrEckiger():
    #Liniare regression Eckiger
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    x,a,b = np.genfromtxt("Daten/eSeinseit.txt", unpack=True)
    #x aus differenz bilden(Aufgabenspezifisch)
    y = a - b
    y = y * 0.001
    x = x * 0.001


    x = (0.6*x**2 + (1/3) * x**3)
    fig, a = plt.subplots(1, 1, layout="constrained")

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.4f} ± {error:.4f}")

    #x-Achse anzeigebereich
    x_plot = np.linspace(0.025, 0.2)
    # ??
    fig, ay = plt.subplots(1, 1, layout="constrained")
    #label der Messwerte
    ay.plot(x, y, "kx", label="Messwerte",markersize=10,)
    ay.grid(True)
    #ploten der Ausgleichsgeraden
    ay.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Lineare Regression",
        #Dicke der linie
        linewidth=1.5,
        #Farbe
        color="tab:blue",
    )
    #Legende anzeigen lassen (labels)
    ay.legend()
    #Achsenbeschriftungen
    ay.set(xlabel=r"$Lx^2-x^3/3 / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
    fig.savefig("build/ploteSeinseit.pdf")


lrEckiger()

    
    

def beidseitigLinks():
    
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    x,a,b = np.genfromtxt("Daten/runderStab.txt", unpack=True, max_rows = 10)
    x2,c,d = np.genfromtxt("Daten/eckigerStab.txt", unpack=True, max_rows = 10)
    #x aus differenz bilden(Aufgabenspezifisch)
    y = a - b
    y = y * 0.001
    x = x * 0.001
    #identisch
    y2 = c - d 
    y2 = y2 * 0.001
    x2 = x2 * 0.001

    x2 = (3*0.6**2*x - 4*x**3)
    x = (3*0.6**2*x - 4*x**3)
    fig, a = plt.subplots(1, 1, layout="constrained")

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.5f} ± {error:.5f}","Parameter Runder Stab beidseitig links")

    #x-Achse anzeigebereich
    x_plot = np.linspace(0.075, 0.225)
    # ??
    fig, ay = plt.subplots(1, 1, layout="constrained")
    #label der Messwerte
    ay.plot(x, y, "kx", label="Messwerte Runder Stab",markersize=10,)
    ay.plot(x, y2, "k.", label="Meswerte Eckiger Stab",markersize=10,)
    ay.grid(True)
    #ploten der Ausgleichsgeraden
    ay.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Regression Runder Stab",
        #Dicke der linie
        linewidth=1.5,
        #Farbe
        color="tab:blue",
    )
    params, covariance_matrix = np.polyfit(x, y2, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.5f} ± {error:.5f}", "parameter eckiger stab beidseitig links")
    ay.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Regression Eckiger Stab",
        #Dicke der linie
        linewidth=1.5,
        #Farbe
        color="tab:red",
    )
    #Legende anzeigen lassen (labels)
    
    ay.legend(fontsize = 10)
    #Achsenbeschriftungen
    ay.set(xlabel=r"$3L^2x-4x^3 / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");

    ##################################################################################################################################
    
    ##############################################################################################################################

    fig.savefig("build/beidseitigLinks.pdf")


beidseitigLinks()





def beidseitigRechts():
    
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    x,a,b = np.genfromtxt("Daten/runderStab.txt",skip_header = 11, unpack=True, max_rows = 10)
    x2,c,d = np.genfromtxt("Daten/eckigerStab.txt",skip_header = 11, unpack=True, max_rows = 10)
    #x aus differenz bilden(Aufgabenspezifisch)
    y = a - b
    y = y * 0.001
    x = x * 0.001
    #identisch
    y2 = c - d 
    y2 = y2 * 0.001
    x2 = x2 * 0.001

    
    x = (4*x**3-12*0.6*x**2+9*0.6**2*x-0.6**3)
    fig, a = plt.subplots(1, 1, layout="constrained")

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.5f} ± {error:.5f}","Parameter Runder Stab beidseitig rechts")

    #x-Achse anzeigebereich
    x_plot = np.linspace(0.075, 0.225)
    # ??
    fig, ay = plt.subplots(1, 1, layout="constrained")
    #label der Messwerte
    ay.plot(x, y, "kx", label="Messwerte Runder Stab",markersize=10,)
    ay.plot(x, y2, "k.", label="Meswerte Eckiger Stab",markersize=10,)
    ay.grid(True)
    #ploten der Ausgleichsgeraden
    ay.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Regression Runder Stab",
        #Dicke der linie
        linewidth=1.5,
        #Farbe
        color="tab:blue",
    )
    params, covariance_matrix = np.polyfit(x, y2, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.5f} ± {error:.5f}", "parameter eckiger stab beidseitig rechts")
    ay.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Regression Eckiger Stab",
        #Dicke der linie
        linewidth=1.5,
        #Farbe
        color="tab:red",
    )
    #Legende anzeigen lassen (labels)
    
    ay.legend(fontsize = 10)
    #Achsenbeschriftungen
    ay.set(xlabel=r"$(4x^3-12Lx^3+9L^2x-L^3) / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");

    ##################################################################################################################################
    
    ##############################################################################################################################

    fig.savefig("build/rechtsBeidseitig.pdf")

beidseitigRechts()





































































