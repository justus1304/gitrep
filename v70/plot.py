import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
#import pandas as pd
from uncertainties import unumpy as unp  # Add this line
from scipy.optimize import curve_fit
pirani,leit1,leit2 = np.genfromtxt('meineDaten/DPEK.txt', unpack = True)


""" # fehler der drücke bestimmen 
def druckFehler(a):
    fehlerListe = []
    i = 0
    for x in a:
        
        if (a[i] > 10):
            fehlerListe.append(1200 * 0.03)
        else:
            if(a[i] > 2*10**(-3)):
                fehlerListe.append(a[i]*0.1)
            else :
                    fehlerListe.append(2*a[i])
        i = i + 1
    return fehlerListe """
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

#ln bestimmen 
def logarithmus(p,pE,p0):
    return unp.log((p-pE)/(p0-pE))


#tabele erstellen 
liste = []
for i in range(len(pirani)-1):
    zeile = []
    wert = ufloat(pirani[i], druckFehler(pirani[i]))
    zeile.append(i+1)
    zeile.append(wert)
    zeile.append(logarithmus(wert,ufloat(0.02,0),ufloat(1007,0)))
    liste.append(zeile)
i = 0
for eintrag in liste:
    # :P steht für die "Standard-Physik-Formatierung" (z.B. 1.234(56))
    if(i == 0 or i % 10 == 0):
        print(eintrag[0],f"Druck: {eintrag[1]:.2uP}, Log: {eintrag[2]:.2uP}")
    i = i +1
zeit = [eintrag[0] for eintrag in liste]
y_werte = [np.asarray(eintrag[2]).item().n for eintrag in liste]
y_fehler = [np.asarray(eintrag[2]).item().s for eintrag in liste]
#np.savetxt("drehschieberevak.txt", liste, fmt="%d", delimiter=",")
#die 3 bereiche fitten
def linear(t,m,b):
    return(t*m+b)
# Regression durchführen
# sigma übergibt die Fehlerbalken an den Fit-Algorithmus
t_bereich1 = [e[0] for e in liste[0:150]]
y_bereich1 = [np.asarray(e[2]).item().n for e in liste[0:150]]
sigma_bereich1 = [np.asarray(e[2]).item().s for e in liste[0:150]]
popt, pcov = curve_fit(linear, t_bereich1, y_bereich1, sigma=sigma_bereich1)

m_fit1 = popt[0]
m_fehler1 = np.sqrt(pcov[0,0]) # Standardabweichung der Steigung
b_fit1 = popt[1]
print(f"Steigung: {m_fit1:.5f} +/- {m_fehler1:.5f}")

##Bereich 2!!
t_bereich2 = [e[0] for e in liste[150:290]]
y_bereich2 = [np.asarray(e[2]).item().n for e in liste[150:290]]
sigma_bereich2 = [np.asarray(e[2]).item().s for e in liste[150:290]]
popt2, pcov2 = curve_fit(linear, t_bereich2, y_bereich2, sigma=sigma_bereich2)

m_fit2 = popt2[0]
m_fehler2 = np.sqrt(pcov2[0,0]) # Standardabweichung der Steigung
b_fit2 = popt2[1]
print(f"Steigung: {m_fit2:.5f} +/- {m_fehler2:.5f}")


##Bereich 3 !!
t_bereich3 = [e[0] for e in liste[290:599]]
y_bereich3 = [np.asarray(e[2]).item().n for e in liste[290:599]]
sigma_bereich3 = [np.asarray(e[2]).item().s for e in liste[290:599]]
popt3, pcov3 = curve_fit(linear, t_bereich3, y_bereich3, sigma=sigma_bereich3)

m_fit3 = popt3[0]
m_fehler3 = np.sqrt(pcov3[0,0]) # Standardabweichung der Steigung
b_fit3 = popt3[1]
print(f"Steigung: {m_fit3:.5f} +/- {m_fehler3:.5f}")

fig, ax1 = plt.subplots()
ax1.set_title('Ausgleichsrechnung zur bestimmung des Saugvermögens mit der Evakuierungskurve',fontsize = 1)
ax1.set_xlabel('t/s')
ax1.set_ylabel(r'$\ln\frac{p - p_E}{p_0 - p_E}$') 
#ax1.plot(zeit,y_werte,linestyle='',fmt ='o')
x = np.linspace(min(t_bereich1),max(t_bereich1),1000)
ax1.plot(x,(m_fit1 * x + b_fit1),linestyle ='-',label = 'regression 1',markersize = 5,linewidth = 5)

x = np.linspace(min(t_bereich2),max(t_bereich2),1000)
ax1.plot(x,(m_fit2 * x + b_fit2),linestyle ='-',label = 'regression 2',markersize = 5,linewidth = 5)

x = np.linspace(min(t_bereich3),max(t_bereich3),1000)
ax1.plot(x,(m_fit3 * x + b_fit3),linestyle ='-',label = 'regression 3',markersize = 5,linewidth = 5)

ax1.errorbar(zeit, y_werte,linestyle='none',errorevery=20, yerr=y_fehler, fmt='o', markersize=0.4, color='black', linewidth=0.5,capsize=3)
ax1.legend()
fig.savefig('build/ersteKurve')


V = ufloat(33,0.1*33)
saug1 = - V * ufloat(m_fit1,m_fehler1)
print(saug1)

saug2 = - V * ufloat(m_fit2,m_fehler2)
print(saug2)

saug3 = - V * ufloat(m_fit3,m_fehler3)
print(saug3)

print(saug1*3.6)
print(saug2*3.6)
print(saug3*3.6)
#fehler_array = np.array(druckFehler(a))
#
## Zeit, Druck und Fehler in Spalten nebeneinander legen
## a, b, c sind deine eingelesenen Daten aus np.genfromtxt
#export_daten = np.column_stack((liste[0], liste[1], liste[2]))
##
### Als Textdatei speichern
#np.savetxt('meineDaten/ergebnisse_fehler.txt', export_daten, 
#           header='Druck[mbar] Zeit[s] Fehler[mbar]', 
#           fmt='%.5e', delimiter='\t')







