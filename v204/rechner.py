from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

#berechnung der Konstanten der Stäbe

#Abmessungen in cm
l_Mb = 9
b_Mb = 1.2
h_Mb = 0.4

l_A = 9
b_A = 1.2
h_A = 0.4

l_E = 9
b_E = 1.2
h_E = 0.4

#Dichte in kg/m^3
r_M = 8520
r_A = 2800
r_E = 8000

#wärmekapazitäten
c_M = 385
c_A = 830
c_E = 400