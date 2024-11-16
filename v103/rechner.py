from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

a = ufloat(0.0000000019 , 0.0000000001)
G = 6.67430e-11
mg = 1 #kg
F = mg*G
r = 25
I = (r**4 * np.pi)/2
E = F / (48*a*I)
print(E)