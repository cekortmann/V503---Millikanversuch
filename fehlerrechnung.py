import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  

def radius2(eta,vab,vauf):
    return np.sqrt((9*eta*(vab-vauf))/(2*9.81*(886-1.204)))

def radius1(eta,v0):
    return np.sqrt((9*eta*v0)/(2*9.81*(886-1.204)))

def neff(n,p,r):
    return n*(1/(1+6.17*1**(-5)*1/p*r))

def q(n,vab,vauf,V):
    return 3*np.pi*n*np.sqrt(9*n*(vab-vauf)/2**9.81*(886-1.204))*(vab-vauf)/(V/d)

p=101300
du= ufloat(7.6250, 0.0051)
eta205 = 1.844*10**(-5)
eta208 = 1.840*10**(-5)
eta217 = 1.834*10**(-5)
eta220 = 1.832*10**(-5)
vab = 0.2053
vauf = 0.01641

v251auf=0.0587
v251ab =0.1042
v252auf=0.0466
v252ab = 0.6027
v2510  =0.0228
v2520  =0.0103

print(radius2(eta217, vab, vauf))

#print('Radius 1 250V Tröpfchen 14',radius1(eta205,v2510))
#print('Radius 1 250V Tröpfchen 16',radius1(eta205,v2520))

print('Radius 2 250V Tröpfchen 14',radius2(eta205,v251ab,v251auf))
print('Radius 2 250V Tröpfchen 16',radius2(eta205,v252ab,v252auf))

print('Korrigiert 14',neff(eta205,p,radius2(eta205,v251ab,v251auf)))
print('Korrigiert 16',neff(eta205,p,radius2(eta205,v252ab,v252auf)))