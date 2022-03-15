##################################
#Fichier de l'image a traiter
##################################
filin = open('Coco_noir.txt','r')
##################################
#ENTREE: ne pas modifier
##################################
###Lecture des informations de l'image
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
print(' ')
print('Transfert image en entree')
print()
###Copie des valeurs des pixels dans la matrice d'entree
E=[]
for i in range(ehaut):
    sl=[]
    c = filin.readline()
    #print(c)
    for j in range(len(c)):
        if (c[j] != ' ') and (c[j]!='\n'):
            sl.append(int(c[j]))
    E.append(sl)
filin.close()
###Preparation de la matrice de sortie
S=[]
for i in range(ehaut):
    sl = []
    for j in range(elarg):
        sl.append(0)
    S.append(sl)







##################################
##################################
#TRAITEMENT: partir a modifier
##################################
##################################
###SIMPLE COPIE
for i in range(ehaut):
    for j in range(elarg):
        S[i][j] = E[i][j]


    
##################################
#SORTIE: ne pas modifier
##################################
print('Sortie: appuyer sur entree puis ouvrir monimage avec GIMP')
filout = open('monimage4.txt','w')
filout.write('P1\n')
filout.write(str(elarg)+'\n')
filout.write(str(ehaut)+'\n')
for i in range(ehaut):
    t = ''
    for j in range(elarg):
        t =  t + str(S[i][j])
        t =  t + ' '
    t =  t + '\n'
    filout.write(t)
    #print(t)
filout.close()
input()
