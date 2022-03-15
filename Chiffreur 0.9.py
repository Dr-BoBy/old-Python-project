import random

alphabet=[] 
alphabetl=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","'","0","1","2","3","4","5","6","7","8","9"]


def cpt():
    print("Phrase à coder ?" ) 
    Mot=input()
    mot=Mot.lower()
    lmot=mot.split()
    for a in range (0,len(lmot)): 
        lc=[] 
        x=lmot[a]
        for i in range(0,len(x)):
            lc.append(x[i])
        lmot[a]=list(lc)
    cle=[] 
    cle.append("#")
    alphabet=list(alphabetl)
    for i in range(0,len(lmot)+1) :
        c=random.randint(0,len(alphabetl))
        c=(alphabetl[c-1]) 
        cle.append(c)
    for b in range(0,alphabet.index(cle[1])):
        for i in range (0,len(lmot)) :
            m=list(lmot[i]) 
            for a in range(0,len(m)) :
                l=(alphabet.index(m[a])) + (alphabet.index(cle[i+1])) + 2
                while l>=len(alphabet):
                    l=l-len(alphabet)
            m[a]=alphabet[l]
            lmot[i]=list(m)
            print(cle)
        c=random.randint(0,len(alphabet)) 
        c=alphabet[c-1]
        cle.append(c)
                                  
        for a in range(2,len(cle)-1) :
            l=(alphabet.index(cle[a])) +(alphabet.index(cle[-1])) +2
            while l>=len(alphabet):
                l=l-len(alphabet)
            cle[a]=alphabet[l]
                
    for i in range(0,len(lmot)):
        m=list(lmot[i])
        m="".join(m)
        lmot[i]=m
    lmot=" ".join(lmot)
    cle[1]=str(cle[1])
    cle="".join(cle)
    print("") 
    print(cle,lmot)
            
        
def dcpt():
    print("Phrase à décoder ?" ) 
    Mot=input()
    if Mot[0]=="#":
        mot=Mot.lower()
        lmot=mot.split()
        for a in range (0,len(lmot)): 
            lc=[] 
            x=lmot[a]
            for i in range(0,len(x)):
                lc.append(x[i])
            lmot[a]=list(lc)
        cle=lmot[0]
        del lmot[0]  
        alphabet=list(alphabetl)
        for b in range (0,alphabet.index(cle[1])):
            for a in range(2,len(cle)) :
                l=(alphabet.index(cle[a])) - (alphabet.index(cle[-1]))-2
                while l<0:
                    l=l+len(alphabet)
                cle[a]=alphabet[l]
            del cle[-1]
            for i in range (0,len(lmot)) :
                m=list(lmot[i]) 
                for a in range(0,len(m)) :
                    l=(alphabet.index(m[a])) - (alphabet.index(cle[i+1])) - 2
                    while l<0:
                        l=l+len(alphabet)
                    m[a]=alphabet[l]
                lmot[i]=list(m)
       
        for i in range(0,len(lmot)):
            m=list(lmot[i])
            m="".join(m)
            lmot[i]=m
        lmot=" ".join(lmot)
        print("") 
        print(lmot)
    else:
        print("") 
        print("ERROR") 
    
        
    
    
 
for i in range (0,100000):
    print("") 
    print ("Que faire ?")
    print(" ") 
    print ("Encrypter (1)") 
    print ("Décrypter (2)")
    action=input()
    if action=="1":
        cpt()
    if action=="2" : 
        dcpt() 
    else:
        continue 
