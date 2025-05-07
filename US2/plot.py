import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e, e
from uncertainties import ufloat

x = np.linspace(0.0000,0.00006,10000)

N,t_o,t_u = np.genfromtxt("daten/acryl.txt",unpack = True)
N2,y_su = np.genfromtxt("daten/leere.txt",unpack = True)
y_su = y_su * 10**(-3)
t_u = t_u * 10 **(-6)
#y_su = np.delete(y_su, -2)
#t_u = np.delete(t_u, -2)
fig, ax =plt.subplots()
ax.plot(t_u[:-2],y_su[:-2],"k.",label = 'Messwerte')

params,cov = np.polyfit(t_u[:-2], y_su[:-2], 1,cov=True) 
m, b = params 
m_err, b_err = np.sqrt(np.diag(cov))
print(f"Steigung: {m:.4f} ± {m_err:.4f}")
print(f"Achsenabschnitt: {b:.4f} ± {b_err:.4f}")
ax.plot(x,m * x + b)
ax.set(xlabel='t',ylabel='s')
ax.legend()
ax.grid(True)
#ax.axvline(x = 560,color = 'red', linestyle='--')
fig.savefig("build/plot1.pdf")

