from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
##Todzeit
N1 = 11936 /200
N2 = 15383 /200
N12 = 27556 /200

#N1 = 158000 /120
#N2 = 155000 /120
#N12 = 270000 /120
t = (N1+N2-N12) / (N12**2-N1**2-N2**2)
t2 =  (N1+N2-N12) / (2*N1 * N2)
print(t)
print(t2)

print(129/150)