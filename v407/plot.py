#from uncertainties import ufloat
#import numpy as np
#import uncertainties.unumpy as unp
#from scipy.stats import sem
#import matplotlib.pyplot as plt
#import scipy.optimize
#from scipy.constants import c,h, m_e
#import math
#a_p,I_p = np.genfromtxt("Daten/parallel.txt",unpack = True)
#a_s,I_s = np.genfromtxt("Daten/senkrecht.txt",unpack = True)
#fehler = ufloat(1,0.002)
##umrechnen in rad
#a_p = a_p/57.2958 
#a_s = a_s/57.2958 
##faktor auf messanzeige berücksichtigen 
#I_p = I_p/3 
#I_s = I_s/3 
#I_e = 0.203
#
#
#def n_p(a,E):
#    return np.sqrt(E/(2*np.cos(a)**2)+(E**2/(4*np.cos(a)**4)-E*np.tan(a)**2)**(1/2))
#def n_s(a,E):
#    return np.sqrt(1+4*E*np.cos(a)**2/((E-1)**2))
#    #return np.sqrt((E**2-2*E*np.cos(2*a)+1)/(E** -2*E+1))
#MW_p = 0
#for i in range(len(I_p)):
#    MW_p = MW_p + (n_p(a_p[i],((I_p[i] + 1)/(I_p[i] - 1))**2))
#    print(n_p(a_p[i],((I_p[i] + 1)/(I_p[i] - 1))**2))
#print('MW_p = ',MW_p/len(I_p))
#print()
#print()
#MW_s = 0
#for i in range(len(I_s)):
#    MW_s = MW_s + n_s(a_s[i],(I_s[i]))
#    print(n_s(a_s[i],(I_s[i])))
#print('MW_s = ',MW_s/len(I_s))
#print(sem(n_p(a_p,I_p)))
#
#def f(a,n_s):
#    return ((np.sqrt(n_s**2-np.sin(a)**2)-np.cos(a))**2/(n_s**2-1))
#def g(a,n_p):
#    return abs(((n_p**2*np.cos(a)-(n_p**2-np.sin(a)**2)**(1/2))/(n_p**2*np.cos(a)+np.sqrt(n_p**2-np.sin(a)**2))))
#fig, ax =plt.subplots()
#
#ax.plot(a_p,np.sqrt(I_p/I_e),"rx",label = "Parallele Polarisation")
#ax.plot(a_s,np.sqrt(I_s/I_e),"kx",label = 'Senkrechte polarisation')
#a = np.linspace(0,1.55,1000)
#ax.plot(a, f(a,1.04))
#ax.plot(a, g(a,2.597))
#ax.legend()
#ax.grid(True)
##ax.set_xscale("log")
#fig.savefig("plot.pdf")
#
##Brewster Winkel in Grad Celsius
#theta_browster = 57.2958 *np.arctan( 2.497/1)
#print('Brewster Winkel = ' , theta_browster)



import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import nominal_values as noms, std_devs as stds
import scipy.constants as const
import scipy.optimize
import sympy
import uncertainties as unc


def linregress(x, y):
    N = len(
        y
    )  # Annahme: len(x) == len(y), sonst kommt während der Rechnung eine Fehlermeldung
    Delta = N * np.sum(x**2) - (np.sum(x)) ** 2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

    sigma_y = np.sqrt(np.sum((y - A * x - B) ** 2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)

    return A, A_error, B, B_error


def ulinregress(x, y):
    A, A_error, B, B_error = linregress(unp.nominal_values(x), unp.nominal_values(y))
    return unp.uarray([A, B], [A_error, B_error])

#Linearisierung

def lin(I):
    return np.sqrt(I / 0.255)

#Theoriekurve

def theo_p(alpha, n):
    alpha = alpha / 360
    alpha = alpha * 2*np.pi
    return abs(((n**2) * np.cos(alpha) - np.sqrt(n**2 - (np.sin(alpha))**2)) / ((n**2) * np.cos(alpha) + np.sqrt(n**2 - (np.sin(alpha))**2)))

def theo_s(alpha, n):
    alpha = alpha / 360
    alpha = alpha * 2*np.pi
    return ((np.sqrt(n**2 - (np.sin(alpha))**2) - np.cos(alpha))**2) / (n**2 - 1)

#Messwerte

alpha_p, I_p = np.genfromtxt("Daten/parallel.txt", unpack=True) #alpha in Grad, I in mA
alpha_s, I_s = np.genfromtxt("Daten/senkrecht.txt", unpack=True) #alpha in Grad, I in mA
I_p_lin = lin(I_p)
I_s_lin = lin(I_s)


#Plot

y_p = np.linspace(alpha_p[0], alpha_p[-1], 100)
tI_p = theo_p(y_p, 2.50)

y_s = np.linspace(alpha_s[0], alpha_s[-1], 100)
tI_s = theo_s(y_s, 1.48)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.set_xlabel(r"$\alph_\text{A}a \mathbin{/} \unit{\degree}$")
ax.set_ylabel(r"$\sqrt{I\left(\alpha\right) \mathbin{/} I_{\text{e}}}$")
ax.plot(alpha_p, I_p_lin, ".", label="parallel")
ax.plot(alpha_s, I_s_lin, ".", label="senkrecht")
ax.plot(y_p, tI_p,"b-", label="Theorie parallel")
ax.plot(y_s, tI_s,"y-", label="Theorie senkrecht")
ax.grid(True)
ax.legend(loc="best")
fig.savefig("build/plot.pdf")