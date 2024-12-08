from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
import scipy.stats as stats
from scipy.stats import sem
print(a)
#Wiederstandsmessung
def wiederstandmessung():
    arrR2 = [1000,664 ,332 ,1000,664 ,332 ,1000,664 ,332 ]
    arrR3 = [ 330,426 ,597  ,474,574 ,732 , 281,370 ,541 ]
    arrR4 = [ 670,574,403, 526,426,268, 719,630,459]
    #Rx = arrR2[i] * (arrR3[i]/arrR4[i])
    R2 = []
    R3 = []
    R4 = []
    i = 0
    while i < 9:
        R2.append(ufloat(arrR2[i], arrR2[i] * 0.002))
        R3.append(ufloat(arrR3[i], arrR3[i] * 0.002))
        R4.append(ufloat(arrR4[i], arrR4[i] * 0.002))
        i = i + 1

    sumR11 = 0
    sumR14 = 0
    sumR12 = 0

###Wiederstand R 11
    i = 0
    while i <3:
        
        sumR11 = sumR11 + R2[i] * (R3[i] / R4[i])
        i = i + 1
    wertR11 = sumR11 / 3
    print("R11 = ", wertR11)


### wiederstand R 14
    i = 3
    while i <6:
        sumR14 = sumR14 + R2[i] * (R3[i] / R4[i])
        i = i + 1
    wertR14 = sumR14 / 3
    print("R14 = ", wertR14)

### wiederstand R 12
    i = 6
    while i <9:
        sumR12 = sumR12 + R2[i] * (R3[i] / R4[i])
        i = i + 1
    wertR12 = sumR12 / 3
    print("R12 = ", wertR12)
wiederstandmessung()  



#Kapazitätsmessung
def kapazitätsmessung():
    arrR2 = [164,369,728,285,654,542,204,443,334]
    arrR3 = [ 772,603,670,620,413,471,693,510,580]
    arrR4 = [ 228,397,330,380,587,529,307,490,420]
    arrC2 = [992,450,597,992,450,597,992,450,597]
    #Rx = arrR2[i] * (arrR3[i]/arrR4[i])
    R2 = []
    R3 = []
    R4 = []
    C2 = []
    i = 0
    while i < 9:
        R2.append(ufloat(arrR2[i], arrR2[i] * 0.002))
        R3.append(ufloat(arrR3[i], arrR3[i] * 0.002))
        R4.append(ufloat(arrR4[i], arrR4[i] * 0.002))
        C2.append(ufloat(arrC2[i], arrC2[i] * 0.002))
        i = i + 1

    sumR8 = 0
    sumR15 = 0
    sumR9 = 0

    sumC8 = 0
    sumC15 = 0
    sumC9 = 0

    print("")
###wert 8
    i = 0
    while i <3:
        sumR8 = sumR8 + R2[i] * (R3[i] / R4[i])
        sumC8 = sumC8 + C2[i] * (R4[i] / R3[i])
        i = i + 1
    wertR8 = sumR8 / 3
    wertC8 = sumC8 / 3
    print("R8 = ", wertR8)
    print("C8 = ", wertC8)
    print("")

###wert 15
    i = 3
    while i <6:
        sumR15 = sumR15 + R2[i] * (R3[i] / R4[i])
        sumC15 = sumC15 + C2[i] * (R4[i] / R3[i])
        i = i + 1
    wertR15 = sumR15 / 3
    wertC15 = sumC15 / 3
    print("R15 = ", wertR15)
    print("C15 = ", wertC15)
    print("")

###wert 9
    i = 6
    while i <9:
        sumR9 = sumR9 + R2[i] * (R3[i] / R4[i])
        sumC9 = sumC9 + C2[i] * (R4[i] / R3[i])
        i = i + 1
    wertR9 = sumR9 / 3
    wertC9 = sumC9 / 3
    print("R9 = ", wertR9)
    print("C9 = ", wertC9)
    print("")
kapazitätsmessung()

w0 = 1 / (1000*663*10**(-9))
v0 = w0 / (2*np.pi)
print(v0)
print(w0)



