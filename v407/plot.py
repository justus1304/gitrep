from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

a_p,I_p = np.genfromtxt("Daten/parallel.txt",unpack = True)
a_s,I_s = np.genfromtxt("Daten/senkrecht.txt",unpack = True)
I_p = I_p/3

def n_p(a,E):
    return np.sqrt(E/(2*np.cos(a)**2)+np.sqrt(E**2/(4*np.cos(a)**4)-E*np.tan(a)**2))
def n_s(a,E):
    return np.sqrt(1+4*E*np.cos(a)**2/((E-1)**2))
    #return np.sqrt((E**2-2*E*np.cos(2*a)+1)/(E** -2*E+1))

for i in range(len(I_p)):
    print(n_p(a_p[i],((I_p[i] + 1)/(I_p[i] - 1))**2))

print()
print()

for i in range(len(I_s)):
    print(n_s(a_s[i],(I_s[i])))




