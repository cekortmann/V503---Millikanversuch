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
    return ((9*eta*(vab-vauf))/(4*9.81*(886-1.204)))**0.5

def radius1(eta,v0):
    return np.sqrt((9*eta*v0)/(4*9.81*(886-1.204)))

def neff(n,p,r):
    return n*(1/(1+6.17*10**(-6)*1/(p*r)))

def q(n,vab,vauf,U, d):
    return 3*np.pi*n*(9*n*(vab-vauf)/(4*9.81*(886-1.204)))**0.5*(vab+vauf)/(U/d)

#def qkorr (q0, r):
#    return q0*(1+6.17*10**(-5)*133.322/(101300*r))**(-3/2)

def qkorr (q0, r):
    return q0*(1+6.17*10**(-5)/(760 * r))**(-3/2)


s= ufloat(5*10**(-4), 2*10**(-5))

t01   = ufloat(12.57,0.01)
tab11= ufloat(3.29,0.01)
tab12= ufloat(3.65,0.01)
tab13= ufloat(4.51,0.01)
tauf11 = ufloat(7.19,0.01)
tauf12 = ufloat(8.02,0.01)
tauf13 = ufloat(7.91,0.01)

t05  = ufloat(26.80,0.01)
tauf51= ufloat(5.38,0.01)
tauf52= ufloat(1.95,0.01)
tauf53= ufloat(3.5,0.01)
tab51 = ufloat(2.06,0.01)
tab52 = ufloat(2.32,0.01)
tab53 = ufloat(3.17,0.01)

t012  = ufloat(105.44,0.01)
tauf121= ufloat(5.17,0.01)
tauf122= ufloat(5.06,0.01)
tauf123= ufloat(5.19,0.01)
tab121 = ufloat(4.99,0.01)
tab122 = ufloat(4.62,0.01)
tab123 = ufloat(4.57,0.01)

t014  = ufloat(21.89,0.01)
tauf141= ufloat(8.85,0.01)  
tauf142= ufloat(8.19,0.01)
tauf143= ufloat(8.5,0.01)
tab141 = ufloat(4.55,0.01)
tab142 = ufloat(4.94,0.01)
tab143 = ufloat(4.93,0.01)

t016   = ufloat(48.65,0.01)
tauf161= ufloat(11.88,0.01)
tauf162= ufloat(10.59,0.01)
tauf163= ufloat(9.89,0.01)
tab161 = ufloat(7.72,0.01)
tab162 = ufloat(8.43,0.01)
tab163 = ufloat(7.83,0.01)

def mean(t1,t2,t3):
    return(t1+t2+t3)/3

def v(s,t):
    return s/t

tmauf1=mean(tauf11,tauf12,tauf13)
tmab1 =mean(tab11,tab12,tab13)

tmauf5=mean(tauf51,tauf52,tauf53)
tmab5 =mean(tab51,tab52,tab53)

tmauf12=mean(tauf121,tauf122,tauf123)
tmab12 =mean(tab121,tab122,tab123)

tmauf14=mean(tauf141,tauf142,tauf143)
tmab14 =mean(tab141,tab142,tab143)

tmauf16=mean(tauf161,tauf162,tauf163)
tmab16 =mean(tab161,tab162,tab163)

v01=v(s,t01)
v05=v(s,t05)
v012=v(s,t012)
v014=v(s,t014)
v016=v(s,t016)

vauf1=v(s,tmauf1)
vauf5=v(s,tmauf5)
vauf12=v(s,tmauf12)
vauf14=v(s,tmauf14)
vauf16=v(s,tmauf16)

vab1=v(s,tmab1)
vab5=v(s,tmab5)
vab12=v(s,tmab12)
vab14=v(s,tmab14)
vab16=v(s,tmab16)

vabauf1=vab1-vauf1
vabauf5=vab5-vauf5
vabauf12=vab12-vauf12
vabauf14=vab14-vauf14
vabauf16=vab16-vauf16

p=101300
du= ufloat(7.6250*10**(-3), 0.0051*10**(-3))
eta205 = 1.844*10**(-5)
eta208 = 1.840*10**(-5)
eta217 = 1.834*10**(-5)
eta220 = 1.832*10**(-5)
 
r1 = radius2(eta220, vab1, vauf1)
r5=  radius2(eta217, vab5, vauf5)
r12= radius2(eta208, vab12, vauf12)
r14 = radius2(eta205, vab14, vauf14)
r16 = radius2(eta205, vab16, vauf16)

#print('vabauf1',vabauf1)
#print('vabauf5',vabauf5)
#print('vabauf12',vabauf12)
#print('vabauf14',vabauf14)
#print('vabauf16',vabauf16)


#print('vab',vab1,vab5,vab12,vab14,vab16)
#print('vauf',vauf1,vauf5,vauf12,vauf14,vauf16)
#print('v0',v01,v05,v012,v014,v016)
print('Radius 1. Tröpfchen',radius2(eta220, vab1, vauf1))
print('Radius 5. Tröpfchen',radius2(eta217, vab5, vauf5))
print('Radius 12. Tröpfchen',radius2(eta208, vab12, vauf12))
print('Radius 14. Tröpfchen',radius2(eta205, vab14, vauf14))
print('Radius 16. Tröpfchen',radius2(eta205, vab16, vauf16))
#print('Radius 2 250V Tröpfchen 14',radius2(eta205,v251ab,v251auf))
#print('Radius 2 250V Tröpfchen 16',radius2(eta205,v252ab,v252auf))

#print('Korrigiert 14',neff(eta205,p,radius2(eta205,v251ab,v251auf)))
#print('Korrigiert 16',neff(eta205,p,radius2(eta205,v252ab,v252auf)))

print(qkorr(q(eta220, vab1, vauf1, 201, du),r1))
print(qkorr(q(eta217, vab5, vauf5, 201, du),r5))
print(qkorr(q(eta208, vab12, vauf12, 250, du),r12))
print(qkorr(q(eta205, vab14, vauf14, 250, du),r14))
print(qkorr(q(eta205, vab16, vauf16, 250, du),r16))
print('unkorrigiert')
print(q(eta220, vab1, vauf1, 201, du))
print(q(eta217, vab5, vauf5, 201, du))
print(q(eta208, vab12, vauf12, 250, du))
print(q(eta205, vab14, vauf14, 250, du))
print(q(eta205, vab16, vauf16, 250, du))

e_0 = ufloat(1.65*10**(-19), 0.06*10**(-19))

def avo(e_0):
    return 9.648*10**4/e_0

print('Avogadro', avo(e_0))