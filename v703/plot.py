import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e, e
from uncertainties import ufloat


x = np.linspace(320,640,10000)

U,I,N = np.genfromtxt("Daten/M1.txt",unpack = True)
fig, ax =plt.subplots()
ax.plot(U,N,"k.",label = 'Messwerte')

params,cov = np.polyfit(U[1:-1], N[1:-1], 1,cov=True) 
m, b = params 
m_err, b_err = np.sqrt(np.diag(cov))
print(f"Steigung: {m:.4f} ± {m_err:.4f}")
print(f"Achsenabschnitt: {b:.4f} ± {b_err:.4f}")
ax.plot(x,m * x + b)
ax.set(xlabel='U',ylabel='R')
ax.legend()
ax.grid(True)
ax.axvline(x = 560,color = 'red', linestyle='--')
fig.savefig("build/plot1.pdf")

#m = ufloat(m,m_err)
#b = ufloat(b,b_err)
#steigung = m * 100 
#print("s_1= ",steigung)

U_A = 560
z = 3632
s_2 = (z*(U_A + 50)-z*(U_A - 50)) / (z * U_A)
print("s_2= ",s_2)

Q = I/((N/60)*e)


fig2, ax =plt.subplots()
ax.plot(U,Q,"k.",label = 'Messwerte')



ax.set(xlabel='U',ylabel='Q')
ax.legend()

fig2.savefig("build/plot2.pdf")