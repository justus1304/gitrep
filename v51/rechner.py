from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp
from scipy.stats import sem

# Schmitt-Trigger
U_k = ufloat(1.368,0.001)
U_grenze_exp = U_k * 2
print(f"Wert die experimentell bestimmte U_grenz: {U_grenze_exp.nominal_value} ± {U_grenze_exp.std_dev}")

U_S = 15
R1 = 10
R2 = 100
U_grenze_theo =  U_S * R1 / (R1 + R2)
print(f"Wert die theoretisch bestimmte U_grenz: {U_grenze_theo:.3f}") 
# print(f"Wert die experimentell bestimmte U_grenz: {U_grenze_theo.nominal_value} ± {U_grenze_theo.std_dev}")