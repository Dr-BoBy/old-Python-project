##################################
#Fichier de l'image a traiter
##################################
filin = open('tmt.pgm','r')
##################################
#ENTREE: ne pas modifier
##################################
###Lecture des informations
print("Type de l'image : ")
c = filin.readline()
print(c)
elarg=int(filin.readline())
print('Largeur : ')
print(elarg)
print()
ehaut = int(filin.readline())
print('Hauteur : ')
print(ehaut)
print()
d = filin.readline()
print('Niveaux de gris : ')
print(d)
print()
print('Transfert image en entree')
print()
###Copie des valeurs des pixels dans la matrice d'entree
E=[]
S2=[]
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
    S2=S2+sl
filin.close()
###Preparation de la matrice de sortie
S=[]
for i in range(ehaut):
    tl=[]
    for j in range(ehaut):
            tl.append(255)
    S.append(tl)




##################################
##################################
#TRAITEMENT: partie a modifier
##################################
##################################
### SIMPLE COPIE
lvlgris=[]
S2=[]
S3=[]
tempo=[]

"""for i in range(ehaut):
    for j in range(len(E[i])):
        S2.append(E[i][j])"""
    
for i in range (0,len(S2)):
    if len(tempo)<225:
        tempo.append(S2[i])
    else:
        S3.append(tempo)
        tempo=[]
        
print(len(S3))
print(len(S2))
    
        
        

    
        
##################################
#SORTIE: ne pas modifier
##################################
print('Sortie: appuyer sur entree puis ouvrir monimage avec GIMP')
filout = open('monimage.txt','w')
filout2 = open('test.txt','w')
filout.write('P2\n')
filout.write(str(elarg)+'\n')
filout.write(str(ehaut)+'\n')
filout.write(d)
for i in range(ehaut):
    t = ''
    for j in range(elarg):
        t =  t + str(S[i][j])
        t =  t + ' '
    t =  t + '\n'
    filout.write(t) 
filout.close()
input()
