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

U1=250
U2=210
U3=190
U4=170

R1=2.15
R2=2.13
R3=2.1
R4=2.06

rhoLuft=1.204
rhoOel=886
viskoLuft=1.8575e-5
g = const.g
e = const.e
B = 6.17*10**(-5)*133.322
p = 101.325e3
d = ufloat(7.6250, 0.0051)*10**(-3)
s=0.0005

E1=U1/d
E2=U2/d
E3=U3/d
E4=U4/d
def v(t):
    t = ufloat(np.mean(t), np.std(t))
    return (s/t)

def r(v,visko):
    if v<0:
        return 0
    else:
        return unp.sqrt((9/4)*(visko/g)*(v)/(rhoOel-rhoLuft))

#def q(v, E, r,visko):
#    if r==0:
#        return 0
#    else:
#        return (3/4)*np.pi*visko*r*((v)/(E))
def q(vab,vauf,E,visko):
    return 3*np.pi*visko*unp.sqrt((9/4)*(visko/g)*(vab-vauf)/(rhoOel-rhoLuft))*(vab+vauf)/E

def qkorr(q, r):
    if q==0:
        return 0
    else:
        return q*(1+(B/(p*r)))**(3/2)


data=open('tables/11.csv')
tauf11, tab11=np.loadtxt(data, delimiter=',',unpack=True)
#vauf11=0.5e-2/tauf11
#vab11=0.5e-2/tab11
#v11=(vab11-vauf11)
#mean=np.mean(v11)
#std=np.std(v11)
#print('v11: ',v11)
#print('mean: ',mean)
#print('std: ',std )
#r11=r(ufloat(mean,std))
#q11=q(ufloat(mean,std),E1,r11)
#print('r11: ', r11)
#print('q11: ', q11)
#print(' ')

#vauf11=ufloat(np.mean(vauf11),np.std(vauf11))
#vab11=ufloat(np.mean(vab11),np.std(vab11))
#v11=vab11-vauf11
data=open('tables/12.csv')
tauf12, tab12=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/13.csv')
tauf13, tab13=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/14.csv')
tauf14, tab14=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/15.csv')
tauf15, tab15=np.loadtxt(data, delimiter=',',unpack=True)

vauf11=v(tauf11)
vab11=v(tab11)
v11=vab11-vauf11
print('vauf11: ',format(vauf11,'.2E'))
print('vab11: ', format(vab11,'.2E'))
print('v11: ',format(v11,'.2E'))
print(' ')

vauf12=v(tauf12)
vab12=v(tab12)
v12=vab12-vauf12
print('vauf12: ',format(vauf12,'.2E'))
print('vab12: ', format(vab12,'.2E'))
print('v12: ',format(v12,'.2E'))
print(' ')

vauf13=v(tauf13)
vab13=v(tab13)
v13=vab13-vauf13
print('vauf13: ',format(vauf13,'.2E'))
print('vab13: ', format(vab13,'.2E'))
print('v13: ',format(v13,'.2E'))
print(' ')

vauf14=v(tauf14)
vab14=v(tab14)
v14=vab14-vauf14
print('vauf14: ',format(vauf14,'.2E'))
print('vab14: ', format(vab14,'.2E'))
print('v14: ',format(v14,'.2E'))
print(' ')

vauf15=v(tauf15)
vab15=v(tab15)
v15=vab15-vauf15
print('vauf15: ',format(vauf15,'.2E'))
print('vab15: ',format(vab15,'.2E'))
print('v15: ',format(v15,'.2E'))
print(' ')

#2
data=open('tables/21.csv')
tauf11, tab11=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/22.csv')
tauf12, tab12=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/23.csv')
tauf13, tab13=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/24.csv')
tauf14, tab14=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/25.csv')
tauf15, tab15=np.loadtxt(data, delimiter=',',unpack=True)

vauf11=v(tauf11)
vab11=v(tab11)
v11=vab11-vauf11

print('vauf11: ',format(vauf11,'.2E'))
print('vab11: ', format(vab11,'.2E'))
print('v11: ',format(v11,'.2E'))
print(' ')

vauf12=v(tauf12)
vab12=v(tab12)
v12=vab12-vauf12
print('vauf12: ',format(vauf12,'.2E'))
print('vab12: ', format(vab12,'.2E'))
print('v12: ',format(v12,'.2E'))
print(' ')

vauf13=v(tauf13)
vab13=v(tab13)
v13=vab13-vauf13
print('vauf13: ',format(vauf13,'.2E'))
print('vab13: ', format(vab13,'.2E'))
print('v13: ',format(v13,'.2E'))
print(' ')

vauf14=v(tauf14)
vab14=v(tab14)
v14=vab14-vauf14
print('vauf14: ',format(vauf14,'.2E'))
print('vab14: ', format(vab14,'.2E'))
print('v14: ',format(v14,'.2E'))
print(' ')

vauf15=v(tauf15)
vab15=v(tab15)
v15=vab15-vauf15
print('vauf15: ',format(vauf15,'.2E'))
print('vab15: ',format(vab15,'.2E'))
print('v15: ',format(v15,'.2E'))
print(' ')

vvab7=vab12
vvauf7=vauf12
vvab9=vab14
vvauf9=vauf14
vv7=v12
vv9=v14
#3
data=open('tables/31.csv')
tauf11, tab11=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/32.csv')
tauf12, tab12=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/33.csv')
tauf13, tab13=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/34.csv')
tauf14, tab14=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/35.csv')
tauf15, tab15=np.loadtxt(data, delimiter=',',unpack=True)

vauf11=v(tauf11)
vab11=v(tab11)
v11=vab11-vauf11

vauf12=v(tauf12)
vab12=v(tab12)
v12=vab12-vauf12

vauf13=v(tauf13)
vab13=v(tab13)
v13=vab13-vauf13

vauf14=v(tauf14)
vab14=v(tab14)
v14=vab14-vauf14

vauf15=v(tauf15)
vab15=v(tab15)
v15=vab15-vauf15

print('vauf11: ',format(vauf11,'.2E'))
print('vauf12: ',format(vauf12,'.2E'))
print('vauf13: ',format(vauf13,'.2E'))
print('vauf14: ',format(vauf14,'.2E'))
print('vauf15: ',format(vauf15,'.2E'))

print(' ')
print('vab11: ', format(vab11,'.2E'))
print('vab12: ', format(vab12,'.2E'))
print('vab13: ', format(vab13,'.2E'))
print('vab14: ', format(vab14,'.2E'))
print('vab15: ',format(vab15,'.2E'))

print(' ')
print('v11: ',format(v11,'.2E'))
print('v12: ',format(v12,'.2E'))
print('v13: ',format(v13,'.2E'))
print('v14: ',format(v14,'.2E'))
print('v15: ',format(v15,'.2E'))
vvab14=vab14
vvauf14=vauf14
vvauf15=vauf15
vvab15=vab15
vv14=v14
vv15=v15
#4
data=open('tables/41.csv')
tauf11, tab11=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/42.csv')
tauf12, tab12=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/43.csv')
tauf13, tab13=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/44.csv')
tauf14, tab14=np.loadtxt(data, delimiter=',',unpack=True)
data=open('tables/45.csv')
tauf15, tab15=np.loadtxt(data, delimiter=',',unpack=True)

vauf11=v(tauf11)
vab11=v(tab11)
v11=vab11-vauf11

vauf12=v(tauf12)
vab12=v(tab12)
v12=vab12-vauf12

vauf13=v(tauf13)
vab13=v(tab13)
v13=vab13-vauf13

vauf14=v(tauf14)
vab14=v(tab14)
v14=vab14-vauf14

vauf15=v(tauf15)
vab15=v(tab15)
v15=vab15-vauf15

vvab17=vab12
vvauf17=vauf12
vv17=v12
print('vauf11: ',format(vauf11,'.2E'))
print('vauf12: ',format(vauf12,'.2E'))
print('vauf13: ',format(vauf13,'.2E'))
print('vauf14: ',format(vauf14,'.2E'))
print('vauf15: ',format(vauf15,'.2E'))

print(' ')
print('vab11: ', format(vab11,'.2E'))
print('vab12: ', format(vab12,'.2E'))
print('vab13: ', format(vab13,'.2E'))
print('vab14: ', format(vab14,'.2E'))
print('vab15: ',format(vab15,'.2E'))

print(' ')
print('v11: ',format(v11,'.2E'))
print('v12: ',format(v12,'.2E'))
print('v13: ',format(v13,'.2E'))
print('v14: ',format(v14,'.2E'))
print('v15: ',format(v15,'.2E'))
print('')

#r uns q
print(vv7,vv9,vv14,vv15,vv17)
r7=r(vv7,1.835e-5)
r9=r(vv9,1.835e-5)
r14=r(vv14,1.838e-5)
r15=r(vv15,1.842e-5)
r17=r(vv17,1.844e-5)
print('r7: ',r7)
print('r9: ',r9)
print('r14: ',r14)
print('r15: ',r15)
print('r17: ',r17)

#q7=q(vv7,E2,r7,1.835e-5)
#q9=q(vv9,E2,r9,1.835e-5)
#q14=q(vv14,E3,r14,1.838e-5)
#q15=q(vv15,E3,r15,1.842e-5)
#q17=q(vv17,E4,r17,1.844e-5)
#
#print('q7: ',q7)
#print('q9: ',q9)
#print('q14: ',q14)
#print('q15: ',q15)
#print('q17: ',q17)

#q2
q7=q(vvab7,vvauf7,E2,1.835e-5)
q9=q(vvab9,vvauf9,E2,1.835e-5)
q14=q(vvab14,vvauf14,E3,1.838e-5)
q15=q(vvab15,vvauf15,E3,1.842e-5)
q17=q(vvab17,vvauf17,E4,1.844e-5)

print('q7neu: ',q7)
print('q9neu: ',q9)
print('q14neu: ',q14)
print('q15neu: ',q15)
print('q17neu: ',q17)

#qcorr
qc7=qkorr(q7,r7)
qc9=qkorr(q9,r9)
qc14=qkorr(q14,r14)
qc15=qkorr(q15,r15)
qc17=qkorr(q17,r17)

print('qc7: ',qc7)
print('qc9: ',qc9)
print('qc14: ',qc14)
print('qc15: ',qc15)
print('qc17: ',qc17)

#plot
q0=[unp.nominal_values(q7),unp.nominal_values(q9),unp.nominal_values(q14)
,unp.nominal_values(q15),unp.nominal_values(q17)]
qerr=[unp.std_devs(q7),unp.std_devs(q9),unp.std_devs(q14)
,unp.std_devs(q15),unp.std_devs(q17)]

qc0=[unp.nominal_values(qc7),unp.nominal_values(qc9),unp.nominal_values(qc14)
,unp.nominal_values(qc15),unp.nominal_values(qc17)]
qcerr=[unp.std_devs(qc7),unp.std_devs(qc9),unp.std_devs(qc14)
,unp.std_devs(qc15),unp.std_devs(qc17)]

messwerte=[1,2,3,4,5]
print(qc0)
etick = [0, e, 2*e, 3*e, 4*e, 5*e]
etickname = [r'$0$', r'$e$', r'$2e$', r'$3e$', r'$4e$', r'$5e$']
plt.plot(messwerte, qc0, 'x', label='Ladung nach Korrektur')
plt.errorbar(messwerte, qc0, yerr=qcerr, elinewidth = 0.7, linewidth = 0, markersize = 7, capsize=3)
plt.xlabel('Messung')
plt.xlim(0, 6)
plt.yticks(etick, etickname)
plt.grid()
plt.legend(loc='best')

#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.show()
plt.savefig('pictures/plot1.pdf')
plt.close()

#e berechnen
e3=((q7+q9)/2)
e4=q14
e2=q17
e5=q15

e3c=((qc7+qc9)/2)
e4c=qc14
e2c=qc17
e5c=qc15

#print('3e: ',e3)
#print('4e: ',e4)
#print('2e: ',e2)
#
#print('3ec: ',e3c)
#print('4ec: ',e4c)
#print('2ec: ',e2c)

e=(e3/3+e4/4+e2/2+e5/5)/4
ec=(e3c/3+e4c/4+e2c/2+e5c/5)/4
print('e: ',e)
print('ec: ',ec)
a=96485.34/ec
alit=6.022e23
print('avogardo ',a)
#fehler
print(format((a-alit)/alit,'.2E'))
elit=1.60217e-19
f=(e-elit)/elit *100
fc=(ec-elit)/elit *100
print(f,fc)
#korrektur
diff1=e5-e4
diff2=e4-e3
diff3=e3-e2
en=(diff1+diff2+diff3)/3
print('en: ',format(en,'.2E'))

diff1c=e5c-e4c
diff2c=e4c-e3c
diff3c=e3c-e2c
enc=(diff1c+diff2c+diff3c)/3
print('enc: ',format(enc,'.2E'))

ac=96485.34/enc
alit=6.022e23
print('avogardoc ',format(ac,'.2E'))
#fehler
print(format((ac-alit)/alit*100,'.5'))
elit=1.60217e-19
f=(en-elit)/elit *100
fc=(enc-elit)/elit *100
print(format(f,'.2E'),format(fc,'.2E'))

print(qerr)