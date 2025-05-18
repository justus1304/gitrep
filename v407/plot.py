from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.constants import c,h, m_e
import math
a_p,I_p = np.genfromtxt("Daten/parallel.txt",unpack = True)
a_s,I_s = np.genfromtxt("Daten/senkrecht.txt",unpack = True)
fehler = ufloat(1,0.002)
a_p = a_p/57.2958 
a_s = a_s/57.2958 
I_p = I_p/3 
I_s = I_s/3 
E_e = 0.153


def n_p(a,E):
    return np.sqrt(E/(2*np.cos(a)**2)+(E**2/(4*np.cos(a)**4)-E*np.tan(a)**2)**(1/2))
def n_s(a,E):
    return np.sqrt(1+4*E*np.cos(a)**2/((E-1)**2))
    #return np.sqrt((E**2-2*E*np.cos(2*a)+1)/(E** -2*E+1))
MW_p = 0
for i in range(len(I_p)):
    MW_p = MW_p + (n_p(a_p[i],((I_p[i] + 1)/(I_p[i] - 1))**2))
    print(n_p(a_p[i],((I_p[i] + 1)/(I_p[i] - 1))**2))
print('MW_p = ',MW_p/len(I_p))
print()
print()
MW_s = 0
for i in range(len(I_s)):
    MW_s = MW_s + n_s(a_s[i],(I_s[i]))
    print(n_s(a_s[i],(I_s[i])))
print('MW_s = ',MW_s/len(I_s))
print(sem(n_p(a_p,I_p)))

def f(a,n_s):
    return E_e*((np.sqrt(n_s**2-np.sin(a)**2)-np.cos(a))**2/(n_s**2-1))
def g(a,n_p):
    return abs(E_e*((n_p**2*np.cos(a)-(n_p**2-np.sin(a)**2)**(1/2))/(n_p**2*np.cos(a)+np.sqrt(n_p**2-np.sin(a)**2))))
fig, ax =plt.subplots()

ax.plot(a_p,np.sqrt(I_p),"rx",label = "Parallele Polarisation")
ax.plot(a_s,np.sqrt(I_s),"kx",label = 'Senkrechte polarisation')
a = np.linspace(0,1.55,1000)
ax.plot(a, f(a,1.04))
ax.plot(a, g(a,2.597))
ax.legend()
ax.grid(True)
#ax.set_xscale("log")
fig.savefig("plot.pdf")

#Brewster Winkel in Grad Celsius
theta_browster = 57.2958 *np.arctan( 2.497/1)
print('Brewster Winkel = ' , theta_browster)

