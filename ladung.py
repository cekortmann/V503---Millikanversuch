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

qc0=[2.2059*10**(-18), 1.0198*10**(-18), 7.776*10**(-19), 6.988*10**(-18)]
qcerr=[0.0015*10**(-18), 0.0007*10**(-18), 0.005*10**(-19), 0.005*10**(-18)]

messwerte=[1,2,3,4]
plt.plot(messwerte, qc0, 'x', label='Ladung nach Korrektur')
plt.errorbar(messwerte, qc0, yerr=qcerr, elinewidth = 0.7, linewidth = 0, markersize = 7, capsize=3)
plt.xlabel('Messung')
plt.xlim(0, 5)
plt.xticks(color='w')
plt.grid()
plt.legend(loc='best')

plt.savefig('build/Ladung.pdf', bbox_inches = "tight")
plt.clf() 
