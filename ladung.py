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

qc0=[7.776,10.198, 22.059, 69.88]
qcerr=[0.005*10**(-19),0.0007*10**(-18),0.0015*10**(-18), 0.005*10**(-18)]
def näherung(a,x):
    return a*x

messwerte=[3,4,9,29]
x=np.linspace(0,30,100)
plt.plot(messwerte, qc0, 'x', label='Ladung nach Korrektur')
plt.plot(x, 1.609*x, '-', label='Theoriekurve')
plt.errorbar(messwerte, qc0, yerr=qcerr, elinewidth = 0.7, linewidth = 0, markersize = 7, capsize=3)
plt.xlabel(r'Messung der Größe nach sortiert')
plt.ylabel(r'Ladung der Öltröpfchen in $Q \, / \, 10^{-19} \mathrm{C}$ ')
#plt.xlim(0, )
y,x = np.genfromtxt('Ladung.txt', unpack=True)
params = curve_fit(näherung,x,y)
a_fit = params[0][0]
#b_fit = params[0][1]
h=np.linspace(0,30,10)
plt.plot(h, näherung(a_fit,h), 'orange', linewidth = 1, label = 'Ausgleichskurve', alpha=0.5)
print('a_fit', a_fit)
#print('b_fit', b_fit)
#plt.xticks(color='w')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/Ladung.pdf', bbox_inches = "tight")
plt.clf() 