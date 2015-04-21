import csv
from matplotlib import pyplot as plt
import numpy as np
from pylab import *

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


fig = plt.figure(1)
plot(abscisse,ordonnee, color='blue', lw=2)
#plt.show(1)


#print ordonnee

list_max_ordonnee=[]
list_max_abscisse=[]

for i in range (1,size(ordonnee)-1):
    if (ordonnee[i-1] <= ordonnee[i]) and (ordonnee[i+1] <= ordonnee[i]):
        list_max_ordonnee.append(ordonnee[i])
        list_max_abscisse.append(abscisse[i])

pos_max=np.zeros((size(list_max_ordonnee)-1,2))
for i in range (0,size(list_max_ordonnee)-1):
    pos_max[i,0]=list_max_abscisse[i]
    pos_max[i,1]=list_max_ordonnee[i]

print list_max_abscisse
print list_max_ordonnee
print pos_max