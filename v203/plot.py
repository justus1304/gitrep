import matplotlib.pyplot as plt
import numpy as np

def liniareRegression():
    #Liniare regression Runder Stab Einseitig
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    x , y = np.genfromtxt("Daten/hmesswerte.txt", unpack=True)
    #x aus differenz bilden(Aufgabenspezifisch)
    y0 = 967
    x = 1/x 
    y = np.log(y/y0)

    fig, ax = plt.subplots(1, 1, layout="constrained")

    params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
    errors = np.sqrt(np.diag(covariance_matrix))
    for name, value, error in zip("ab", params, errors):
        print(f"{name} = {value:.4f} ± {error:.4f}")

    #x-Achse anzeigebereich
    x_plot = np.linspace(0.01, 0.05)
    # ??
    fig, ax = plt.subplots(1, 1, layout="constrained")
    #label der Messwerte
    ax.plot(x, y, "kx", label="Messwerte",markersize=4,)
    ax.grid(True)
    #ploten der Ausgleichsgeraden
    ax.plot(
        x_plot,
        params[0] * x_plot + params[1],
        label="Lineare Regression",
        #Dicke der linie
        linewidth=1.5,
        #Farbe
        color="tab:red",
    )
    #Legende anzeigen lassen (labels)
    ax.legend()
    #Achsenbeschriftungen
    ax.set(xlabel=r"$\frac{1}{L} \unit{\per\celsius}$ ", ylabel=r"$\ln\left(\frac{L}{R}\right)$");
    fig.savefig("build/linreg.pdf")


liniareRegression()
