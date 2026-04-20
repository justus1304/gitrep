from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

R = 8.314
a = ufloat(-3874.9574 , 33.1933)

L = -R*a 
print( "L <1Bar = " , L)

L_a = R * 373

print("L_a = " , L_a)

L_i = L - L_a 

print ("L_i = " , L_i)

L_i_EV = (L_i / (6.022 * 10**(23))) / (1.602 * 10**(-19))

print("L_i in EV = ", L_i_EV)