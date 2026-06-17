import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import legendre


import pandas as pd
daten = pd.read_csv('deine_datei.dat', sep='\s+', header=None)

spalte_1 = daten[0]
spalte_2 = daten[1]

def einlesen(datei):
    daten = pd.read_csv(datei, sep='\s+', header=None)

    spalte_1 = daten[0]
    spalte_2 = daten[1]
    return spalte_1,spalte_2