import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, e,g
v_1,v_2 = np.genfromtxt("millikan_data.txt", unpack = True)
nu = 1.81*10**(-5)
l = 76 * 10**(-9)
d = 16*10**(-3)
rho_ol = 875.3
rho_l = 1.1839
U_B = 0
def r(v_2):
    return 1.63*l / 2 + np.sqrt(l**2/4 + 18*nu*v_2/(4*g*(rho_ol - rho_l)))
def q(v_1,v_2):
    return(6*np.pi*r(v_2)*v_1*nu*(1+l/r(v_2))**(-1) + 4*np.pi*r(v_2)**3 * g*(rho_ol-rho_l))*d/400
x = np.linspace(0.4*10**(-6),1.2*10**(-6))
fig, ax =plt.subplots()
ax.plot(r(v_2),q(v_1,v_2),"k.",label = 'Meswerte')
ax.set_xlabel('r')
ax.set_ylabel('q')
def f(x,b):
    return 0 * x + b
ax.plot(x,f(x,e))
ax.plot(x,f(x,2*e),linewidth = 0.25)
ax.plot(x,f(x,3*e),linewidth = 0.25)
ax.plot(x,f(x,4*e),linewidth = 0.25)
ax.plot(x,f(x,6*e),linewidth = 0.25)
ax.plot(x,f(x,7*e),linewidth = 0.25)
ax.plot(x,f(x,8*e),linewidth = 0.25)
ax.plot(x,f(x,9*e),linewidth = 0.25)
ax.plot(x,f(x,10*e),linewidth = 0.25)
ax.plot(x,f(x,11*e),linewidth = 0.25)
ax.plot(x,f(x,12*e),linewidth = 0.25)
ax.plot(x,f(x,13*e),linewidth = 0.25)
ax.plot(x,f(x,14*e),linewidth = 0.25)
ax.plot(x,f(x,15*e),linewidth = 0.25)
ax.legend()
ax.grid(True)
#ax.set_xscale("log")
fig.savefig("plot.pdf")