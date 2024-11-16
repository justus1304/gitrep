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
        print(f"{name} = {value:.3f} ± {error:.3f}")

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
    ax.set(xlabel=r"$x / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
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
        print(f"{name} = {value:.3f} ± {error:.3f}")

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
    ay.set(xlabel=r"$x / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
    fig.savefig("build/ploteSeinseit.pdf")


lrEckiger()

    
    

def beidseitigLinks():
    
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    x,a,b = np.genfromtxt("Daten/runderStab.txt", unpack=True, max_rows = 10)
    #x aus differenz bilden(Aufgabenspezifisch)
    y = a - b
    y = y * 0.001
    x = x * 0.001


    x = (3*0.6**2*x - 4*x**3)
    fig, a = plt.subplots(1, 1, layout="constrained")

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.3f} ± {error:.3f}")

    #x-Achse anzeigebereich
    x_plot = np.linspace(0.075, 0.275)
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
    ay.set(xlabel=r"$x / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
    fig.savefig("build/beidseitigLinks.pdf")



beidseitigLinks()


def beidseitigRechts():
    
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    x,a,b = np.genfromtxt("Daten/runderStab.txt", unpack=True, max_rows = 10,skip_header=11)
    #x aus differenz bilden(Aufgabenspezifisch)
    y = a - b
    y = y * 0.001
    x = x * 0.001


    x = (4*x**3-12*0.6*x**2+9*0.6**2*x-0.6**3)
    fig, a = plt.subplots(1, 1, layout="constrained")

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.3f} ± {error:.3f}")

    #x-Achse anzeigebereich
    x_plot = np.linspace(0.075, 0.275)
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
    ay.set(xlabel=r"$x / \unit{\milli\meter}$", ylabel=r"$\symbf{D} / \unit{\milli\meter}$");
    fig.savefig("build/beidseitigLinks.pdf")



beidseitigRechts()









































































