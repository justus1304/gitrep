from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

R = 8.314
a = ufloat(-3874.9574 , 33.1933)

L = -R*a 
print(L, "L <1Bar")