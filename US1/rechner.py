from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

a = [0.5,0.6,0.7,0.5,0.7,0.7]
b = ufloat(np.mean(a), sem(a))
print("Mittewert = ", np.mean(a), sem(a))
print(ufloat(2744,14)*b)