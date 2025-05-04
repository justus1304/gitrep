from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
##Todzeit
N1 = 11936
N2 = 15383
N12 = 27556
t = (N1+N2-N12) / (N12**2-N1**2-N2**2)
print(t*10)