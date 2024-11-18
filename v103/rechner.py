from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem


#runder Stab einseitig
def runderStabEinseitig():
    
    mg = 0.2 #kg
    a = ufloat( 0.0100 , 0.0005)
    
    G = 9.81
    F = mg*G
    r = 0.005
    I = (r**4 * np.pi)/2
    E = F / (2*a*I)
    print(I,"Flt rund")
    print(E,"E modul rund einseitig")
runderStabEinseitig()

def eckigerStabEinseitig():
    
    mg = 0.2 #kg
    a = ufloat( 0.0059 , 0.0003)
    
    G = 9.81
    F = mg*G
    h = 0.01
    I = (h**4)/12
    E = F / (2*a*I)
    print(I,"Flt eckig")
    print(E,"E modul eckig einseitig")
eckigerStabEinseitig()


print(" ")


def runderStabBeidseitigLinks():
    
    mg = 1 #kg
    a = ufloat( 0.00243 , 0.00018)
    
    G = 9.81
    F = mg*G
    r = 0.005
    I = (r**4 * np.pi)/2
    E = F / (48*a*I)
    
    print(E,"E modul rund beidseitig links")
runderStabBeidseitigLinks()

print(" ")
def eckigerStabBeidseitigLinks():
    
    mg = 1 #kg
    a = ufloat( 0.00189 , 0.00006)
    
    G = 9.81
    F = mg*G
    h = 0.01
    I = (h**4)/12
    E = F / (48*a*I)
    
    print(E,"E modul eckig beidseitig links")
eckigerStabBeidseitigLinks()


print(" ")
################################################################
def runderStabBeidseitigRechts():
    
    mg = 1 #kg
    a = ufloat( 0.00374 , 0.00014)
    
    G = 9.81
    F = mg*G
    r = 0.005
    I = (r**4 * np.pi)/2
    E = F / (48*a*I)
    
    print(E,"E modul rund beidseitig Rechts")
runderStabBeidseitigRechts()
print(" ")
def eckigerStabBeidseitigRechts():
    
    mg = 1 #kg
    a = ufloat( 0.00272 , 0.00008)
    
    G = 9.81
    F = mg*G
    h = 0.01
    I = (h**4)/12
    E = F / (48*a*I)
    
    print(E,"E modul eckig beidseitig Rechts")
eckigerStabBeidseitigRechts()


Ere = ufloat(1.00 * 10**(11), 0.05 * 10**(11))
Erl = ufloat(8.6 * 10**(10), 0.6 * 10**(10))
Err = ufloat(1.30 * 10**(11), 0.04 * 10**(11))

Eee = ufloat(2.00 * 10**(11), 0.01 * 10**(11))
Eel = ufloat(5.57 * 10**(10), 0.21 * 10**(10))
Eer = ufloat(9.02 * 10**(10), 0.27 * 10**(10))

Erund = (Ere + Erl + Err)/3
Eeckig = (Eee + Eel + Eer)/3

print(Erund)
print(Eeckig)


print(390 / (60 * np.pi * 0.5**2))
print(500 / (60 * 1),"Dichte Eckig")

print(Erund/10**9)
print(Eeckig/10**9)
abweichungRund = (Erund/10**9) / 100
abweichungEckig = (Eeckig/10**9) / 100
print(abweichungRund,"abweichung Rund")
print(abweichungEckig,"abweichung Eckig")