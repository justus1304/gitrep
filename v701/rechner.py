from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
#print("N_max/2(4cm) = " , 59397/2)
#print("N_max/2(7cm) = " , 11903/2)
#def p(x,p_0,l_eff):
#    return = x*p_0/l_eff
#def E()
def E(x):
    return (x/3.1)**(2/3)

print(E(ufloat(5.3,0.9)*10))
print(E(ufloat(2.4,0.4)*10))