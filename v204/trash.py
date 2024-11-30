#Dynamische methode Edelstahl
def Edelstahl():
    plt.rcParams["figure.figsize"] = (6, 4)
    plt.rcParams["font.size"] = 16
    # daten aus txt laden
    t, T_8, T_7 = np.genfromtxt("Daten/Edelstahl.txt", unpack=True)
    T_8 = T_8 + 273
    T_7 = T_7 + 273
    
    T_8peaks, _ = find_peaks(T_8, height=0)
    T_8lows, _ = find_peaks(-T_8)

    T_7peaks, _ = find_peaks(T_7, height=0)
    T_7lows, _ = find_peaks(-T_7)
    
    #x-Achse anzeigebereich
    x_plot = np.linspace(0,1000)
    # ??
    fig, ax = plt.subplots(1, 1, layout="constrained")
    #ploten der Meswerte und Maxima/Minima
    ax.plot(t, T_8, "kx", label="Temperatur $T_8$",markersize=0.5,)
    ax.plot(t, T_7, "rx", label="Temperatur $T_7$",markersize=0.5,)
    ax.plot(t[T_8peaks], T_8[T_8peaks], "rx", label='Maxima')
    ax.plot(t[T_8lows], T_8[T_8lows], "kx", label='Minima')

    ax.plot(t[T_7peaks], T_7[T_7peaks], "rx")
    ax.plot(t[T_7lows], T_7[T_7lows], "kx")
    ax.grid(True)

    #phasendifferenz in (s)
    pd = t[T_8peaks] - t[T_7peaks]
    print ("T1T2 Delta t (s)= ", pd)
    Mwpd = ufloat(np.mean(pd), stats.sem(pd))
    print("Mwpd = ", np.mean(pd), " +- ", stats.sem(pd))
    
    #Amplituden in (K)
#########################berechnung Amplituden A_nah
    A_nah = [0]*10
    i = 0
    while(i<=9):
        A_nah[i] = 0.5 * (T_8[T_8peaks][i+1] - 0.5 * (T_8[T_8peaks][i+1] - T_8[T_8lows][i]) - T_8[T_8lows][i])
        i = i + 1
#########################
    A_nah = np.array(A_nah)
    print("A_nah = ", A_nah)
    
    
#########################berechnung Amplituden A_fern
    A_fern = [0]*10
    i = 0
    while(i<=9):
        A_fern[i] = 0.5 * (T_7[T_7peaks][i+1] - 0.5 * (T_7[T_7peaks][i+1] - T_7[T_7lows][i]) - T_7[T_7lows][i])
        i = i + 1
#########################
    A_fern = np.array(A_fern)
    print("A_fern = ", A_fern)

    print("")
    print("MwA_nah = ", np.mean(A_nah), " +- ", stats.sem(A_nah))
    print("MwA_fern = ", np.mean(A_fern), " +- ", stats.sem(A_fern))

    #ln(anteil)

    print("ln(A_nah / A_fern) ", np.log(A_nah/A_fern))

    Mwln = ufloat(np.mean(np.log(A_nah/A_fern)), stats.sem(np.log(A_nah/A_fern)))
    print("Mwln(A_nah/A_fern) = ", np.mean(np.log(A_nah/A_fern)), " +- ", stats.sem(np.log(A_nah/A_fern)))
    
    #berechnung der wärmeleitfähigkeit k
    k = (r_M * c_M * (dx)**2)/(2 * Mwpd * Mwln)
    print(k)
    ax.legend()
    #ax.set(xlabel=r"$t/\unit{\second}$ ", ylabel=r"$T/\unit{\kelvin}$");
    fig.savefig("build/EdelstahlPlot.pdf")
Edelstahl()

