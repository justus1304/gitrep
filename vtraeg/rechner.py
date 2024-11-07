from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

#berechnung trägheitsmoment kugel und zylinder
mk = ufloat(0.6386, 0.001)
rk = ufloat(0.0605,0.0001)

Tk = (2/5) * mk * rk * rk
print (Tk ," Trägheit kugel")

#zylinder
mz = ufloat(0.366, 0.001)
rz = ufloat(0.0493, 0.0001)
hz = ufloat(0.0995, 0.0001)

Tz = (1/2) * mz * rz * rz
print(Tz ," Trägheit zylinder")



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