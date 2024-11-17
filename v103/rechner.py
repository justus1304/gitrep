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
    I = (r**4 * np.pi)/4
    E = F / (2*a*I)
    print(I,"Flt rund")
    print(repr(E),"E modul rund einseitig")
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
    print(repr(E),"E modul eckig einseitig")
eckigerStabEinseitig()


print(" ")


def runderStabBeidseitigLinks():
    
    mg = 1 #kg
    a = ufloat( 0.00243 , 0.00018)
    
    G = 9.81
    F = mg*G
    r = 0.005
    I = (r**4 * np.pi)/4
    E = F / (48*a*I)
    
    print(repr(E),"E modul rund beidseitig links")
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
    
    print(repr(E),"E modul eckig beidseitig links")
eckigerStabBeidseitigLinks()


print(" ")
################################################################
def runderStabBeidseitigRechts():
    
    mg = 1 #kg
    a = ufloat( 0.00374 , 0.00014)
    
    G = 9.81
    F = mg*G
    r = 0.005
    I = (r**4 * np.pi)/4
    E = F / (48*a*I)
    
    print(repr(E),"E modul rund beidseitig Rechts")
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
    
    print(repr(E),"E modul eckig beidseitig Rechts")
eckigerStabBeidseitigRechts()