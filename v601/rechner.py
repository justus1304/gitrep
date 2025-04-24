from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
from scipy.constants import h, c, e

def mfwl(T):
    w = 0.0029 / (5.5 * 10**7 * np.exp(-6876/T)) *0.1
    return w
print(mfwl(296.15))
print(mfwl(419.15))
print(mfwl(436.15))
print(mfwl(448.15))

print()

print(0.62/8)

print()


def steigung(a):
    print(a * 0.000875/1)
    return 0
steigung(0.3)


def xwert(b):
    print((50/184) * (b - 1))
    return 0
xwert(183.5)

print((h*c)/(5.5*e))