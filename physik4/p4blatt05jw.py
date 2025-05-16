import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, e,g,m_e

#radius berrechnen (r = L)
lamda = 4 * 10**(-6) #Welllenlänge des Lichts
L = np.sqrt(h*2*np.pi**2*lamda*3/(4*c*m_e))
print(L)