
##################################
#Fichier de l'image a traiter
##################################
filin = open('Coco_couleurs.txt','r')
##################################
#ENTREE: ne pas modifier
##################################
print("Type de l'image : ")
c = filin.readline()
print(c)
print('Largeur : ')
elarg = int(filin.readline())
print(elarg)
print()
print('Hauteur : ')
ehaut = int(filin.readline())
print(ehaut)
print()
print('Couleurs : ')
d = filin.readline()
print(d)
print()
print('Transfert image en entree')
print()
###Copie des valeurs des pixels dans la matrice d'entree
E=[]
for i in range(ehaut):
    sl=[]
    c = filin.readline()
    u=0
    for j in range(len(c)):
        if (c[j] != ' ') and (c[j]!='\n'):
            u=u*10+int(c[j])
        else:
            sl.append(u)
            u = 0
    E.append(sl)
filin.close()
###Preparation de la matrice de sortie
S=[]
for i in range(ehaut):
    sl = []
    for j in range(3*elarg):
        sl.append(255)
    S.append(sl)




##################################
##################################
#TRAITEMENT: partie a modifier
##################################
##################################
###SIMPLE COPIE

for i in range(ehaut):
    for j in range(0,3*elarg,3):
        """S[i][j] = E[i][j]"""
        
        S[i][j] = E[i][j+1]
        S[i][j+1] = E[i][j+2]
        S[i][j+2] = E[i][j]
        """S[i][j] = E[i][j+2]
        S[i][j+2] = E[i][j+1]
        S[i][j+1] = E[i][j]"""


##################################
#SORTIE: ne pas modifier
##################################
print('Sortie: appuyer sur entree puis ouvrir monimage avec GIMP')
filout = open('monimage.txt','w')
filout.write('P3\n')
filout.write(str(elarg)+'\n')
filout.write(str(ehaut)+'\n')
filout.write(d)
for i in range(ehaut):
    t = ''
    for j in range(3*elarg):
        t =  t + str(S[i][j])
        t =  t + ' '
    t =  t + '\n'
    filout.write(t)
input()

