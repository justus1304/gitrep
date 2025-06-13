import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e
h = h/(2*np.pi)
a = 1
m = 1
def f(r,a):
    return np.sqrt(1/(8*a**3))*np.exp(-r/(2*a))*(-r/a+2)*1/(np.sqrt(4*np.pi))
x = np.linspace(0,20,10000)
fig, ax =plt.subplots()
#ax.plot(x,f(x,0,1),label = 't = 0, k_0 = 1')
ax.plot(x,f(x,1),color = 'red',label = 't = 0, k_0 = 2')
#ax.plot(x,f(x,0.20,0),color = 'black',label = 't = 20, k_0 = 0')
#ax.plot(x,f(x,20,3),color = 'green',label = 't = 20, k_0 = 3')
ax.legend()
ax.grid(True)
#ax.set_xscale("log")
fig.savefig("200.pdf")


