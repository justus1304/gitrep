from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
from math import log, pi
import statistics
import math

N = 0.95
f = 0.35
eta = 0.28
sigma = 5.7*10**(-12)

U1 = 3
U2 = 4
U3 = 4
U4 = 5
U5 = 5
I1 = 1.8
I2 = 2.0
I3 = 2.1
I4 = 2.3
I5 = 2.5

def T(U,I):
    return ((U * I - N)/(f * eta * sigma))**(0.25)

result1 = T(U1, I1)
print("T1: ", result1)

result2 = T(U2, I2)
print("T2: ", result2)

result3 = T(U3, I3)
print("T3: ", result3)

result4 = T(U4, I4)
print("T4: ", result4)

result5 = T(U5, I5)
print("T5: ", result5)

#-----------------------------------------------------
k = 1.381*10**(-23)
e = 1.602*10**(-19)
m = 9.109*10**(-31)
h = 6.626*10**(-34)

T1 = 1680.021
T2 = 1884.829
T3 = 1911.014
T4 = 2084.673
T5 = 2132.408

I1 = 0.007 * 10**(-3)
I2 = 0.066 * 10**(-3)
I3 = 0.120 * 10**(-3)
I4 = 0.593 * 10**(-3)
I5 = 2.140 * 10**(-3)
def W(T,I):
    return -k * T * log(h**3*I/(4 * pi * e * m * k**2 * T**2 * f))

res1 = W(T1,I1)
print("W1: ", res1)

res2 = W(T2,I2)
print("W2: ", res2)

res3 = W(T3,I3)
print("W3: ", res3)

res4 = W(T4,I4)
print("W4: ", res4)

res5 = W(T5,I5)
print("W5: ", res5)

print("W1 in eV: ", res1 * 1*.602*10**19)
print("W2 in eV: ", res2 * 1*.602*10**19)
print("W3 in eV: ", res3 * 1*.602*10**19)
print("W4 in eV: ", res4 * 1*.602*10**19)
print("W5 in eV: ", res5 * 1*.602*10**19)

zahlen = [5.541, 5.901, 5.892, 6.181, 6.103]
y = np.mean(zahlen)
print("Mittelwert: ", y)
print("Fehler d. Mittwelwerts: ", sem(zahlen))