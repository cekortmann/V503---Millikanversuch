import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import pandas as pd
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray

# Plot 1:

qc0=[1.09, 1.31, 3.15, 5.9, 9.6]
qcerr=[0.07, 0.09, 0.20, 0.4, 0.6]
def näherung(a,x,b):
    return a*x + b

e = 1.65

messwerte=[1, 1, 2, 4, 6]
x=np.linspace(0,7,100)
plt.plot(messwerte, qc0, 'x', label='Ladung nach Korrektur')
etick = [e, 2*e, 3*e, 4*e, 5*e, 6*e, 25*e, 30*e]
etickname = [r'$e$', r'$2e$', r'$3e$', r'$4e$', r'$5e$', r'$6e$', r'$25e$', r'$30e$']
plt.plot(x, 1.609*x, 'green',linewidth = 1, label='Theoriekurve mit Literaturwert', alpha = 0.5)
plt.errorbar(messwerte, qc0, yerr=qcerr, elinewidth = 0.7, color = 'blue', linewidth = 0,  markersize = 7, capsize=3)
plt.yticks(etick, etickname)
plt.xlabel(r'n Vielfache von dem GGT')
plt.ylabel(r'Ladung der Öltröpfchen in $Q \, / \, 10^{-19} \mathrm{C}$ ')
#plt.xlim(0, )
y,x = np.genfromtxt('Ladung.txt', unpack=True)
#params = curve_fit(näherung,x,y)
#a_fit = params[0][0]

para, pcov = curve_fit(näherung, x, y)
a_fit, b = para
pcov = np.sqrt(np.diag(pcov))
fa, fb = pcov
ua = ufloat(a_fit, fa) 
ub = ufloat(b, fb)
#b_fit = params[0][1]
h=np.linspace(0,7,10)
plt.plot(h, näherung(a_fit,h, b), 'orange', linewidth = 1, label = 'lineare Ausgleichskurve', alpha=0.5)
print('a_fit', ua)
print('b', ub)
#print('b_fit', b_fit)
#plt.xticks(color='w')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/Ladung.pdf', bbox_inches = "tight")
plt.clf() 