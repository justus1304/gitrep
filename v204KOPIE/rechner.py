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

#Wärmeströme, kappa [W/ mK], A[m], delT[s], delx[m] --> dQ[W]
#zu T1-T2
#zu 100s
dQ_dt11 = -120 * 0.004 * 0.007 * (36.77-31.27)/0.03
print("dQ1 nach 100s = ", dQ_dt11)
#zu 200s
dQ_dt12 = -120 * 0.004 * 0.007 * (40.05-36.9)/0.03
print("dQ1 nach 200s = ", dQ_dt12)
#zu 400s
dQ_dt13 = -120 * 0.004 * 0.007 * (42.56-40.72)/0.03
print("dQ1 nach 400s = ", dQ_dt13)
#zu 600s
dQ_dt14 = -120 * 0.004 * 0.007 * (43.28-42.28)/0.03
print("dQ1 nach 600s = ", dQ_dt14)
#zu 800
dQ_dt15 = -120 * 0.004 * 0.007 * (47.48-45.3)/0.03
print("dQ1 nach 800s = ", dQ_dt15)

#zu T7-T8
#zu 100s
dQ_dt21 = -120 * 0.004 * 0.012 * (34.93-22.85)/0.03
print("dQ2 nach 100s = ", dQ_dt21)
#zu 200s
dQ_dt22 = -120 * 0.004 * 0.012 * (37.37-26.37)/0.03
print("dQ2 nach 200s = ", dQ_dt22)
#zu 400s
dQ_dt23 = -120 * 0.004 * 0.012 * (39.11-30.20)/0.03
print("dQ2 nach 400s = ", dQ_dt23)
#zu 600s
dQ_dt24 = -120 * 0.004 * 0.012 * (40.60-32.59)/0.03
print("dQ2 nach 600s = ", dQ_dt24)
#zu 800
<<<<<<< HEAD
dQ_dt25 = -120 * 0.004 * 0.012 * (44.1-34.89)/0.03
print("dQ2 nach 800s = ", dQ_dt25)
||||||| ea5476e
dQ_dt25 = -120 * 0.09 * 0.012 * (44.1-34.89)/0.03
print("dQ2 nach 800s = ", dQ_dt25)
=======
dQ_dt25 = -120 * 0.09 * 0.012 * (44.1-34.89)/0.03
print("dQ2 nach 800s = ", dQ_dt25)



#abweichung aluminium
print(248/235)
>>>>>>> refs/remotes/origin/main
