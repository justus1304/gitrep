#import matplotlib.pyplot as plt
#import numpy as np
#from uncertainties import ufloat
##import pandas as pd
#from uncertainties import unumpy as unp  # Add this line
#from scipy.optimize import curve_fit
#import pandas as pd
#from scipy import stats
#
#df1 = pd.read_csv('Daten/TPEK1/TPG_all_data_2026_04_20-PM12_57_24.csv',sep=',')
#df2 = pd.read_csv('Daten/TPEK2/TPG_all_data_2026_04_20-PM01_06_54.csv', sep=',')
#df3 = pd.read_csv('Daten/TPEK3/TPG_all_data_2026_04_20-PM01_15_54.csv', sep=',')
#df4 = pd.read_csv('Daten/TPEK4/TPG_all_data_2026_04_20-PM01_21_30.csv', sep=',')
#df5 = pd.read_csv('Daten/TPEK5/TPG_all_data_2026_04_20-PM01_28_16.csv', sep=',')
#
#
#def druckFehler(a):
#    x = 0
#    if (a > 10):
#        x = 1200 * 0.03
#    else:
#        if(a > 2*10**(-3)):
#            x = a*0.1
#        else :
#            x = 2*a
#    return x
#
#def tabelle10(zeit, druck, fehler,pfad):
#    df = pd.DataFrame({
#    'Zeit': zeit,
#    'Druck': druck,
#    'Fehler': fehler
#    })
#    df_g = df.iloc[::10]
#    df_g.to_csv(f'{pfad}', index=False, sep=',')
#
#def tabelle(zeit, druck, fehler,pfad):
#    df = pd.DataFrame({
#    'Zeit': zeit,
#    'Druck': druck,
#    'Fehler': fehler
#    })
#    df_g = df
#    df_g.to_csv(f'{pfad}', index=False, sep=',')
#
#druck1 =df1['	 TPG361_D1 [mbar]']
#druck2 =df1['	 TPG361_D1 [mbar]']
#druck3 =df1['	 TPG361_D1 [mbar]']
#druck4 =df1['	 TPG361_D1 [mbar]']
#druck5 =df1['	 TPG361_D1 [mbar]']
#
##mittelwert druck
#druck = []
#for i in range(len(druck1)):
#    mittel = np.mean([druck1[i],druck2[i],druck3[i],druck4[i],druck5[i]])
#    druck.append(mittel)
##mittelwert druckfehler
#druckfm = []
#for i in range(len(druck1)):
#    mittel = stats.sem([druck1[i],druck2[i],druck3[i],druck4[i],druck5[i]])
#    druckfm.append(mittel)
#
##uflats erstellen 
##udruck = []
##for i in range(len(druck1)):
##   udruck.append(ufloat(druck[i],druckf[i]))
#
#
##haben mitelwerte und fehler des mittelwerts 
#
##nun systematischen fehler 
#druckfs = []
#for i in range(len(druck1)):
#    druckfs.append(druckFehler(druck[i]))
#
##uflats erstellen
#udruck = []
#fgesamt = []
#for i in range(len(druck1)):
#    fehlergesammt = np.sqrt(druckfs[i]**2+druckfm[i]**2)
#    udruck.append(ufloat(druck[i],fehlergesammt))
#    fgesamt.append(fehlergesammt)
#
#def logarithmus(p,pE,p0):
#    return unp.log((p-pE)/(p0-pE))
#
## 1. Zuerst deine Druckwerte und deren Fehler in ein uarray packen
## (Ich nehme an, 'druck' und 'fgesamt' sind deine Listen von oben)
#u_druck = unp.uarray(druck, fgesamt)
#
## 2. Deine Konstanten als ufloats definieren
#pE = ufloat(3.52e-6, 0.3 * 3.52e-6)
#p0 = 3.52e-3  # Falls p0 auch einen Fehler hat, hier ufloat nutzen
#
## 3. Den Logarithmus direkt auf das ganze Array anwenden
## Du brauchst hier KEINE Schleife (for i in range...), 
## da unp.log und die Rechenoperationen auf das ganze Array wirken.
#ln = unp.log((u_druck - pE) / (p0 - pE))
#
## 4. Jetzt kannst du die Werte für Matplotlib oder curve_fit extrahieren
## Diese sind jetzt garantiert reine numpy-Arrays mit Floats.
#lnn = unp.nominal_values(ln)
#lns = unp.std_devs(ln)
#
## 5. Zeit-Array erstellen
#zeit = np.arange(len(druck))
#
###ploten
##ax.errorbar(zeit, y_werte,linestyle='none',errorevery=20, yerr=y_fehler, fmt='o', markersize=0.4, color='black', linewidth=0.5,capsize=3)
#
#tabelle(zeit,druck,fgesamt,"build/testtabelle.csv")
#
#
#fig, ax1 = plt.subplots()
#ax1.set_title('Ausgleichsrechnung zur bestimmung des Saugvermögens mit der Evakuierungskurve der Turbomolekularpumpe',fontsize = 1)
#ax1.set_xlabel('t/s')
#ax1.set_ylabel(r'$\ln\frac{p - p_E}{p_0 - p_E}$') # eigentlich: \ln(\frac{p - p_E}{p_0 - p_E}), NICHT log
##ax1.plot(zeit,y_werte,linestyle='',fmt ='o')
#
##x = np.linspace(min(t_bereich3),max(t_bereich3),1000)
##ax1.plot(x,(m_fit3 * x + b_fit3),linestyle ='-',label = 'regression 3',markersize = 5,linewidth = 5)
#def error(a,b):
#    ax1.errorbar(zeit[a:b], lnn[a:b],linestyle='none',errorevery=20, yerr=lns[a:b], fmt='o', markersize=0.4, color='black', linewidth=0.5,capsize=3,label='Messwerte')
#
#def linear(x,a,b):
#    return a*x+b
#
#def fit(slice,b):
#    popt, pcov = curve_fit(linear, zeit[slice:b], lnn[slice:b], sigma=lns[slice:b])
#
#    m_fit1 = popt[0]
#    m_fehler1 = np.sqrt(pcov[0,0]) # Standardabweichung der Steigung
#    b_fit1 = popt[1]
#    print(f"Steigung leckrate 1: {m_fit1:.2e} +/- {m_fehler1:.1e}")
#    x = np.linspace(slice-2,b+10,1000)
#    ax1.plot(x,m_fit1 * x + b_fit1)
#    return(ufloat(m_fit1,m_fehler1))
#
#ergebnis= fit(0,12)
#
#ax1.grid()
#error(0,100)
#ax1.legend()
#fig.savefig('build/turboevakuierung.pdf')
#
#V = ufloat(33,0.1*33)
#saug = - V * ergebnis
#print(saug)
#
#print(33*0.1)
#print(3.52*10**-6*0.3)
#print(5*0.3)
#
#df = pd.DataFrame(
#    {
#        "zeit": zeit,
#        "druck": druck,
#        "fehler": fgesamt,
#        "ln": lnn,
#        "lnfehler": lns
#    }
#)
#df.iloc[::10].to_csv("build/messdatendruck.csv", index=False, sep=';', encoding='utf-8')






import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import pandas as pd
from scipy import stats

# 1. Daten einlesen (und korrekt den einzelnen DataFrames zuordnen!)
df1 = pd.read_csv('Daten/TPEK1/TPG_all_data_2026_04_20-PM12_57_24.csv', sep=',')
df2 = pd.read_csv('Daten/TPEK2/TPG_all_data_2026_04_20-PM01_06_54.csv', sep=',')
df3 = pd.read_csv('Daten/TPEK3/TPG_all_data_2026_04_20-PM01_15_54.csv', sep=',')
df4 = pd.read_csv('Daten/TPEK4/TPG_all_data_2026_04_20-PM01_21_30.csv', sep=',')
df5 = pd.read_csv('Daten/TPEK5/TPG_all_data_2026_04_20-PM01_28_16.csv', sep=',')

def druckFehler(a):
    if a > 10:
        return 1200 * 0.03
    elif a > 2 * 10**(-3):
        return a * 0.1
    else:
        return 2 * a

def tabelle(zeit, druck, fehler, pfad):
    df = pd.DataFrame({
        'Zeit': zeit,
        'Druck': druck,
        'Fehler': fehler
    })
    df.to_csv(pfad, index=False, sep=',')

# HIER KORRIGIERT: Jetzt werden die verschiedenen DataFrames genutzt
#druck1 = df1['    TPG361_D1 [mbar]']
#druck2 = df2['    TPG361_D1 [mbar]']
cyan3 = df3['	 TPG361_D1 [mbar]'] # Temporär umbenannt für Übersicht oder direkt druck3
#druck3 = df3['    TPG361_D1 [mbar]']
#druck4 = df4['    TPG361_D1 [mbar]']
#druck5 = df5['    TPG361_D1 [mbar]']
druck1 =df1['	 TPG361_D1 [mbar]']
druck2 =df1['	 TPG361_D1 [mbar]']
druck3 =df1['	 TPG361_D1 [mbar]']
druck4 =df1['	 TPG361_D1 [mbar]']
druck5 =df1['	 TPG361_D1 [mbar]']
 #Mittelwert und statistischer Fehler (Fehler des Mittelwerts)
druck = []
druckfm = []
for i in range(len(druck1)):
    werte = [druck1[i], druck2[i], druck3[i], druck4[i], druck5[i]]
    druck.append(np.mean(werte))
    druckfm.append(stats.sem(werte))

# Systematischer Fehler & Gesamtfehler
druckfs = [druckFehler(p) for p in druck]
fgesamt = []
for i in range(len(druck1)):
    fehlergesamt = np.sqrt(druckfs[i]**2 + druckfm[i]**2)
    fgesamt.append(fehlergesamt)

# uarray für die Fehlerfortpflanzung erstellen
u_druck = unp.uarray(druck, fgesamt)

# Konstanten
pE = ufloat(3.52e-6, 0.3 * 3.52e-6)
p0 = 3.52e-3  

# Logarithmus berechnen
ln = unp.log((u_druck - pE) / (p0 - pE))
lnn = unp.nominal_values(ln)
lns = unp.std_devs(ln)

zeit = np.arange(len(druck))
tabelle(zeit, druck, fgesamt, "build/testtabelle.csv")

# Plot vorbereiten
fig, ax1 = plt.subplots()
ax1.set_title('Ausgleichsrechnung zur Bestimmung des Saugvermögens', fontsize=10)
ax1.set_xlabel('t / s')
ax1.set_ylabel(r'$\ln\frac{p - p_E}{p_0 - p_E}$')

def linear(x, a, b):
    return a * x + b

# Angepasste Fit-Funktion, die ein Label für den Plot akzeptiert
def fit(start, ende, label_name):
    popt, pcov = curve_fit(linear, zeit[start:ende], lnn[start:ende], sigma=lns[start:ende])
    
    m_fit = popt[0]
    m_fehler = np.sqrt(pcov[0,0])
    b_fit = popt[1]
    b_fehler = np.sqrt(pcov[1,1])
    
    print(f"--- Fit für Bereich {start} bis {ende} ({label_name}) ---")
    print(f"Steigung m:  {m_fit:.2e} +/- {m_fehler:.1e}")
    print(f"Achsenabschnitt b: {b_fit:.2e} +/- {b_fehler:.1e}\n")
    
    # Gerade in den Plot eintragen
    x = np.linspace(start - 2, ende + 10 if ende < len(zeit) else ende, 1000)
    ax1.plot(x, linear(x, m_fit, b_fit), linestyle='-', label=f'Fit {label_name}')
    
    return ufloat(m_fit, m_fehler)

# 1. Fit: von Wert 0 bis 12
ergebnis1 = fit(0, 12, "Bereich 1 (0-22)")

# HIER NEU: 2. Fit: von Wert 22 bis zum Ende des Arrays
ergebnis2 = fit(22, len(zeit), "Bereich 2 (22-Ende)")

# Messwerte mit Fehlerbalken einzeichnen
ax1.errorbar(zeit, lnn, linestyle='none', errorevery=20, yerr=lns, 
             fmt='o', markersize=0.4, color='black', linewidth=0.5, capsize=3, label='Messwerte')

ax1.grid()
ax1.legend()
fig.savefig('build/turboevakuierung.pdf')

# Saugvermögen für beide Bereiche berechnen
V = ufloat(33, 0.1 * 33)
saug1 = - V * ergebnis1
saug2 = - V * ergebnis2

print("--- Berechnete Saugvermögen ---")
print(f"Saugvermögen 1: {saug1}")
print(f"Saugvermögen 2: {saug2}")

# CSV-Export
df_export = pd.DataFrame({
    "zeit": zeit,
    "druck": druck,
    "fehler": fgesamt,
    "ln": lnn,
    "lnfehler": lns
})
df_export.iloc[::10].to_csv("build/messdatendruck.csv", index=False, sep=';', encoding='utf-8')


# =============================================================================
# KORREKTUR: Jetzt werden die verschiedenen DataFrames für die 5 Messungen genutzt
# =============================================================================
druck1 = df1['	 TPG361_D1 [mbar]'].reset_index(drop=True)
druck2 = df2['	 TPG361_D1 [mbar]'].reset_index(drop=True)
druck3 = df3['	 TPG361_D1 [mbar]'].reset_index(drop=True)
druck4 = df4['	 TPG361_D1 [mbar]'].reset_index(drop=True)
druck5 = df5['	 TPG361_D1 [mbar]'].reset_index(drop=True)

# Listen für Mittelwert und statistischen Fehler (SEM)
druck = []
druckfm = []

# Da die Datensätze eventuell minimal unterschiedliche Längen haben könnten, 
# sichern wir uns mit der minimalen Länge ab
min_len = min(len(druck1), len(druck2), len(druck3), len(druck4), len(druck5))

for i in range(min_len):
    werte = [druck1[i], druck2[i], druck3[i], druck4[i], druck5[i]]
    druck.append(np.mean(werte))
    # ddof=1 ist wichtig für die korrekte empirische Standardabweichung der Stichprobe
    druckfm.append(stats.sem(werte, ddof=1))

# Da wir die Arrays oben eventuell gekürzt haben, kürzen wir auch die Zeit
zeit = np.arange(min_len)

# =============================================================================
# NEU: DataFrame für den Export der 5 Einzelwerte, Mittelwert & SEM erstellen
# =============================================================================
df_uebersicht = pd.DataFrame({
    "Zeit [s]": zeit,
    "Druck 1 [mbar]": druck1[:min_len],
    "Druck 2 [mbar]": druck2[:min_len],
    "Druck 3 [mbar]": druck3[:min_len],
    "Druck 4 [mbar]": druck4[:min_len],
    "Druck 5 [mbar]": druck5[:min_len],
    "Mittelwert [mbar]": druck,
    "Stat_Fehler_SEM [mbar]": druckfm
})

# Jeden 10. Wert herausfiltern und als CSV speichern
df_uebersicht.iloc[::10].to_csv("build/druck_uebersicht_jeder_10.csv", index=False, sep=';', encoding='utf-8')

print("-> Übersichtstabelle 'build/druck_uebersicht_jeder_10.csv' erfolgreich exportiert!")