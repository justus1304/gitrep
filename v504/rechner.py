from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

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