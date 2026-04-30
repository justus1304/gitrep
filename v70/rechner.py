from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem
import panda as pd
## Lädt die Originaldatei (beachtet die Tabs nach den Kommas)
#df = pd.read_csv('Daten/DPEK/TPG_all_data_2026_04_20-PM03_43_33.csv', sep=',\t', engine='python')
#
## Wählt nur die Druckspalten aus
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#
## Speichert es als saubere .txt Datei für genfromtxt
#pressures.to_csv('meineDaten/DPEK.txt', sep='\t', index=False, header=False)
#
#print("Datei 'meineDaten/pressure_data.txt' wurde erstellt!")
#
#
## Drehschieberpumpe Leckratenmessungen 
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/DPLR1/TPG_all_data_2026_04_20-PM04_14_00.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/DPLR1.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/DPLR2/TPG_all_data_2026_04_20-PM04_33_53.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/DPLR2.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/DPLR3/TPG_all_data_2026_04_20-PM04_53_22.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/DPLR3.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/DPLR41/TPG_all_data_2026_04_20-PM05_02_36.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/DPLR41.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/DPLR42/TPG_all_data_2026_04_20-PM05_11_52.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/DPLR42.txt', sep='\t', index=False, header=False)
#
##Turbopumpe Evakuierungskurve
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPEK1/TPG_all_data_2026_04_20-PM12_57_24.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPEK1.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPEK2/TPG_all_data_2026_04_20-PM01_06_54.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPEK2.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPEK3/TPG_all_data_2026_04_20-PM01_15_54.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPEK3.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPEK4/TPG_all_data_2026_04_20-PM01_21_30.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPEK4.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPEK5/TPG_all_data_2026_04_20-PM01_28_16.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPEK5.txt', sep='\t', index=False, header=False)
#
##Turbopumpe Leckraten
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPLR1/TPG_all_data_2026_04_20-PM01_39_18.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPLR1.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPLR2/TPG_all_data_2026_04_20-PM01_49_18.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPLR2.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPLR3/TPG_all_data_2026_04_20-PM01_49_18.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPLR3.txt', sep='\t', index=False, header=False)
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/TPLR4/TPG_all_data_2026_04_20-PM01_58_31.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/TPLR4.txt', sep='\t', index=False, header=False)
#
#
#
#df = pd.read_csv('/home/justus/gitrep/v70/Daten/Letzte/TPG_all_data_2026_04_20-PM05_41_21.csv', sep=',\t', engine='python')
#pressures = df[[' TPG202 [mbar]', ' TPG361_D1 [mbar]', ' TPG361_D2 [mbar]']]
#pressures.to_csv('meineDaten/letzte.txt', sep='\t', index=False, header=False)
#
#
#
#