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


#Puppe Berechnungen
 
mg = 0.3308 * 1000
#Mittelwerte radien
#Bein
dataRbein = np.array([1.25  ,1.305 ,1.19  ,1     ,0.95 , 1.010,1.075,0.97,0.825,0.78])
mwRbein = np.sum(dataRbein) / 10
mwFehlerRbein = sem(dataRbein)
print(mwRbein , mwFehlerRbein, "Radius Bein")
rb = ufloat(mwRbein, mwFehlerRbein)
#Arm
dataRarm = np.array([0.985 ,0.925 ,1.045 ,1.055 ,1.05  ,0.995 ,0.88  ,0.8   ,0.795 ,0.79 , 0.875,0.905,0.95,0.91,0.81,0.775,0.71,0.655,0.8,1.95 ])
mwRarm = np.sum(dataRarm) / 20
mwFehlerRarm = sem(dataRarm)
print(mwRarm , mwFehlerRarm, "Radius Arm")
ra = ufloat(mwRarm, mwFehlerRarm)
#Kopf
dataRkopf = np.array([1.580,1.725,1.715,1.65,1.59,1.425])
mwRkopf = np.sum(dataRkopf) / 6
mwFehlerRkopf = sem(dataRkopf)
print(mwRkopf , mwFehlerRkopf , "Radius Kopf")
rk = ufloat(mwRkopf, mwFehlerRkopf)
#Torso
dataRtorso = np.array([2.14 ,2.485,2.495,2.36 ,1.925, 1.885,2.415,2.195,2.03,3.67])
mwRtorso = np.sum(dataRtorso ) / 6
mwFehlerRtorso = sem(dataRtorso)
print(mwRtorso , mwFehlerRtorso , "Radius Torso")
rt = ufloat(mwRtorso, mwFehlerRtorso)

#(höhen)
ht = 7.19 + 4.28
ha = 6.075 + 5.74
hb = 7.54 + 8.46
hk = 5.02

#Volumen Körperteile
Vb = np.pi * (hb*rb*rb) 
Va = np.pi * (hb * rb * rb)
Vk = np.pi * (hk * rk * rk)
Vt = np.pi * (ht * rt * rt)

Vg = Vb + Va + Vk + Vt
#Berechnen der Trägheitsmomente einzelteile
mk = (Vk/Vg)*mg
mb = (Vb/Vg)*mg
ma = (Va/Vg)*mg
mt = (Vt/Vg)*mg

Ik = (2/5) * mk * rk * rk
It = (2/5) * mt * rt * rt
Ib = (2/5) * mb * rb * rb
Ia = (2/5) * ma * ra * ra

Iah = ma * ((ra*ra)/4 + (ha * ha)/12)
Ibh = mb * ((rb*rb)/4 + (hb * hb)/12)

#gesamtes Trägheitsmoment 
Ip1 = Ik + It + (Ib + mb*(rb)*(rb)) * 2 + (Ia + ma*(ra+rt)*(ra+rt)) * 2

Ip2 = Ik + It + (Ib + mb*(hb/2)*(hb/2)) + (Ibh + mb*(hb/2)*(hb/2)) + (Iah + ma*(ha/2+rt)*(ha/2+rt)) * 2

#umrechnung in kg*m²
Ip1 = Ip1 * 10**(-7)
Ip2 = Ip2 * 10**(-7)
print(repr(Ip1), "Gesamtes Trägheitsmoment P1")
print(repr(Ip2), "Gesamtes Trägheitsmoment P2")
print (" ")

#ausgabe mittel radien höhen ...
print(ra," Radius arm ", rb, " Radius Bein ", rk ," Radius Kopf ", rt, " Radius Torso ")
print (" ")
print(ha," höhe arm ", hb, " höhe Bein ", hk ," höhe Kopf ", ht, " höhe Torso ")
print (" ")
print(Va," Volumen arm ", Vb, " Volumen Bein ", Vk ," Volumen Kopf ", repr(Vt), " Volumen Torso ")
print (" ")
print(ma," masse arm ", mb, " hmasse Bein ", mk ," masse Kopf ", mt, " masse Torso ")

print(Ia," I arm ",repr(Iah), " Iarmh ", Ib, " I Bein ", repr(Ibh), " Ibh ", Ik ," I Kopf ", repr(It), " I Torso ")
  

#Mittelwert T Puppe
#pos1
dataPos1 = np.array([0.75,0.82,0.78,0.84,0.72,0.78,0.78,0.88,0.78,0.85])
mwPos1 = np.sum(dataPos1) / 10
mwFehlerPos1 = sem(dataPos1)
print(mwPos1 , mwFehlerPos1, "Tmw pos1")
Tp1 = ufloat(mwPos1, mwFehlerPos1)

#pos2
dataPos2 = np.array([1.59,1.63,1.75,1.69,1.65,1.78,1.72,1.61,1.62,1.55])
mwPos2 = np.sum(dataPos2) / 10
mwFehlerPos2 = sem(dataPos2)
print(mwPos2 , mwFehlerPos2, "Tmw pos2")
Tp2 = ufloat(mwPos2, mwFehlerPos2)

#I Puppen exp
Ipos1exp = ((Tp1*Tp1)/4*np.pi**2) * D
Ipos2exp = (Tp2**2/4*np.pi**2) * D

print(Ipos1exp , " Ipos1exp")
print(Ipos2exp , " Ipos2exp")

#a^2b^2
m = ufloat(0.113,  0.002)
b = ufloat(-1.019 , 0.540)
