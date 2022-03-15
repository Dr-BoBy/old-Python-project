
def cod():
    me2=[]
    me3=[]
    X1="a"
    X2="b"
    X3="c"
    X4="d"
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    L=[L1,L2,L3,L4]
    #Création de la liste
    me=input("Message envoyé (en bits) :\n")
    if len(me)!=7:
        print("error")
    else:
        me=list(me)
        for i in range(len(me)):
            me[i]=int(me[i])
        #ajout de X1 X2 X3 X4
        me2.append(X4)
        me2.append(X3)
        me2.append(me[0])
        me2.append(X2)
        me2.append(me[1])
        me2.append(me[2])
        me2.append(me[3])
        me2.append(X1)
        me2.append(me[4])
        me2.append(me[5])
        me2.append(me[6])
        #création X1 X2 X3 X4
        for i in range(len(me2)):
            if me2[i]==1:
                X=list(bin(i+1))
                del X[0:2]
                X.reverse()
                while len(X)<=3:
                    X.append(0)
                X.reverse()
                for i in range(len(X)):
                    X[i]=int(X[i])
                for i in range(len(X)):
                    L[i].append(X[i])
        a=0
        for i in range (len(L1)):
            a+=L1[i]
            if a%2==0:
                X1=0
            else:
                X1=1
        a=0
        for i in range (len(L1)):
            a+=L2[i]
            if a%2==0:
                X2=0
            else:
                X2=1
        a=0
        for i in range (len(L1)):
            a+=L3[i]
            if a%2==0:
                X3=0
            else:
                X3=1
        a=0
        for i in range (len(L1)):
            a+=L4[i]
            if a%2==0:
                X4=0
            else:
                X4=1
        me3.append(X4)
        me3.append(X3)
        me3.append(me[0])
        me3.append(X2)
        me3.append(me[1])
        me3.append(me[2])
        me3.append(me[3])
        me3.append(X1)
        me3.append(me[4])
        me3.append(me[5])
        me3.append(me[6])
        for i in range(len(me3)):
            me3[i]=str(me3[i])
        me3="".join(me3)
        print(me3)

def decod():
    X1="a"
    X2="b"
    X3="c"
    X4="d"
    L1=[]
    L2=[]
    L3=[]
    L4=[]
    L=[L1,L2,L3,L4]
    #Création de la liste
    me=input("Message reçu (en bits) :\n")
    if len(me)!=11:
        print("error")
    else:
        me=list(me)
        for i in range(len(me)):
            me[i]=int(me[i])
        for i in range(len(me)):
                if me[i]==1:
                    X=list(bin(i+1))
                    del X[0:2]
                    X.reverse()
                    while len(X)<=3:
                        X.append(0)
                    X.reverse()
                    for i in range(len(X)):
                        X[i]=int(X[i])
                    for i in range(len(X)):
                        L[i].append(X[i])
        a=0
        for i in range (len(L1)):
            a+=L1[i]
            if a%2==0:
                X1=0
            else:
                    X1=1
        a=0
        for i in range (len(L1)):
            a+=L2[i]
            if a%2==0:
                X2=0
            else:
                X2=1
        a=0
        for i in range (len(L1)):
            a+=L3[i]
            if a%2==0:
                X3=0
            else:
                X3=1
        a=0
        for i in range (len(L1)):
            a+=L4[i]
            if a%2==0:
                X4=0
            else:
                X4=1
        if X1!=0 or X2!=0 or X3!=0 or X4!=0:
            L1=[]
            L2=[]
            L3=[]
            L4=[]
            L=[L1,L2,L3,L4]
            print(X1,X2,X3,X4)
            print("Une erreur est survenue")
            print("Tentative détection d\'erreur...")
            b=[str(X1),str(X2),str(X3),str(X4)]
            b="".join(b)
            me4=list(me)
            b=int(b,2)-1
            print("Erreur au bit",b)
            if me4[b]==1:
                me4[b]=0
            else:
                me4[b]=1
            me4=list(me4)
            for i in range(len(me4)):
                me4[i]=int(me4[i])
            for i in range(len(me4)):
                    if me4[i]==1:
                        X=list(bin(i+1))
                        del X[0:2]
                        X.reverse()
                        while len(X)<=3:
                            X.append(0)
                        X.reverse()
                        for i in range(len(X)):
                            X[i]=int(X[i])
                        for i in range(len(X)):
                            L[i].append(X[i])
            a=0
            for i in range (len(L1)):
                a+=L1[i]
                if a%2==0:
                    X1=0
                else:
                        X1=1
            a=0
            for i in range (len(L1)):
                a+=L2[i]
                if a%2==0:
                    X2=0
                else:
                    X2=1
            a=0
            for i in range (len(L1)):
                a+=L3[i]
                if a%2==0:
                    X3=0
                else:
                    X3=1
            a=0
            for i in range (len(L1)):
                a+=L4[i]
                if a%2==0:
                    X4=0
                else:
                    X4=1
            if X1==0 and X2==0 and X3==0 and X4==0:
                for i in range(len(me4)):
                    me4[i]=str(me4[i])
                print("Message correcte potentiellement reçu :\n","".join(me4))
        else:
            print("Le message à été reçu avec succès")

for i in range(0,1000):
    action=input("Que souhaitez vous faire :\nCodage Hammming (1)\nDecodage Hamming (2)\n")
    if action=="1":
        cod()
    if action=="2":
        decod()

    
    
    
        
    
    

    
