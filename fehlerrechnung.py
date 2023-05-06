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

def radius(eta,vab,vauf):
    return np.sqrt((9*eta*(vab-vauf))/(2*9.81*(886-1.204)))

eta205 = 1.844*10**(-5)
eta208 = 1.840*10**(-5)
eta217 = 1.834*10**(-5)
eta220 = 1.832*10**(-5)
vab = 0.2053
vauf = 0.01641

print(radius(eta217, vab, vauf))