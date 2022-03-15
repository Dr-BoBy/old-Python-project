#Base de donnée projet

import re
import sqlite3
BDD=sqlite3.connect('BDD.db')
a=BDD.cursor()
a.execute("""CREATE TABLE IF NOT EXISTS vrac(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, Produit TEXT, Image TEXT, Quantité INT, Code_barre TEXT)""")
a.execute("""CREATE TABLE IF NOT EXISTS unite(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, Produit TEXT, Image TEXT, Quantité INT, Code_barre TEXT)""")
#Validation de l'écriture
BDD.commit()

###Ajout des produits en vrac
unite=[]
unite.append(("Haricots 2.5kg", "Haricots.png", 20, "0212020320"))
unite.append(("Steak haché x4", "Steakhaché.png", 15, "0202203202"))

a.executemany("INSERT INTO unite(Produit,Image,Quantité,Code_barre) VALUES(?,?,?,?)",unite)
BDD.commit()

###Ajouter des lignes à la base de donnée
def ajouterqte():
    BDD=sqlite3.connect('BDD.db')
    a=BDD.cursor()
    ###Unité ou vrac?
    b=input("Voulez-vous ajouter du vrac de de l'unite? ")
    ###Ajouter au vrac:
    if b=="vrac":
        a=BDD.cursor()
        ###Scan de code barre
        cb=input("Entrez le code barre: ")
        a.execute("SELECT id FROM unite WHERE Code_barre=?",(cb,))
        vrac2=a.fetchone()
        vrac2=str(vrac2)
        vrac2=vrac2.lstrip('(')
        vrac2=vrac2.rstrip(')')
        vrac2=vrac2.rstrip(',')
        vrac2=int(vrac2)
        print("l'ID =",vrac2)
        a.execute("SELECT Quantité FROM unite WHERE id=?",(vrac2,))
        vrac3=a.fetchone()
        vrac3=str(vrac3)
        vrac3=vrac3.lstrip('(')
        vrac3=vrac3.rstrip(')')
        vrac3=vrac3.rstrip(',')
        vrac3=int(vrac3)
        print("unite3= ",vrac3)
        ajt=int(input("Combien de produits entrent dans le stock? "))
        newval=(ajt)+(vrac3)
        print(newval)
        a.execute("UPDATE unite SET Quantité=? WHERE id=?",(newval,vrac2,))
        vrac4=a.fetchone()
        print(vrac4)
        a.execute("SELECT Quantité FROM unite WHERE id=?",(vrac2,))
        v3=a.fetchone()
        print(v3)
        BDD.commit()
        a.close()
        BDD.close()
            

    ###Ajouter à l'unite
    elif b=="unite":
        a=BDD.cursor()
        ###Scan de code barre
        cb=input("Entrez le code barre: ")
        a.execute("SELECT id FROM unite WHERE Code_barre=?",(cb,))
        unite2=a.fetchone()
        unite2=str(unite2)
        unite2=unite2.lstrip('(')
        unite2=unite2.rstrip(')')
        unite2=unite2.rstrip(',')
        unite2=int(unite2)
        print("l'ID =",unite2)
        a.execute("SELECT Quantité FROM unite WHERE id=?",(unite2,))
        unite3=a.fetchone()
        unite3=str(unite3)
        unite3=unite3.lstrip('(')
        unite3=unite3.rstrip(')')
        unite3=unite3.rstrip(',')
        unite3=int(unite3)
        print("unite3= ",unite3)
        ajt=int(input("Combien de produits entrent dans le stock? "))
        newval=(ajt)+(unite3)
        print(newval)
        a.execute("UPDATE unite SET Quantité=? WHERE id=?",(newval,unite2,))
        unite4=a.fetchone()
        print(unite4)
        a.execute("SELECT Quantité FROM unite WHERE id=?",(unite2,))
        u3=a.fetchone()
        print(u3)
        BDD.commit()
        a.close()
        BDD.close()
    else:
        print("Vous n'avez pas orthographié comme il fallait le nom")

#Sortie de produits
def enleverqte():
    BDD=sqlite3.connect('BDD.db')
    a=BDD.cursor()
    ###Unité ou vrac?
    b=input("Voulez-vous enlever du vrac ou de l'unite? ")
    ###Enlever au vrac:
    if b=="vrac":
        a=BDD.cursor()
        ###Scan de code barre
        cb=input("Entrez le code barre: ")
        a.execute("SELECT id FROM unite WHERE Code_barre=?",(cb,))
        vrac2=a.fetchone()
        vrac2=str(vrac2)
        vrac2=vrac2.lstrip('(')
        vrac2=vrac2.rstrip(')')
        vrac2=vrac2.rstrip(',')
        vrac2=int(vrac2)
        print("l'ID =",vrac2)
        a.execute("SELECT Quantité FROM unite WHERE id=?",(vrac2,))
        vrac3=a.fetchone()
        vrac3=str(vrac3)
        vrac3=vrac3.lstrip('(')
        vrac3=vrac3.rstrip(')')
        vrac3=vrac3.rstrip(',')
        vrac3=int(vrac3)
        print("unite3= ",vrac3)
        ajt=int(input("Combien de produits sortent du stock? "))
        newval=(vrac3)-(ajt)
        if newval>=0:
            print(newval)
            a.execute("UPDATE unite SET Quantité=? WHERE id=?",(newval,vrac2,))
            vrac4=a.fetchone()
            print(vrac4)
            a.execute("SELECT Quantité FROM unite WHERE id=?",(vrac2,))
            v3=a.fetchone()
            print(v3)
            BDD.commit()
            a.close()
            BDD.close()
        else:
            print("La valeur est négative, c'est impossible")
            a.close()
            BDD.close()

    ###Enlever à l'unite
    elif b=="unite":
        a=BDD.cursor()
        ###Scan de code barre
        cb=input("Entrez le code barre: ")
        a.execute("SELECT id FROM unite WHERE Code_barre=?",(cb,))
        unite2=a.fetchone()
        unite2=str(unite2)
        unite2=unite2.lstrip('(')
        unite2=unite2.rstrip(')')
        unite2=unite2.rstrip(',')
        unite2=int(unite2)
        print("l'ID =",unite2)
        a.execute("SELECT Quantité FROM unite WHERE id=?",(unite2,))
        unite3=a.fetchone()
        unite3=str(unite3)
        unite3=unite3.lstrip('(')
        unite3=unite3.rstrip(')')
        unite3=unite3.rstrip(',')
        unite3=int(unite3)
        print("unite3= ",unite3)
        ajt=int(input("Combien de produits sortent du stock? "))
        newval=(unite3)-(ajt)
        if newval>=0:
            print(newval)
            a.execute("UPDATE unite SET Quantité=? WHERE id=?",(newval,unite2,))
            unite4=a.fetchone()
            print(unite4)
            a.execute("SELECT Quantité FROM unite WHERE id=?",(unite2,))
            u3=a.fetchone()
            print(u3)
            BDD.commit()
            a.close()
            BDD.close()
        else:
            print("La valeur est négative, c'est impossible")
            a.close()
            BDD.close()
    else:
        print("Vous n'avez pas orthographié comme il fallait le nom")

def ajouterproduit():
    BDD=sqlite3.connect('BDD.db')
    a=BDD.cursor()
    ###Unité ou vrac?
    b=input("Voulez-vous ajouter un nouvel élément en vrac ou en unite? ")
    if b=="vrac":
        nbr=int(input("Combien de produits voulez vous entrer? "))
        for i in range(nbr):
            ###Scan de code barre
            cb=input("Entrez le code barre: ")
            a.execute("SELECT * FROM vrac WHERE Code_barre=?",(cb,))
            vrac2=a.fetchone()
            print(vrac2)
            
    elif b=="unite":
        a=BDD.cursor()
        nbr=int(input("Combien de produits voulez vous entrer? "))
        for i in range(nbr):
            ###Scan de code barre
            cb=input("Entrez le code barre: ")
            a.execute("SELECT id FROM unite WHERE Code_barre=?",(cb,))
            unit2=a.fetchone()
            print(unit2)
            if unit2!="None":
                unite=[]
                name=str(input("Quel est le nom du nouveau produit? "))
                photo=str(input("Quel est le nom de l'image dans le dossier? "))
                quantite=int(input("Quelle quantité de ce nouveau produit entre dans le stock? "))
                unite.append((name,photo,quantite,cb))
                print("Nom:",name)
                print("Photo:",photo)
                print("Quantité:",quantite)
                print("Code barre:",cb)
                BDD.commit()
                
                a.execute("SELECT id FROM unite WHERE Code_barre=?",(cb,))
                lid=a.fetchone()
                print("L'id est:",lid)
                a.close()
                BDD.close()
                
            else:
                print("Le produit existe déjà")
    else:
        print("Vous avez mal orthographié")


###Programme principal
action=int(input("Que voulez vous faire sur la base de donnée? 1.ajouter de la quantité, 2.enlever de la quantité, 3.ajouter un nouveau produit? "))
if action==1:
    ajouterqte()
elif action==2:
    enleverqte()
elif action==3:
    ajouterproduit()
else:
    print("Vous avez fait une erreur")







            
