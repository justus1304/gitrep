from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

print(1-(80/122))
print(1-(79/117))

mu0 = 4*np.pi*(10)**(-7)

x,y = np.genfromtxt("Daten/kurve.txt" ,unpack=True)
I = x #Ampere
r = 0.135 #meter
n = 595 #Windungen 
z = (n*x)/(2*np.pi*r)


print(z)

print((1 / mu0)*((0.00539)/(3507)))