from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
import scipy.stats as stats
from scipy.stats import sem

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
        R2.append(ufloat(arrR2[i], arrR2[i] * 0.02))
        R3.append(ufloat(arrR3[i], arrR3[i] * 0.02))
        R4.append(ufloat(arrR4[i], arrR4[i] * 0.02))
        i = i + 1

    sumR11 = 0
    sumR14 = 0
    sumR12 = 0

###Wiederstand R 11
    i = 0
    
    arr = []
    #arr.append(R2[1] * (R3[1] / R4[1]))
    arr.append((R2[1] * (R3[1] / R4[1]))**2)
    arr.append((R2[2] * (R3[2] / R4[2]))**2)
    arr.append((R2[3] * (R3[3] / R4[3]))**2)
        
    wertR11 = np.mean(arr)
    print("R11 = ", wertR11)
    print(np.sqrt(432000-629))

### wiederstand R 14
    i = 3
    arr = []
    while i <6:
        arr.append(R2[i] * (R3[i] / R4[i]))
        i = i + 1
    wertR14 = np.mean(arr)
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
        R2.append(ufloat(arrR2[i], arrR2[i] * 0.02))
        R3.append(ufloat(arrR3[i], arrR3[i] * 0.02))
        R4.append(ufloat(arrR4[i], arrR4[i] * 0.02))
        C2.append(ufloat(arrC2[i], arrC2[i] * 0.02))
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

#Kapazitätsmessung
def induktivitaet():
    arrR2 = [ 58 ,108,75 ,51 ,86 ,59 ,103,194,138]
    arrR3 = [ 647,496,572,901,831,870,773,645,713]
    arrR4 = [ 353,504,428,99,169,130,227,355,287]
    arrL2 = [ 14.6,27.5,20.1,14.6,27.5,20.1,14.6,27.5,20.1]
    #Rx = arrR2[i] * (arrR3[i]/arrR4[i])
    R2 = []
    R3 = []
    R4 = []
    L2 = []
    i = 0
    while i < 9:
        R2.append(ufloat(arrR2[i], arrR2[i] * 0.02))
        R3.append(ufloat(arrR3[i], arrR3[i] * 0.02))
        R4.append(ufloat(arrR4[i], arrR4[i] * 0.02))
        L2.append(ufloat(arrL2[i], arrL2[i] * 0.02))
        i = i + 1

    sumR18 = 0
    sumR16 = 0
    sumR9 = 0

    sumL19 = 0
    sumL16 = 0
    sumL18 = 0

    print("")
###wert 19
    i = 0
    arr = []
    while i <3:
        arr.append(R2[i] * (R3[i] / R4[i]))
        sumL19 = sumL19 + L2[i] * (R3[i] / R4[i])
        i = i + 1
    wertR19 = np.mean(arr)
    wertL19 = sumL19 / 3
    print("R19 = ", wertR19)
    print("L19 = ", wertL19)
    print("")

###wert 15
    i = 3
    while i <6:
        sumR16 = sumR16 + R2[i] * (R3[i] / R4[i])
        sumL16 = sumL16 + L2[i] * (R3[i] / R4[i])
        i = i + 1
    wertR16 = sumR16 / 3
    wertL16 = sumL16 / 3
    print("R16 = ", wertR16)
    print("L16 = ", wertL16)
    print("")

###wert 9
    i = 6
    while i <9:
        sumR9 = sumR9 + R2[i] * (R3[i] / R4[i])
        sumL18 = sumL18 + L2[i] * (R3[i] / R4[i])
        i = i + 1
    wertR9 = sumR9 / 3
    wertL18 = sumL18 / 3
    print("R9 = ", wertR9)
    print("L18 = ", wertL18)
    print("")
induktivitaet()  

g2 = np.sqrt(   (1/9) * (2**2-1)**2 / ((1-2**2)**2 + 9*2**2)    )
print("g(2) = ", g2)
U2 = v0 * g2
print("k = ", U2/1000)