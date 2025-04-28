import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e
h = h/(2*np.pi)
a = 1
m = 1
def f(x,t,k_0):
    return np.sqrt((((a / (2 * np.pi))**(1/4) / np.sqrt((a/2) + (1j * h * t)/m)) * np.exp(-(a * (x - (k_0 * h * t) / m))**2 / (a**2 + (4*h**2 *t**2) / m**2)) * np.exp(1j*(((2*h*t*x / m +a**2 * k_0)*x - a**2 * k_0**2 * h * t /(2*m))/ (a**2 + 4 * h**2 * t**2 / m**2)))).real**2 + ((((a / (2 * np.pi))**(1/4) / np.sqrt((a/2) + (1j * h * t)/m)) * np.exp(-(a * (x - (k_0 * h * t) / m))**2 / (a**2 + (4*h**2 *t**2) / m**2)) * np.exp(1j*(((2*h*t*x / m +a**2 * k_0)*x - a**2 * k_0**2 * h * t /(2*m))/ (a**2 + 4 * h**2 * t**2 / m**2)))).imag)**2)

x = np.linspace(-20,20,10000)
fig, ax =plt.subplots()
#ax.plot(x,f(x,0,1),label = 't = 0, k_0 = 1')
ax.plot(x,f(x,0,2),color = 'red',label = 't = 0, k_0 = 2')
ax.plot(x,f(x,0.20,0),color = 'black',label = 't = 20, k_0 = 0')
#ax.plot(x,f(x,20,3),color = 'green',label = 't = 20, k_0 = 3')
ax.legend()
#ax.set_xscale("log")
fig.savefig("plot.pdf")


