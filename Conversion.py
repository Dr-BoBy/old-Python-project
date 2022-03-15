a=0
r=0
def dectobi(b10):
    global r
    q=b10
    r=[]
    while q>0:
        q=b10//2
        r.append(str(b10%2))
        b10=q
    r.reverse()

    r="".join(r)

def bitodec(b2):
    global r
    r=0
    b2=list(str(b2))
    b2.reverse()
    for i in range(0, len(b2)):
        if b2[i]=="1":
            r+=2**i             


def dectohex(b10):
    global r
    nombres=[10,11,12,13,14,15]
    lettres=["A","B","C","D","E","F"]
    q=b10
    r=[]
    while q>16:
        q=b10//16
        r.append(b10%16)
        b10=q
    r.append(q)
    r.reverse()
    for i in range (0,len(r)):
        if r[i]>9:
            a=nombres.index(r[i])
            r[i]=lettres[a]
        r[i]=str(r[i])
    r="".join(r)

def hextodec(b16):
    global r
    nombres=[10,11,12,13,14,15]
    lettres=["A","B","C","D","E","F"]
    r=0
    b16=list(str(b16))
    b16.reverse()
    for i in range (0,len(b16)):
        if b16[i] in lettres:
            a=lettres.index(b16[i])
            b16[i]=nombres[a]
    for i in range(0, len(b16)):
        r+=int(b16[i])*(16**i)

def bitohex(b2):
    bitodec(b2)
    dectohex(r)

def hextobi(b16):
    hextodec(b16)
    dectobi(r)

while a==0:
    print("\n\n\n")
    b=input("Décimal en binaire (1)\nDécimal en hexadécimal (2)\nBinaire en décimal (3)\nBinaire en hexadécimal (4)\nHexadécimal en décimal (5)\nHexadécimal en binaire (6)\nFermer (7)\n")
    if b=="1":
        c=int(input("Nombre à convertir ?\n"))
        dectobi(c)
    if b=="2":
        c=int(input("Nombre à convertir ?\n"))
        dectohex(c)
    if b=="3":
        c=int(input("Nombre à convertir ?\n"))
        bitodec(c)
    if b=="4":
        c=int(input("Nombre à convertir ?\n"))
        bitohex(c)
    if b=="5":
        c=input("Nombre à convertir ?\n")
        hextodec(c)
    if b=="6":
        c=input("Nombre à convertir ?\n")
        hextobi(c)
    if b=="7":
        a=1
    print("-->",r)
