# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import legendre  # Direktes SciPy-Legendre-Objekt


def legendre_l2_fit(alpha, A, B):
    """
    alpha: Drehwinkel in Radiant
    A: Skalierungsfaktor (Amplitude)
    B: Offset (für eventuelles Hintergrundrauschen im Labor)
    """
    # Geometrische Transformation in den echten Polarwinkel-Cosinus
    cos_theta = 0.5 * (np.cos(alpha) - 1)
    
    # Legendre-Polynom P_2(x) = 0.5 * (3x^2 - 1)
    p2 = 0.5 * (3 * cos_theta**2 - 1)
    
    # Da die Betragsamplitude gemessen wird:
    return np.abs(A * p2) + B

def legendre_l3_fit(alpha, A, B):
    """
    alpha: Drehwinkel in Radiant
    A: Skalierungsfaktor (Amplitude)
    B: Offset (Hintergrundrauschen)
    """
    # Geometrische Transformation in den echten Polarwinkel-Cosinus
    cos_theta = 0.5 * (np.cos(alpha) - 1)
    
    # Legendre-Polynom P_3(x) = 0.5 * (5 * x^3 - 3 * x)
    p3 = 0.5 * (5 * cos_theta**3 - 3 * cos_theta)
    
    # Da die Betragsamplitude gemessen wird:
    return np.abs(A * p3) + B

def legendre_l4_fit(alpha, A ,B):
    # Geometrische Transformation in den echten Polarwinkel-Cosinus
    cos_theta = 0.5 * (np.cos(alpha) - 1)

    # Legendre-Polynom P_4(x)
    #p4 = (1/8) * (35*cos_theta**4-30*cos_theta**2+3)
    p4 = 0.125 * (63 * cos_theta**5 - 70 * cos_theta**3 + 15 * cos_theta)
    return np.abs(A * p4) + B

def legendre_l10_fit(alpha, A ,B):
    # Geometrische Transformation in den echten Polarwinkel-Cosinus
    cos_phi = 0.5 * (np.cos(alpha) - 1)
    p11 = cos_phi
    
    return np.abs(A * p11) + B

    #return A * np.cos(1 * phi + phase) + B
def legendre_l11_fit(alpha, A, B):
    # Für Maxima bei 0/180 Grad und Minimum bei 90 Grad:
    p11 = np.cos(alpha)

    return np.abs(A * p11) + B
def werte_und_plotte_scipy_legendre(ordner_name, l_ordnung,fit,save,label1):
    winkel_grad = np.arange(0, 185, 5)
    p_daten = []
    alpha_winkel = []
    
    # Daten einlesen
    for w_grad in winkel_grad:
        datei_name = f"{w_grad}.dat"
        vollstaendiger_pfad = os.path.join('v23', 'Daten', ordner_name, datei_name)
        if not os.path.exists(vollstaendiger_pfad):
            vollstaendiger_pfad = os.path.join('Daten', ordner_name, datei_name)
        if not os.path.exists(vollstaendiger_pfad):
            vollstaendiger_pfad = os.path.join(ordner_name, datei_name)

        if os.path.exists(vollstaendiger_pfad):
            try:
                daten = np.loadtxt(vollstaendiger_pfad)
                max_amplitude = np.max(daten[:, 1])
                p_daten.append(max_amplitude)
                alpha_winkel.append(np.deg2rad(w_grad))
            except Exception:
                continue

    alpha_winkel = np.array(alpha_winkel)
    p_daten = np.array(p_daten)

    if len(p_daten) == 0:
        print(f"[-] Keine Daten im Ordner '{ordner_name}' gefunden.")
        return

    
    theta = alpha_winkel
    r = p_daten

    popt, pcov = curve_fit(fit, alpha_winkel, p_daten, p0=[1.0, 0.1])
    A_opt, B_opt = popt

    print(f"Optimale Parameter: Amplitude A = {A_opt:.3f}, Offset B = {B_opt:.3f}")

    #Ploten
    alpha_fit = np.linspace(0, np.pi*2, 500)
    amplitude_fit = fit(alpha_fit, A_opt, B_opt)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Messpunkte
    ax.scatter(alpha_winkel, p_daten, color='blue', s=25, label='Messpunkte', zorder=3)

    # Fit ploten
    ax.plot(alpha_fit, amplitude_fit, color='red', linewidth=2, label= label1, zorder=2)

    ax.set_xlim(0, np.pi*2) # Zeigt den gemessenen Bereich von 0° bis 180°
    ax.legend(loc='upper right')
    #plt.show()
    fig.savefig(save)
werte_und_plotte_scipy_legendre("Daten/peak2.3", 2,legendre_l10_fit,"build/legendre_11_fit.png",r'$Y_1^0(\alpha)$ Fit')
werte_und_plotte_scipy_legendre("Daten/peak3.7", 2,legendre_l2_fit,"build/legendre_12_fit.png",r'$Y_2^0(\alpha)$ Fit')
werte_und_plotte_scipy_legendre("Daten/peak5.0", 2,legendre_l3_fit,"build/legendre_13_fit.png",r'$Y_3^0(\alpha)$ Fit')
werte_und_plotte_scipy_legendre("Daten/peak7.4", 2,legendre_l4_fit,"build/legendre_14_fit.png",r'$Y_5^0(\alpha)$ Fit')

def werte_und_plotte_scipy_legendre_azimutal(ordner_name, l_ordnung,fit,save,nummer_peak, label1):
    winkel_grad = np.arange(0, 185, 5)
    p_daten = []
    alpha_winkel = []
    
    # Daten einlesen
    for w_grad in winkel_grad:
        datei_name = f"{w_grad}.dat"
        vollstaendiger_pfad = os.path.join('v23', 'Daten', ordner_name, datei_name)
        if not os.path.exists(vollstaendiger_pfad):
            vollstaendiger_pfad = os.path.join('Daten', ordner_name, datei_name)
        if not os.path.exists(vollstaendiger_pfad):
            vollstaendiger_pfad = os.path.join(ordner_name, datei_name)

        if os.path.exists(vollstaendiger_pfad):
            try:
                daten = np.loadtxt(vollstaendiger_pfad)
                if(nummer_peak == 1):
                    max_amplitude = np.max(daten[:len(daten)//2, 1])
                else:
                    max_amplitude = np.max(daten[len(daten)//2:, 1])

                p_daten.append(max_amplitude)
                alpha_winkel.append(np.deg2rad(w_grad))
            except Exception:
                continue

    alpha_winkel = np.array(alpha_winkel)
    p_daten = np.array(p_daten)

    if len(p_daten) == 0:
        print(f"[-] Keine Daten im Ordner '{ordner_name}' gefunden.")
        return

    
    theta = alpha_winkel
    r = p_daten

    popt, pcov = curve_fit(fit, alpha_winkel, p_daten, p0=[1.0, 0.1])
    A_opt, B_opt = popt

    print(f"Optimale Parameter: Amplitude A = {A_opt:.3f}, Offset B = {B_opt:.3f}")

    #Ploten
    alpha_fit = np.linspace(0, np.pi*2, 500)
    amplitude_fit = fit(alpha_fit, A_opt, B_opt)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Messpunkte
    ax.scatter(alpha_winkel, p_daten, color='blue', s=25, label='Messpunkte', zorder=3)

    # Fit ploten
    ax.plot(alpha_fit, amplitude_fit, color='red', linewidth=2, label= label1, zorder=2)

    
    ax.set_xlim(0, np.pi*2) # Zeigt den gemessenen Bereich von 0° bis 180°
    ax.legend(loc='upper right')
    plt.show()
    plt.savefig(save)

werte_und_plotte_scipy_legendre_azimutal( "Daten/ring peak 2.3" , 1,legendre_l11_fit,"build/aufspaltung_l1_m1.png",2, r'$Y_1^1(\alpha)$ Fit')
werte_und_plotte_scipy_legendre_azimutal( "Daten/ring peak 2.3" , 1,legendre_l10_fit,"build/aufspaltung_l1_m0.png",1, r'$Y_1^0(\alpha)$ Fit')

## daten ploten

# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt

def plotte_einzelnes_spektrum(einlese_pfad, speicher_pfad):
    """
    Liest ein einzelnes Frequenzspektrum aus einer .dat-Datei,
    plottet es (Frequenz vs. Amplitude) und speichert die Grafik ab.
    
    Parameters:
    einlese_pfad (str): Pfad zur .dat-Datei (z.B. 'v23/Daten/peak2.3/0.dat')
    speicher_pfad (str): Zielpfad für das PDF (z.B. 'build/spektrum_0.pdf')
    """
    # 1. Überprüfen, ob die Datei überhaupt existiert
    if not os.path.exists(einlese_pfad):
        print(f"[-] Datei nicht gefunden: {einlese_pfad}")
        return

    try:
        # 2. Daten laden (Spalte 0 = Frequenz, Spalte 1 = Amplitude)
        daten = np.loadtxt(einlese_pfad)
        frequenz = daten[:, 0]
        amplitude = daten[:, 1]
    except Exception as e:
        print(f"[-] Fehler beim Laden von {einlese_pfad}: {e}")
        return

    # Old-Plots im Hintergrund schließen, um Speicherfehler zu vermeiden
    plt.close('all')
    
    # 3. Das Diagramm erstellen
    fig, ax = plt.subplots(figsize=(8, 4.5))
    
    # Spektrum als Linie plotten
    ax.plot(frequenz, amplitude, color='#2b6cb0', linewidth=1.5, label='Messwerte')
    
    # Achsenbeschriftungen (gemäß deiner Anleitung: 1V entspricht 1kHz)
    ax.set_xlabel('Frequenz $f$ / Hz', fontsize=11)
    ax.set_ylabel('Druckamplitude $p$ ', fontsize=11)
    
    # Titel generieren (nutzt den reinen Dateinamen zur Beschriftung)
    dateiname_rein = os.path.basename(einlese_pfad)
    #ax.set_title(f"Frequenzspektrum ({dateiname_rein})", weight='bold', fontsize=12, pad=12)
    
    # Gitternetz und Legende
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    
    # 4. Ordnerstruktur für das Ziel sichern (falls 'build/' noch nicht existiert)
    ziel_ordner = os.path.dirname(speicher_pfad)
    if ziel_ordner and not os.path.exists(ziel_ordner):
        os.makedirs(ziel_ordner)
        
    # 5. Speichern und Schließen
    plt.savefig(speicher_pfad, bbox_inches='tight', dpi=300)
    print(f"[+] Plot erfolgreich gespeichert unter: {speicher_pfad}")
    plt.close(fig)


plotte_einzelnes_spektrum("Daten/2vor1.dat", "build/2vor1.pdf")
plotte_einzelnes_spektrum("Daten/2vor6.dat", "build/2vor6.pdf")
plotte_einzelnes_spektrum("Daten/2vor12.dat", "build/2vor12.pdf")
plotte_einzelnes_spektrum("Daten/vor1.dat", "build/vor1.pdf")
plotte_einzelnes_spektrum("Daten/vor4.dat", "build/vor4.pdf")
plotte_einzelnes_spektrum("Daten/vor8.dat", "build/vor8.pdf")

plotte_einzelnes_spektrum("Daten/uerbersicht.dat", "build/spektrum.pdf")

