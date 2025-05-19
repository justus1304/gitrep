from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.constants import c,h, m_e
import math
import statistics
a_p,I_p = np.genfromtxt("Daten/parallel.txt",unpack = True)
a_s,I_s = np.genfromtxt("Daten/senkrecht.txt",unpack = True)

#umrechnen in rad
a_p = a_p/57.2958 
a_s = a_s/57.2958 
#faktor auf messanzeige berücksichtigen 
I_p = I_p/3 
I_s = I_s/3 
I_e = 0.203


def n_p(a,E):
    return np.sqrt(E/(2*np.cos(a)**2)+(E**2/(4*np.cos(a)**4)-E*np.tan(a)**2)**(1/2))
def n_s(a,E):
    return np.sqrt(1+4*E*np.cos(a)**2/((E-1)**2))
    #return np.sqrt((E**2-2*E*np.cos(2*a)+1)/(E** -2*E+1))

array_s = n_s(a_s, np.sqrt(I_s/I_e))
#Mittelweet und fehler senkrecht
print(f"{statistics.mean(array_s):.2f}"," +- " f"{sem(array_s):.2f}")
n_s = ufloat(statistics.mean(array_s),sem(array_s))

array_p = n_p(a_p, ((I_p + 1)/(I_p-1))**2)
#Mittelwert
print(f"{statistics.mean(array_p):.2f}"," +- " f"{sem(array_p):.2f}")
n_p = ufloat(statistics.mean(array_p),sem(array_p))
#Brewster Winkel
print("T_B = ", np.arctan(statistics.mean(array_p))*57.29)
print("FT_B = ", np.arctan(sem(array_p))*57.29)
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
