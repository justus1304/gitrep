from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

n, o, u = np.genfromtxt("daten/acryl.txt", unpack = True)
v_s = ufloat(1374, 14 ) * 2
print(n)
print(o)
print(u)
print(v_s*2)
#zeitdifferenz in strecke umrechnen + umrechnen in s und dann in mm(komisch xd)
s_o = (o ) * (1/2) * v_s * 10**(-3)
s_u = (u ) * (1/2) * v_s * 10**(-3)
s_hoehe = 59.2 * (1/2) * v_s * 10**(-3)
print("obere distanz")
for i in range(len(s_o)):
    print(s_o[i])

print("untere distanz")
for i in range(len(s_o)):
    print(s_u[i])

#lochdurchmesser aus Positionen bestimmen
h = 79.65 #mm
d =  s_hoehe - (s_o + s_u)

print("durchmesser")
for i in range(len(d)):
    print(d[i])

print(s_hoehe)

auge = np.genfromtxt("daten/auge.txt", unpack = True)
s_auge = (auge ) * (1/2) * v_s * 10**(-3)
print("auge")
for i in range(len(s_auge)):
    print(s_auge[i])