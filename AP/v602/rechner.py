import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import nominal_values as noms, std_devs as stds
import scipy.constants as const
import scipy.optimize
import sympy
import uncertainties as unc
from uncertainties import ufloat
from scipy.constants import h,c

def minl(t,d):
    return 2*d*10**(-3)*unp.sin(t)
def maxe(l):
    return (1.24/l )
def E(t,d):
    return maxe(minl(t*np.pi/180, d))
def f(x,R):
    return 0*x+R

def bog(g):
    return g*np.pi /180

def aufloesung():
    print(E(5.7, 201.4*10**(0)))
    
    mittela = E(ufloat(22.35,0.1), 201.4*10**(-3))
    mina = E(ufloat(22,0.1), 201.4*10**(-3))
    maxa = E(ufloat(22.7,0.1), 201.4*10**(-3))
    mittelb = E(ufloat(20.1,0.1), 201.4*10**(-3))
    minb = E(ufloat(19.8,0.1), 201.4*10**(-3))
    maxb = E(ufloat(20.4,0.1), 201.4*10**(-3))
    
    print("difa",mina-maxa)
    print("mittel a ",maxa)
    print("difb ",minb-maxb)
    print("mittel b ",mittelb)
    print("aufloese a =", mittela/(mina-maxa))
aufloesung()


def abschirm():

    # Gegebene Werte (Beispiel: Kupfer)
    Z = 29  # Ordnungszahl
    R_inf = 13.6  # Rydberg-Konstante in eV
    E_K_abs = 8987  # eV (K-Absorptionskante)
    E_K_alpha = ufloat(8100,40)  # eV (Kα-Linie, L → K)
    E_K_beta = ufloat(8950,40)   # eV (Kβ-Linie, M → K) - Beispielwert, ggf. anpassen!

    # Schritt 1: σ₁ aus K-Absorptionskante
    sigma_1 = Z - unp.sqrt(E_K_abs / R_inf)

    # Schritt 2: σ₂ aus Kα-Linie (n = 1, m = 2)
    n = 1
    m2 = 2
    term1_alpha = (1 / n**2) * (Z - sigma_1)**2
    term2_alpha = E_K_alpha / R_inf
    sigma_2 = Z - unp.sqrt((term1_alpha - term2_alpha) * m2**2)

    # Schritt 3: σ₃ aus Kβ-Linie (n = 1, m = 3)
    m3 = 3
    term1_beta = (1 / n**2) * (Z - sigma_1)**2
    term2_beta = E_K_beta / R_inf
    sigma_3 = Z - unp.sqrt((term1_beta - term2_beta) * m3**2)

    # Ergebnisse ausgeben
    print(f"Abschirmkonstante σ₁: {sigma_1:.2f}")
    print(f"Abschirmkonstante σ₂: {sigma_2:.2f}")
    print(f"Abschirmkonstante σ₃: {sigma_3:.2f}")
abschirm()  
print(np.sin((np.pi/180)*22.5))
print(c*(h/180))
print(6.6*10**(-27)*2.99*10**8/(2*201.4*10**(-3)*np.sin(5.7*np.pi/180)))

print(ufloat(8.1,0.04)/ufloat(0.26,0.07))
print(ufloat(8.95,0.04)/ufloat(0.26,0.07))