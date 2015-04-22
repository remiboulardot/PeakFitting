import csv
from matplotlib import pyplot as plt
import numpy as np
from pylab import *
from scipy import signal

fichier = np.loadtxt("AgBprofile.csv", dtype={'names': ('abscisse', 'ordonnee'), 'formats': (np.float, np.float)}, delimiter=',', skiprows=1)
#print fichier

abscisse=np.zeros(size(fichier))
ordonnee=np.zeros(size(fichier))

i=0
for ligne in fichier:
    #print ligne
    abscisse[i]=ligne[0]
    ordonnee[i]=ligne[1]
    i=i+1




#########################################################################################
#all peak finding (noise)

# print ordonnee
# list_max_ordonnee=[]
# list_max_abscisse=[]
#
# for i in range (1,size(ordonnee)-1):
#    if (ordonnee[i-1] <= ordonnee[i]) and (ordonnee[i+1] <= ordonnee[i]):
#        list_max_ordonnee.append(ordonnee[i])
#        list_max_abscisse.append(abscisse[i])

########################################################################################
#http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.signal.find_peaks_cwt.html
#peak finding without noise but lose

peakind = signal.find_peaks_cwt(ordonnee, np.arange(.1,20))
list_max_abscisse=abscisse[peakind]
list_max_ordonnee=ordonnee[peakind]

########################################################################################
#Full Width Half Max (FWHM)

HM=[]
HM=list_max_ordonnee/2
FWHM=[]

for k in range(0,size(HM)):
    y1=max(ordonnee)
    y2=max(ordonnee)
    i=0
    j=0
    while y1>=HM[k]:
        y1=ordonnee[peakind[k]-i]
        i=i+1
        if i>10: y1=0
    while y2>=HM[k]:
        y2=ordonnee[peakind[k]+j]
        j=j+1
        if j>10: y2=0
    wtps=abscisse[peakind[k]+j-1]-abscisse[peakind[k]-i+1]
    plt.axvspan(abscisse[peakind[k]+j-1], abscisse[peakind[k]-i+1], facecolor='g', alpha=1)

    if (i>10) or (j>10): wtps=0
    FWHM.append(wtps)

########################################################################################
#disp all

Result=np.zeros((size(list_max_ordonnee),3))
for i in range (0,size(list_max_ordonnee)):
   Result[i,0]=list_max_abscisse[i]
   Result[i,1]=list_max_ordonnee[i]
   Result[i,2]=FWHM[i]

fig = plt.figure(1)
plot(abscisse,ordonnee, color='blue', lw=2)
for i in range(0,size(list_max_ordonnee)-1):
    plt.axvspan(list_max_abscisse[i], list_max_abscisse[i], facecolor='b', alpha=1)
plt.show(1)

print list_max_abscisse
print list_max_ordonnee
print
print Result