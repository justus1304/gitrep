from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

#berechnung konstante D
dataPhi = np.array([22.5 ,45   ,67.5 ,90   ,112.5,135  ,157.5,180  ,202.5,225  ])
dataF = np.array([0.0000,0.04,0.068,0.09,0.126,0.164,0.172,0.18,0.2,0.28])
dataD = np.array([0.0000000000,0,0,0,0,0,0,0,0,0])
#print(dataF)
i = 0
while(i<= 9):
    #print(dataF[i])
    #print(dataPhi[i])
    dataD[i] = (dataF[i]*0.292)/(dataPhi[i])
    #print(dataD[i])
    i = i+1
    #print(dataD)
mwD = np.sum(dataD) / 10
mwFehlerD = sem(dataD)
print(mwD , mwFehlerD, "mwD")
D = ufloat(mwD, mwFehlerD)

#berechnung trägheitsmoment kugel und zylinder
mk = ufloat(0.6386, 0.001)
rk = ufloat(0.0605,0.0001)

Tk = (2/5) * mk * rk * rk
print (Tk ," Trägheit kugel theor")

#zylinder
mz = ufloat(0.366, 0.001)
rz = ufloat(0.0493, 0.0001)
hz = ufloat(0.0995, 0.0001)

Tz = (1/2) * mz * rz * rz
print(Tz ," Trägheit zylinder theor")

#Mittelwerte plus fehler Kugel
dataK = np.array([1.13 ,1.22 ,1.15 ,1.16 ,1.16 ,1.22 ,1.22 ,1.25, 1.16 ,1.19 ])
mwKugel = np.sum(dataK) / 10
mwFehlerKugel = sem(dataK)
print(mwKugel , mwFehlerKugel)

#Mittelwerte plus fehler Zylinder
dataZ = np.array([0.78,0.65,0.78,0.78,0.78,0.75,0.72,0.79,0.75,0.78 ])
mwZylinder = np.sum(dataZ) / 10
mwFehlerZylinder = sem(dataZ)
print(mwZylinder , mwFehlerZylinder)

#Trägheitsmomente k,z experimentel
Tk = ufloat(1.1859999999999997, 0.012489995996796807)
Tz = ufloat(0.756, 0.01359738536958076)

Ik = (Tk*Tk*D)/4*np.pi*np.pi
print(Ik, "Trägheitsmoment kugel")

Iz = (Tz*Tz*D)/4*np.pi*np.pi
print(Iz, "Trägheitsmoment zylinder")





""" d1 = ufloat((0), 0)
d2 = ufloat((0.04*29.2)/45, 0)
d3 = ufloat((0.06*29.2)/67.5, 0)
d4 = ufloat((0.09*29.2)/90, 0)
d5 = ufloat((0.12*29.2)/112.5, 0)
d6 = ufloat((0.16*29.2)/135, 0)
d7 = ufloat((0.17*29.2)/157.5, 0)
d8 = ufloat((0.18*29.2)/180, 0)
d9 = ufloat((0.20*29.2)/102.5, 0)
d10 = ufloat((0.28*29.2)/225, 0)

mwd = np.mean([d1,d2,d3])

print(mwd) """