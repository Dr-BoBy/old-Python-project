# lecture du fichier son ASCII et extraction des amplitudes et frequences dans deux listes

fichiersource = open('crapaud.dat', 'r')
fichierdestination = open('son_traite_crapaud.dat', 'w')

samplerate = fichiersource.readline()
nbcanaux = fichiersource.readline()
#print(samplerate)
#print(nbcanaux)

fichierdestination.write(samplerate)
fichierdestination.write('; Channels 1\n')

son=[]
temps=[]
amplitude=[]
indice=0

while 1:
    txt = fichiersource.readline()
    if txt == "":
        break
        #permet de stopper la boucle en fin de fichier

    son = txt.split()
    #decompose la chaine de caracteres lue en une liste de chaines successives

    temps.append(float(son[0]))
    amplitude.append(float(son[1]))

    indice=indice+1

print('lecture du fichier source terminee')
print("le nombre d'echantillons est de : " + str(indice))
print ('traitement des donnees')
input('Valider pour demarrer')

############################################################################
#   Traitement eventuel du son

tempsinitial = temps
amplitudeinitiale = amplitude

#FADIN/FADOUT
"""for i in range(len(temps)):
    if temps[i]<4:
        if float(amplitude[i])>(0.25*float(temps[i])):
            amplitude[i]=(0.25*float(temps[i]))
        if float(amplitude[i])<(-0.25*float(temps[i])):
            amplitude[i]=(-0.25*float(temps[i]))

    if temps[i]>(temps[-1]-4):
        if float(amplitude[i])>(-0.25*(float(temps[i])-(temps[-1]-4))+1):
            amplitude[i]=(-0.25*(float(temps[i])-(temps[-1]-4))+1)
        if float(amplitude[i])<(0.25*(float(temps[i])-(temps[-1]-4))-1):
            amplitude[i]=(0.25*(float(temps[i])-(temps[-1]-4))-1)"""

"""amplitude2=list(amplitude)
                 
for i in range(len(temps)):
    if i>2205:
        amplitude2[i]=0.75*(amplitude[i-2205])
    else :
        amplitude2[i]=0"""

############################################################################
print('traitement termine')
print("le nombre d'echantillons est maintenant de: " + str(len(amplitude)))
print('creation du fichier destination')

for i in range(len(temps)):
    fichierdestination.write(str(temps[i])+'    '+str(amplitude[i])+ '\n')


fichiersource.close()
fichierdestination.close()

print('fichier destination cree')
print('generation du graphique')

# generation d'un graphe a l'aide de la bibliotheque matplotlib

from matplotlib.pyplot import *
from numpy import *

nbechantillons="nombre d'echantillons : " + str(len(temps))
suptitle(nbechantillons)
echantillon=[]
for i in range (len(temps)):
    echantillon.append(i)
x1 = echantillon
y1 = amplitude

subplot(2,1,1)
xlabel('temps (s)')
ylabel('amplitude normalisee')
plot(x1,y1)

subplot(2,1,2)
x2 = tempsinitial
y2 = amplitudeinitiale

xlabel('temps (s)')
ylabel('amp ini')
plot(x2,y2)

print('generation du graphique terminee')

show()












