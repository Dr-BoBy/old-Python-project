import tkinter
from tkinter import *

##################################
#Fichier de l'image a traiter
##################################
filin = open('Coco_gris.txt','r')
##################################
#ENTREE: ne pas modifier
##################################
###Lecture des informations
c = filin.readline()
print(c)
elarg=int(filin.readline())
ehaut = int(filin.readline())
d = filin.readline()

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
    tl=[]
    for j in range(elarg):
            tl.append(255)
    S.append(tl)

##################################
##################################
#TRAITEMENT: partie a modifier
##################################
##################################
### SIMPLE COPIE
lvlgris=[]
a1 =-1
b1 =-1
c1 =-1
d1 =-1
e1 =8
f1 =-1
g1 =-1
h1 =-1
i1 =-1
def FILTRE ():
    for i in range(1,ehaut-1):
        for j in range(1,elarg-1):
            S[i][j] = E[i][j]
            #EX3
            """if S[i][j]>=127:
                S[i][j]=0
            else:
                S[i][j]=255"""
            #ex4
            """if S[i][j]>=63:
                S[i][j]=255
            elif S[i][j]>=126:
                S[i][j]=170
            elif S[i][j]>=189:
                S[i][j]=85
            else:
                S[i][j]=0"""
            #ex5
            """if S[i][j]>=127:
                S[i][j]=170
            else:
                S[i][j]=85"""
            #ex6
            """S[i][j]=E[-i][j]"""
            #ex7
            """if S[i][j] not in lvlgris:
                lvlgris.append(S[i][j])
            print("l:",elarg,"h:",ehaut,len(lvlgris),"nuances de gris utilisés")"""
            #ex8
            """if S[i][j]-E[i-3][j]>=45 or S[i][j]-E[i][j-3]>=45 or S[i][j]-E[i+3][j]>=45 or S[i][j]-E[i][j+3]>=45:
                S[i][j]=0
            else:
                S[i][j]=255"""
            #matrix contour
            S[i][j]=(a1*E[i-1][j-1])+ (b1*E[i-1][j])+ (c1*E[i-1][j+1])+ (d1*E[i][j-1])+ (e1*E[i][j])+ (f1*E[i][j+1])+ (g1*E[i+1][j-1])+ (h1*E[i+1][j])+ (i1*E[i+1][j+1])
            if (a1+b1+c1+d1+e1+f1+g1+h1+i1)==0:
                dv=1
            else:
                dv=(a1+b1+c1+d1+e1+f1+g1+h1+i1)
            S[i][j]=S[i][j]/dv
            if (a1+b1+c1+d1+e1+f1+g1+h1+i1)==0:
                S[i][j]=S[i][j]+128
                S[i][j]=255-S[i][j]
    ##################################
    #SORTIE: ne pas modifier
    ##################################
    print('Sortie: appuyer sur entree puis ouvrir monimage avec GIMP')
    filout = open('monimage.txt','w')
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



##################################
#INTERFACE
##################################
traitimg=["Noir et Blanc","4 Nuances de gris","2 Nuances de gris","Methode contour 1","Methode contour 2"]
root=tkinter.Tk()
effect = sorted(traitimg)
v=StringVar()
v.set(effect[0])
effect0 = OptionMenu(root,v, *effect)
effect0.pack()
bt=tkinter.Button(root,text="Appliquer",command=FILTRE)
bt.pack()
        
root.mainloop()        
