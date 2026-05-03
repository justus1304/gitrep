import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
#import pandas as pd
from uncertainties import unumpy as unp  # Add this line
from scipy.optimize import curve_fit
import pandas as pd
from scipy import stats

df1 = pd.read_csv('Daten/TPEK1/TPG_all_data_2026_04_20-PM12_57_24.csv',sep=',')
df2 = pd.read_csv('Daten/TPEK2/TPG_all_data_2026_04_20-PM01_06_54.csv', sep=',')
df3 = pd.read_csv('Daten/TPEK3/TPG_all_data_2026_04_20-PM01_15_54.csv', sep=',')
df4 = pd.read_csv('Daten/TPEK4/TPG_all_data_2026_04_20-PM01_21_30.csv', sep=',')
df5 = pd.read_csv('Daten/TPEK5/TPG_all_data_2026_04_20-PM01_28_16.csv', sep=',')


def druckFehler(a):
    x = 0
    if (a > 10):
        x = 1200 * 0.03
    else:
        if(a > 2*10**(-3)):
            x = a*0.1
        else :
            x = 2*a
    return x

def tabelle10(zeit, druck, fehler,pfad):
    df = pd.DataFrame({
    'Zeit': zeit,
    'Druck': druck,
    'Fehler': fehler
    })
    df_g = df.iloc[::10]
    df_g.to_csv(f'{pfad}', index=False, sep=',')

def tabelle(zeit, druck, fehler,pfad):
    df = pd.DataFrame({
    'Zeit': zeit,
    'Druck': druck,
    'Fehler': fehler
    })
    df_g = df
    df_g.to_csv(f'{pfad}', index=False, sep=',')

druck1 =df1['	 TPG361_D1 [mbar]']
druck2 =df1['	 TPG361_D1 [mbar]']
druck3 =df1['	 TPG361_D1 [mbar]']
druck4 =df1['	 TPG361_D1 [mbar]']
druck5 =df1['	 TPG361_D1 [mbar]']

#mittelwert druck
druck = []
for i in range(len(druck1)):
    mittel = np.mean([druck1[i],druck2[i],druck3[i],druck4[i],druck5[i]])
    druck.append(mittel)
#mittelwert druckfehler
druckfm = []
for i in range(len(druck1)):
    mittel = stats.sem([druck1[i],druck2[i],druck3[i],druck4[i],druck5[i]])
    druckfm.append(mittel)

#uflats erstellen 
#udruck = []
#for i in range(len(druck1)):
#   udruck.append(ufloat(druck[i],druckf[i]))


#haben mitelwerte und fehler des mittelwerts 

#nun systematischen fehler 
druckfs = []
for i in range(len(druck1)):
    druckfs.append(druckFehler(druck[i]))

#uflats erstellen
udruck = []
fgesamt = []
for i in range(len(druck1)):
    fehlergesammt = np.sqrt(druckfs[i]**2+druckfm[i]**2)
    udruck.append(ufloat(druck[i],fehlergesammt))
    fgesamt.append(fehlergesammt)

def logarithmus(p,pE,p0):
    return unp.log((p-pE)/(p0-pE))

# 1. Zuerst deine Druckwerte und deren Fehler in ein uarray packen
# (Ich nehme an, 'druck' und 'fgesamt' sind deine Listen von oben)
u_druck = unp.uarray(druck, fgesamt)

# 2. Deine Konstanten als ufloats definieren
pE = ufloat(3.52e-6, 0.3 * 3.52e-6)
p0 = 3.52e-3  # Falls p0 auch einen Fehler hat, hier ufloat nutzen

# 3. Den Logarithmus direkt auf das ganze Array anwenden
# Du brauchst hier KEINE Schleife (for i in range...), 
# da unp.log und die Rechenoperationen auf das ganze Array wirken.
ln = unp.log((u_druck - pE) / (p0 - pE))

# 4. Jetzt kannst du die Werte für Matplotlib oder curve_fit extrahieren
# Diese sind jetzt garantiert reine numpy-Arrays mit Floats.
lnn = unp.nominal_values(ln)
lns = unp.std_devs(ln)

# 5. Zeit-Array erstellen
zeit = np.arange(len(druck))

##ploten
#ax.errorbar(zeit, y_werte,linestyle='none',errorevery=20, yerr=y_fehler, fmt='o', markersize=0.4, color='black', linewidth=0.5,capsize=3)

tabelle(zeit,druck,fgesamt,"build/testtabelle.csv")


fig, ax1 = plt.subplots()
ax1.set_title('Ausgleichsrechnung zur bestimmung des Saugvermögens mit der Evakuierungskurve der Turbomolekularpumpe',fontsize = 1)
ax1.set_xlabel('t/s')
ax1.set_ylabel(r'$\ln\frac{p - p_E}{p_0 - p_E}$') # eigentlich: \ln(\frac{p - p_E}{p_0 - p_E}), NICHT log
#ax1.plot(zeit,y_werte,linestyle='',fmt ='o')

#x = np.linspace(min(t_bereich3),max(t_bereich3),1000)
#ax1.plot(x,(m_fit3 * x + b_fit3),linestyle ='-',label = 'regression 3',markersize = 5,linewidth = 5)
def error(a,b):
    ax1.errorbar(zeit[a:b], lnn[a:b],linestyle='none',errorevery=20, yerr=lns[a:b], fmt='o', markersize=0.4, color='black', linewidth=0.5,capsize=3,label='Messwerte')

def linear(x,a,b):
    return a*x+b

def fit(slice,b):
    popt, pcov = curve_fit(linear, zeit[slice:b], lnn[slice:b], sigma=lns[slice:b])

    m_fit1 = popt[0]
    m_fehler1 = np.sqrt(pcov[0,0]) # Standardabweichung der Steigung
    b_fit1 = popt[1]
    print(f"Steigung leckrate 1: {m_fit1:.2e} +/- {m_fehler1:.1e}")
    x = np.linspace(slice-2,b+10,1000)
    ax1.plot(x,m_fit1 * x + b_fit1)
    return(ufloat(m_fit1,m_fehler1))

ergebnis= fit(0,12)

ax1.grid()
error(0,100)
ax1.legend()
fig.savefig('build/turboevakuierung.pdf')

V = ufloat(33,0.1*33)
saug = - V * ergebnis
print(saug)

print(33*0.1)
print(3.52*10**-6*0.3)
print(5*0.3)

df = pd.DataFrame(
    {
        "zeit": zeit,
        "druck": druck,
        "fehler": fgesamt,
        "ln": lnn,
        "lnfehler": lns
    }
)
df.iloc[::10].to_csv("build/messdatendruck.csv", index=False, sep=';', encoding='utf-8')