import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
#import pandas as pd
from uncertainties import unumpy as unp  # Add this line
from scipy.optimize import curve_fit

#pirani,leit1,leit2 = np.genfromtxt('meineDaten/DPEK.txt', unpack = True)

import pandas as pd

# Alle Zeilen anzeigen
pd.set_option('display.max_rows', None)

# Alle Spalten anzeigen
pd.set_option('display.max_columns', None)

# CSV einlesen
df1 = pd.read_csv('Daten/TPLR1/TPG_all_data_2026_04_20-PM01_39_18.csv',sep=',')
df2 = pd.read_csv('Daten/TPLR2/TPG_all_data_2026_04_20-PM01_49_18.csv', sep=',')
df3 = pd.read_csv('Daten/TPLR3/TPG_all_data_2026_04_20-PM01_49_18.csv', sep=',')
df4 = pd.read_csv('Daten/TPLR4/TPG_all_data_2026_04_20-PM01_58_31.csv', sep=',')
#df42 = pd.read_csv('/home/justus/gitrep/v70/Daten/DPLR42/TPG_all_data_2026_04_20-PM05_11_52.csv', sep=',')
#df_gesamt = pd.concat([df41['	 TPG202 [mbar]1'], df42['	 TPG202 [mbar]']], axis=1)
#df_gesamt['mittelwert'] = df_gesamt[['	 TPG202 [mbar]1', '	 TPG202 [mbar]']].mean(axis=1)
# Die ersten 5 Zeilen anzeigen
#print(df.head())

# Zugriff auf eine bestimmte Spalte
druck1 = df1['	 TPG361_D1 [mbar]']
druck2 = df2['	 TPG361_D1 [mbar]']
druck3 = df3['	 TPG361_D1 [mbar]']
druck4 = df4['	 TPG361_D1 [mbar]']
#druck41 = df41['	 TPG202 [mbar]1']
#druck42 = df42['	 TPG202 [mbar]']

zeit1 = []
zeit2 = []
zeit3 = []
zeit4 = []

for i in range(len(druck1)):
    zeit1.append(i+1)

for i in range(len(druck2)):
    zeit2.append(i+1)

for i in range(len(druck3)):
    zeit3.append(i+1)

for i in range(len(druck4)):
    zeit4.append(i+1)


def druckFehler(a):
    x = 0
    if (a > 100):
        x = a*0.5
    else:
        x = a*0.3
    return x
i = 0
fehler1 = []
for e in druck1:
    fehler1.append(druckFehler(e))

for e in fehler1:
    print(f"{e:.2f}")
print ('')

fdruck1 = []
for i in range(len(fehler1)):
    fdruck1.append(ufloat(druck1[i],fehler1[i])) 

######
fehler2 = []
for e in druck2:
    fehler2.append(druckFehler(e))

for e in fehler2:
    print(f"{e:.2f}")
print ('')

fdruck2 = []
for i in range(len(fehler2)):
    fdruck2.append(ufloat(druck2[i],fehler2[i])) 
#####
fehler3 = []
for e in druck3:
    fehler3.append(druckFehler(e))

for e in fehler3:
    print(f"{e:.2f}")
print ('')

fdruck3 = []
for i in range(len(fehler3)):
    fdruck3.append(ufloat(druck3[i],fehler3[i])) 
###
fehler4 = []
for e in druck4:
    fehler4.append(druckFehler(e))

for e in fehler4:
    print(f"{e:.2f}")

fdruck4 = []
for i in range(len(fehler4)):
    fdruck4.append(ufloat(druck4[i],fehler4[i])) 

####
#fehler41 = []
#for e in druck41:
#    fehler41.append(druckFehler(e))
#
#for e in fehler41:
#    print(f"{e:.2f}")
#
#fdruck41 = []
#for i in range(len(fehler41)):
#    fdruck4.append(ufloat(druck41[i],fehler41[i])) 
#
#
######
#fehler42 = []
#for e in druck42:
#    fehler42.append(druckFehler(e))
#
#for e in fehler42:
#    print(f"{e:.2f}")
#
#fdruck42 = []
#for i in range(len(fehler42)):
#    fdruck4.append(ufloat(druck42[i],fehler42[i])) 
#######regressionen 

def linear(x,a,b):
    return a*x+b


##die 3 bereiche fitten

## Regression durchführen
## sigma übergibt die Fehlerbalken an den Fit-Algorithmus
#t_bereich1 = [e[0] for e in liste[0:150]]
#y_bereich1 = [np.asarray(e[2]).item().n for e in liste[0:150]]
#sigma_bereich1 = [np.asarray(e[2]).item().s for e in liste[0:150]]


def eins(zeit, druck, fehler,pfad,meinTitel):
    popt, pcov = curve_fit(linear, zeit[:], druck[:], sigma=fehler[:])

    m_fit1 = popt[0]
    m_fehler1 = np.sqrt(pcov[0,0]) # Standardabweichung der Steigung
    b_fit1 = popt[1]
    print(f"Steigung leckrate 1: {m_fit1:.2e} +/- {m_fehler1:.1e}")

    fig, ax1 = plt.subplots()
    ax1.errorbar(zeit, druck,linestyle='none',errorevery=20, yerr=fehler, fmt='o', markersize=0.4, color='black', linewidth=0.5,capsize=3, label='Messwerte')
    x = np.linspace(0,150,1000)
    ax1.plot(x,m_fit1 * x + b_fit1,label='Regression')
    ax1.set_xlabel('t / s')
    ax1.set_ylabel('p / mbar')
    fig.suptitle(meinTitel)
    ax1.legend()
    fig.savefig(f'{pfad}')
    return ufloat(m_fit1,m_fehler1)

# param1 = eins(zeit1,druck1,fehler1,'build/TurbomolekularpumpeLeckrate1.pdf',13,'Leckratenmessung Turbomolekularpumpe p_g = 0.502 mbar')
# param2 = eins(zeit2,druck2,fehler2,'build/TurbomolekularpumpeLeckrate2.pdf',2,'Leckratenmessung Turbomolekularpumpe p_g = 10 mbar')
# param3 = eins(zeit3,druck3,fehler3,'build/TurbomolekularpumpeLeckrate3.pdf',2,'Leckratenmessung Turbomolekularpumpe p_g = 50.1 mbar')
# param4 = eins(zeit4,druck4,fehler4,'build/TurbomolekularpumpeLeckrate4.pdf',0,'Leckratenmessung Turbomolekularpumpe p_g = 105 mbar')

param1 = eins(zeit1, druck1, fehler1, 'build/TurbomolekularpumpeLeckrate1.pdf', 
              r'Leckratenmessung Turbomolekularpumpe $p_g = (5 +- 1.5) \cdot 10^{-5}$ mbar')
param2 = eins(zeit2, druck2, fehler2, 'build/TurbomolekularpumpeLeckrate2.pdf',
              r'Leckratenmessung Turbomolekularpumpe $p_g = (6.9 +- 2.3) \cdot 10^{-4}$ mbar')  # 56.96e-5 = 5.696e-4
param3 = eins(zeit3, druck3, fehler3, 'build/TurbomolekularpumpeLeckrate3.pdf',
              r'Leckratenmessung Turbomolekularpumpe $p_g = (1 +- 0.3) \cdot 10^{-4}$ mbar')
param4 = eins(zeit4, druck4, fehler4, 'build/TurbomolekularpumpeLeckrate4.pdf',
              r'Leckratenmessung Turbomolekularpumpe $p_g = (1.9 +- 0.5) \cdot 10^{-4}$ mbar')

##### Tabellen erstellen 

def tabelle(zeit, druck, fehler,pfad):
    df = pd.DataFrame({
    'Zeit': zeit,
    'Druck': druck,
    'Fehler': fehler
    })
    df_g = df.iloc[::10]
    df_g.to_csv(f'{pfad}', index=False, sep=',')

tabelle(zeit1,druck1,fehler1,"build/dpergebnisse1.csv")
tabelle(zeit2,druck2,fehler2,"build/dpergebnisse2.csv")
tabelle(zeit3,druck3,fehler3,"build/dpergebnisse3.csv")
tabelle(zeit4,druck4,fehler4,"build/dpergebnisse4.csv")
#tabelle(zeit4,druck42,fehler42,"build/ergebnisse42.csv")

#############Volumen
V = ufloat(34,0.1*34)

def saug(v,pg,a):
    return v/pg * a
print('Saugvermögen l/ s')
print(saug(V,5.04*10**(-5),param1))
print(saug(V,6.96*10**(-5),param2))
print(saug(V,1.03*10**(-4),param3))
print(saug(V,1.91*10**(-4),param4))

print('saugvermögen m³/s')
print(saug(V,5.04*10**(-5),param1)*3.6)
print(saug(V,6.96*10**(-5),param2)*3.6)
print(saug(V,1.03*10**(-4),param3)*3.6)
print(saug(V,1.91*10**(-4),param4)*3.6)

druck = [5.04*10**(-5),6.96*10**(-5),1.03*10**(-4),1.91*10**(-4)]
saug = [saug(V,5.04*10**(-5),param1),saug(V,6.96*10**(-5),param2),saug(V,1.03*10**(-4),param3),saug(V,1.91*10**(-4),param4)]
saug1 = []
for i in range(len(saug)):
    saug1.append(saug[i].n)
saug1f = []
for i in range(len(saug)):
    saug1f.append(saug[i].s)

def sonMist(x,a):
    return 0*x + a


fig, ax = plt.subplots()

ax.errorbar(druck, saug1,linestyle='none',errorevery=1, yerr=saug1f, fmt='x', markersize=2, color='black', linewidth=0.5,capsize=3, label='Saugvermögen aus Leckratenmessung')
#x = np.linspace(0,210,1000)
#ax.plot(x,m_fit1 * x + b_fit1,label='Regression')
ax.set_xlabel('p / mbar')
ax.set_ylabel('S / l/sec')
x = np.linspace(0,0.0002,1000)
#b = np.linspace(150,290,1000)
#c = np.linspace(290,599,1000)
ax.errorbar(x, sonMist(x,15.4),linestyle='none',errorevery=20, yerr=sonMist(x,1.6), fmt='x', markersize=2, color='blue', linewidth=0.5,capsize=3, label='Saugvermögen aus Evakuierungskurve')
plt.xticks(rotation=45)
fig.suptitle('')
ax.legend()
ax.grid()
fig.savefig('build/saugvermögenTurbopumpe.pdf')
print(5.04*0.3)
print(5.69*0.3)
print(1.03*0.3)
print(1.91*0.3)