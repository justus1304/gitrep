import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e

preis = 165
level = 4
erhoehung = 2
#Fertigungsanzahl
fertigungsanzahl = 32149
gekaufte_teile = 35000
#preise 
p_teile = 35
teile_gesamt = p_teile * gekaufte_teile
geplante_verkaufsmenge = 45000

#werbung + ansehen
werbekosten = 450000
corp_ident = 160000
werbung_gesamt = corp_ident + werbekosten

#Lagerkosten
lk_teile = 3
lk_produkte = 5
transport = 3
lager_eine_periode = (gekaufte_teile - fertigungsanzahl) * lk_teile 

#personalkosten 
pk_einkauf = 36100
pk_verwaltung = 33000
pk_fertigung = 41200
pk_betreuer = 39100

a_einkauf = 3
a_verwaltung = 2
a_fertigung = 18
a_betreuer = 10
pk_gesammt = 1.3 * (pk_einkauf * a_einkauf + a_verwaltung * pk_verwaltung + a_fertigung * pk_fertigung + a_betreuer * pk_betreuer)

#fertigungskosten
def fertigungskosten(level,erhoehung):
     return 100000*erhoehung + level * fertigungsanzahl

#Steuern

gesamtkosten = teile_gesamt + lager_eine_periode + pk_gesammt + werbung_gesamt + fertigungskosten(level,erhoehung)
einnahmen = preis * geplante_verkaufsmenge





print(gesamtkosten)
print(einnahmen)
print((einnahmen-gesamtkosten)/geplante_verkaufsmenge)