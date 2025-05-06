from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

n, o, u = np.genfromtxt("daten/acryl.txt", unpack = True)
v_s = ufloat(1374, 14 )
print(v_s*2)
#zeitdifferenz in strecke umrechnen + umrechnen in s und dann in mm(coursed)
s_o = o * (1/2) * 2730 * 10**(-3)
s_u = u * (1/2) * 2730 * 10**(-3)

for i in range(len(s_o)):
    print(s_o[i])
print()
for i in range(len(s_o)):
    print(s_u[i])