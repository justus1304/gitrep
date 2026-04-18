#Kapazitätsmessung
def kapazitätsmessung():
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
        R2.append(ufloat(arrR2[i], arrR2[i] * 0.002))
        R3.append(ufloat(arrR3[i], arrR3[i] * 0.002))
        R4.append(ufloat(arrR4[i], arrR4[i] * 0.002))
        L2.append(ufloat(arrL2[i], arrL2[i] * 0.002))
        i = i + 1

    sumR18 = 0
    sumR16 = 0
    sumR9 = 0

    sumL19 = 0
    sumL16 = 0
    sumL18 = 0

    print("")
###wert 8
    i = 0
    while i <3:
        sumR18 = sumR18 + R2[i] * (R3[i] / R4[i])
        sumL19 = sumL19 + L2[i] * (R3[i] / R4[i])
        i = i + 1
    wertR18 = sumR18 / 3
    wertL19 = sumL19 / 3
    print("R18 = ", wertR18)
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
kapazitätsmessung()  