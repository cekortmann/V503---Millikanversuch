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
    return np.sqrt((9*eta*(vab-vauf))/(4*9.81*(886-1.204)))

def radius1(eta,v0):
    return np.sqrt((9*eta*v0)/(4*9.81*(886-1.204)))

def neff(n,p,r):
    return n*(1/(1+6.17*10**(-6)*1/(p*r)))

def q(n,vab,vauf,U, d):
    return 3*np.pi*n*np.sqrt(9*n*(vab-vauf)/(4*9.81*(886-1.204)))*(vab+vauf)/(U/d)

def qkorr (q0, r):
    return q0*(1+6.17*10**(-5)*133.322/(101300*r))**(3/2)


r1 = 1.6723 * 10**(-7)
r5=  2.9967 *10**(-7)
r14 = 1.4748 * 10**(-7)
r16 = 5.1558*10**(-7)



p=101300
du= ufloat(7.6250*10**(-3), 0.0051*10**(-3))
eta205 = 1.844*10**(-5)
eta208 = 1.840*10**(-5)
eta217 = 1.834*10**(-5)
eta220 = 1.832*10**(-5)
vab1= 0.2053*10**(-3)
vauf1 = 0.14641*10**(-3)
vab5 = 0.1333*10**(-3)
vauf5 = 0.0065*10**(-3)

v251auf=0.0587*10**(-3)
v251ab =0.1042*10**(-3)
v252auf=0.0466*10**(-3)
v252ab = 0.6027*10**(-3)
v2510  =0.0228*10**(-3)
v2520  =0.0103*10**(-3)

#print(radius2(eta220, vab1, vauf1))

#print('Radius 1 250V Tröpfchen 14',radius1(eta205,v2510))
#print('Radius 1 250V Tröpfchen 16',radius1(eta205,v2520))

#print('Radius 2 250V Tröpfchen 14',radius2(eta205,v251ab,v251auf))
#print('Radius 2 250V Tröpfchen 16',radius2(eta205,v252ab,v252auf))

#print('Korrigiert 14',neff(eta205,p,radius2(eta205,v251ab,v251auf)))
#print('Korrigiert 16',neff(eta205,p,radius2(eta205,v252ab,v252auf)))

print(qkorr(q(eta220, vab1, vauf1, 201, du),r1))
print(qkorr(q(eta217, vab5, vauf5, 201, du),r5))
print(qkorr(q(eta205, v251ab, v251auf, 250, du),r14))
print(qkorr(q(eta205, v252ab, v252auf, 250, du),r16))
print('unkorrigiert')
print(q(eta220, vab1, vauf1, 201, du))
print(q(eta217, vab5, vauf5, 201, du))
print(q(eta205, v251ab, v251auf, 250, du))
print(q(eta205, v252ab, v252auf, 250, du))