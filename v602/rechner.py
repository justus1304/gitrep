import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import nominal_values as noms, std_devs as stds
import scipy.constants as const
import scipy.optimize
import sympy
import uncertainties as unc
from uncertainties import ufloat
from scipy.constants import h,c

def minl(t,d):
    return 2*d*unp.sin(t)
def maxe(l):
    return ((h*2*np.pi)*c)/l
def E(t,d):
    return maxe(minl(t*np.pi/180, d))
def f(x,R):
    return 0*x+R

def bog(g):
    return g*np.pi /180

def aufloesung():
    print(E(5.7, 201.4*10**(-12)))
    
    mittela = E(ufloat(22.35,0.1), 201.4*10**(-12))
    mina = E(ufloat(22,0.1), 201.4*10**(-12))
    maxa = E(ufloat(22.7,0.1), 201.4*10**(-12))
    mittelb = E(ufloat(20.1,0.1), 201.4*10**(-12))
    minb = E(ufloat(19.8,0.1), 201.4*10**(-12))
    maxb = E(ufloat(20.4,0.1), 201.4*10**(-12))
    
    print("difa",mina-maxa)
    print("mittel a ",maxa)
    print("difb ",minb-maxb)
    print("mittel b ",mittelb)
    print("aufloese a =", mittela/(mina-maxa))
aufloesung()