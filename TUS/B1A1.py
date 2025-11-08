import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.constants import c,h, m_e

def f(y,N):
    return (1+y)**(-N)
def Tf(y,N,y0):
    return ((1+y0)**(-N)-N*(1+y0)**(-N-1)*(y-y0)+(N**2+N)*(1+y0)**(-N-2)*(y-y0)**2)
def Tlnf(y,N,y0):
    return np.exp(-N*y-(N/2)*y**(2))
def Tumkehr(y,N,y0):
    return np.exp(Tlnf(y,N,y0)+N/(1+y0)*(y-y0)+N*(y-y0)**2)

y = np.linspace(0,0.1,100)
fig, ax=plt.subplots()
ax.plot(y,f(y,10),label="f(y)")
ax.plot(y,Tf(y,10,0),label="Taylor f(y)")
ax.plot(y,Tlnf(y,10,0),label="Taylor ln(f(y))")

#diference
ax.plot(y,np.abs(f(y,10)-Tf(y,10,0)),label="Abweichung Taylor")
ax.plot(y,np.abs(f(y,10)-Tlnf(y,10,0)),label="Abweichung Taylor ln")

#gittter einfügen
ax.grid(True)
#ax.plot(y,Tumkehr(y,10,0))
ax.set_xlabel("y")
ax.legend()
fig.savefig("plot1.pdf")
