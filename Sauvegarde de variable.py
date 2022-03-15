D={"pommes":21, "melons":3, "poires":31}

def add():
    global D
    a=input("clé?")
    b=input("valeur?")
    D[a]=b

def load():
    global D
    D={}
    filin = open('dict.txt','r')
    longueur=int(filin.readline())
    for i in range (longueur):
        a=(filin.readline()).split()
        b=(filin.readline()).split()
        del a [-1:-2]
        del b [-1:-2]
        a="".join(a)
        b="".join(b)
        print(a,b)
        D[a]=b
    print(D)
        

def save():
    filout = open('dict.txt','w')
    filout.write(str(len(D))+"\n")
    for cle in D:
        filout.write(cle+"\n")
        filout.write(str(D[cle])+"\n")
    
