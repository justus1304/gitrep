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
df1 = pd.read_csv('Daten/DPLR1/TPG_all_data_2026_04_20-PM04_14_00.csv', sep=',')
df2 = pd.read_csv('Daten/DPLR2/TPG_all_data_2026_04_20-PM04_33_53.csv', sep=',')
df3 = pd.read_csv('Daten/DPLR3/TPG_all_data_2026_04_20-PM04_53_22.csv', sep=',')
df41 = pd.read_csv('Daten/DPLR41/TPG_all_data_2026_04_20-PM05_02_36.csv', sep=',')
df42 = pd.read_csv('Daten/DPLR42/TPG_all_data_2026_04_20-PM05_11_52.csv', sep=',')
df_gesamt = pd.concat([df41['	 TPG202 [mbar]1'], df42['	 TPG202 [mbar]']], axis=1)
df_gesamt['mittelwert'] = df_gesamt[['	 TPG202 [mbar]1', '	 TPG202 [mbar]']].mean(axis=1)
# Die ersten 5 Zeilen anzeigen
#print(df.head())

# Zugriff auf eine bestimmte Spalte
druck1 = df1['TPG202 [mbar]']
druck2 = df2['	 TPG202 [mbar]']
druck3 = df3['	 TPG202 [mbar]']
druck4 = df_gesamt['mittelwert']
druck41 = df41['	 TPG202 [mbar]1']
druck42 = df42['	 TPG202 [mbar]']

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
    if (a > 10):
        x = 1200 * 0.03
    else:
        if(a > 2*10**(-3)):
            x = a*0.1
        else :
            x = 2*a
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
fehler41 = []
for e in druck41:
    fehler41.append(druckFehler(e))

for e in fehler41:
    print(f"{e:.2f}")

fdruck41 = []
for i in range(len(fehler41)):
    fdruck4.append(ufloat(druck41[i],fehler41[i])) 


#####
fehler42 = []
for e in druck42:
    fehler42.append(druckFehler(e))

for e in fehler42:
    print(f"{e:.2f}")

fdruck42 = []
for i in range(len(fehler42)):
    fdruck4.append(ufloat(druck42[i],fehler42[i])) 
######regressionen 

def linear(x,a,b):
    return a*x+b


##die 3 bereiche fitten

## Regression durchführen
## sigma übergibt die Fehlerbalken an den Fit-Algorithmus
#t_bereich1 = [e[0] for e in liste[0:150]]
#y_bereich1 = [np.asarray(e[2]).item().n for e in liste[0:150]]
#sigma_bereich1 = [np.asarray(e[2]).item().s for e in liste[0:150]]


def eins(zeit, druck, fehler,pfad,slice,meinTitel):
    popt, pcov = curve_fit(linear, zeit[slice:], druck[slice:], sigma=fehler[slice:])

    m_fit1 = popt[0]
    m_fehler1 = np.sqrt(pcov[0,0]) # Standardabweichung der Steigung
    b_fit1 = popt[1]
    print(f"Steigung leckrate 1: {m_fit1:.5f} +/- {m_fehler1:.5f}")

    fig, ax1 = plt.subplots()
    ax1.errorbar(zeit, druck,linestyle='none',errorevery=20, yerr=fehler, fmt='o', markersize=0.4, color='black', linewidth=0.5,capsize=3, label='Messwerte')
    x = np.linspace(0,210,1000)
    ax1.plot(x,m_fit1 * x + b_fit1,label='Regression')
    ax1.set_xlabel('t / s')
    ax1.set_ylabel('p / mbar')
    fig.suptitle(meinTitel)
    ax1.legend()
    fig.savefig(f'{pfad}')
    return ufloat(m_fit1,m_fehler1)

param1 = eins(zeit1, druck1, fehler1, 'build/drehschieberLeckrate1.pdf', 13, 
              r'Leckratenmessung Drehschieberpumpe $p_g = 0.502$ mbar')
param2 = eins(zeit2, druck2, fehler2, 'build/drehschieberLeckrate2.pdf', 2,
              r'Leckratenmessung Drehschieberpumpe $p_g = 10$ mbar')
param3 = eins(zeit3, druck3, fehler3, 'build/drehschieberLeckrate3.pdf', 2,
              r'Leckratenmessung Drehschieberpumpe $p_g = 50.1$ mbar')
param4 = eins(zeit4, druck4, fehler4, 'build/drehschieberLeckrate4.pdf', 0,
              r'Leckratenmessung Drehschieberpumpe $p_g = 105$ mbar')


##### Tabellen erstellen 

def tabelle(zeit, druck, fehler,pfad):
    df = pd.DataFrame({
    'Zeit': zeit,
    'Druck': druck,
    'Fehler': fehler
    })
    df_g = df.iloc[::10]
    df_g.to_csv(f'{pfad}', index=False, sep=',')

tabelle(zeit1,druck1,fehler1,"build/ergebnisse1.csv")
tabelle(zeit2,druck2,fehler2,"build/ergebnisse2.csv")
tabelle(zeit3,druck3,fehler3,"build/ergebnisse3.csv")
tabelle(zeit4,druck41,fehler41,"build/ergebnisse41.csv")
tabelle(zeit4,druck42,fehler42,"build/ergebnisse42.csv")

#############Volumen
V = ufloat(34,0.1*34)

def saug(v,pg,a):
    return v/pg * a
print('Saugvermögen l/ s')
print(saug(V,0.502,param1))
print(saug(V,10,param2))
print(saug(V,50.7,param3))
print(saug(V,105,param4))

print('saugvermögen m³/s')
print(saug(V,0.502,param1)*3.6)
print(saug(V,10,param2)*3.6)
print(saug(V,50.7,param3)*3.6)
print(saug(V,105,param4)*3.6)

druck = [0.502,10,50.7,105]
saug = [saug(V,0.502,param1)*3.6,saug(V,10,param2)*3.6,saug(V,50.7,param3)*3.6,saug(V,105,param4)*3.6]
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
a = np.linspace(0,150,1000)
b = np.linspace(150,290,1000)
c = np.linspace(290,599,1000)
ax.errorbar(a, sonMist(a,4.9),linestyle='none',errorevery=20, yerr=sonMist(a,0.5), fmt='x', markersize=2, color='blue', linewidth=0.5,capsize=3, label='S aus Evakuierungskurve Bereich 1')
ax.errorbar(b, sonMist(b,1.71),linestyle='none',errorevery=20, yerr=sonMist(b,0.17), fmt='x', markersize=2, color='yellow', linewidth=0.5,capsize=3, label='S aus Evakuierungskurve Bereich 2')

ax.errorbar(c, sonMist(c,0.70),linestyle='none',errorevery=20, yerr=sonMist(c,0.07), fmt='x', markersize=2, color='green', linewidth=0.5,capsize=3, label='S aus Evakuierungskurve Bereich 3')

plt.xticks(rotation=45)
fig.suptitle('')
ax.legend()
ax.grid()
fig.savefig('build/saugvermögenDrehschieberpumpe.pdf')