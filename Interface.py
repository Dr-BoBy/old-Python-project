import tkinter
import time
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import *
#from Pillow import Image, ImageTk
import re
import sqlite3

BDD=sqlite3.connect('BDD.db')
a=BDD.cursor()

###################################################################################################
############################### AJOUTER NOUVEAU PRODUIT AU STOCK ##################################
###################################################################################################
img=""

def importer_image():
    global img
    global canvas_apercu_image
    name_file = filedialog.askopenfilename()
    name_file=list(name_file)
    name_file2="".join(name_file)
    for i in range (len(name_file)):
        if name_file[i]==".":
            del name_file[0:i+1]
            break
    name_file="".join(name_file)
    
    if name_file!="png" and name_file!="jpg":
        tkinter.messagebox.showerror(title="Erreur Format", message="Format d\'image non-valide")
        img=""
    else:
        canvas_apercu_image=Canvas(page3,width=200,height=200,bg="black")
        #canvas_apercu_image.pack()
        #image = Image.open(name_file2)
        #img = ImageTk.PhotoImage(image)  
        #apercu_img=canvas_apercu_image.create_image(0,0,anchor="nw",image=img)
        #canvas_apercu_image.update()
    
    
def ajouter_nouveau_produit(): #à revoir !
    Label_entree_nouveau_produit=tkinter.Label(page3,text="Nom du nouveau produit :")
    Entry_entree_nouveau_produit=tkinter.Entry(page3)
    Label_entree_nouveau_code_barre=tkinter.Label(page3,text="Code barre :")
    Entry_entree_nouveau_code_barre=tkinter.Entry(page3)
    Boutton_importer_image=tkinter.Button(page3,text="Importer une image",command=importer_image)
    Boutton_ajouter_nouveau_produit_final=tkinter.Button(page3,text="Ajouter un nouveau produit",command=ajouter_nouveau_produit_final)


    Label_entree_nouveau_produit.pack()
    Entry_entree_nouveau_produit.pack()
    Label_entree_nouveau_code_barre.pack()
    Entry_entree_nouveau_code_barre.pack()
    Boutton_importer_image.pack()
    Boutton_ajouter_nouveau_produit.destroy()
    Boutton_ajouter_nouveau_produit_final.pack()
    
def ajouter_nouveau_produit_final():
    if Entry_entree_nouveau_code_barre.get()=="" or len(Entry_entree_nouveau_code_barre.get())!=13 or Entry_entree_nouveau_produit.get()=="" or img=="":   
        tkinter.messagebox.showerror(title="Erreur validation", message="Il manque des informations !")
    else:
        Label_entree_nouveau_produit.destroy()
        Entry_entree_nouveau_produit.destroy()
        Label_entree_nouveau_code_barre.destroy()
        Entry_entree_nouveau_code_barre.destroy()
        Boutton_importer_image.destroy()
        Boutton_ajouter_nouveau_produit_final.destroy()
        canvas_apercu_image.destroy()

###################################################################################################
##################################### AJOUTER UNITE AU STOCK ######################################
###################################################################################################

def finalisé_ajout_unité():
    #ajouté gabin
    fen2_1.destroy()
    fen2.destroy()
    
def annulé_unité():
    fen2_1.destroy()
    
def validé_ajout_unité():
    global fen2_1
    fen2_1=tkinter.Toplevel(fen2)
    a.execute("SELECT id FROM unite WHERE Code_barre=?",(Entry_code_barre_unité.get(),))
    vrac2=a.fetchone()
    vrac2=str(vrac2); vrac2=vrac2.lstrip('('); vrac2=vrac2.rstrip(')'); vrac2=vrac2.rstrip(','); vrac2=int(vrac2)
    a.execute("SELECT Produit FROM unite WHERE id=?",(vrac2,))
    nom=a.fetchone()
    nom=str(nom); nom=nom.lstrip('('); nom=nom.rstrip(')'); nom=nom.rstrip(',')
    quantité=Entry_quantité_unité.get()
    text="Ajouter "+nom+" "+str(quantité)+" fois au stock ?"
    Label_question_unité=tkinter.Label(fen2_1,text=text)
    Label_question_unité.pack()
    Can=Canvas(fen2_1,height=200,width=200,bg="black")
    Can.pack()
    frame_ouinon_unité=tkinter.Frame(fen2_1)
    frame_ouinon_unité.pack()
    (tkinter.Button(frame_ouinon_unité,text="Oui",command=finalisé_ajout_unité)).pack(side=tkinter.LEFT)
    (tkinter.Button(frame_ouinon_unité,text="Nob",command=annulé_unité)).pack(side=tkinter.LEFT)
    
def ajouter_produit_unité():
    global fen2
    global Entry_code_barre_unité
    global Entry_quantité_unité
    fen2=tkinter.Toplevel()
    Label_code_barre_unité=tkinter.Label(fen2,text="Code barre :")
    Label_code_barre_unité.pack()
    Entry_code_barre_unité=tkinter.Entry(fen2)
    Entry_code_barre_unité.pack()
    Entry_code_barre_unité.focus()
    Label_quantité_unité=tkinter.Label(fen2,text="Quantité :")
    Label_quantité_unité.pack()  
    Entry_quantité_unité=tkinter.Entry(fen2)
    Entry_quantité_unité.pack()
    Entry_quantité_unité.insert(0,"1")
    Boutton_validé_unité=tkinter.Button(fen2,text="Validé",command=validé_ajout_unité)
    Boutton_validé_unité.pack() 

"""###################################################################################################
##################################### ENLEVER UNITE AU STOCK ######################################
###################################################################################################

def finalisé_ajout_unité():
    #ajouté gabin
    fen2_1.destroy()
    fen2.destroy()
    
def annulé_unité():
    fen2_1.destroy()
    
def validé_ajout_unité():
    global fen2_1
    fen2_1=tkinter.Toplevel(fen2)
    #get gabin
    
    nom=" haricots"
    quantité=" 10"
    text="Enlever"+nom+quantité+" fois au stock ?"
    Label_question_unité=tkinter.Label(fen2_1,text=text)
    Label_question_unité.pack()
    Can=Canvas(fen2_1,height=200,width=200,bg="black")
    Can.pack()
    frame_ouinon_unité=tkinter.Frame(fen2_1)
    frame_ouinon_unité.pack()
    (tkinter.Button(frame_ouinon_unité,text="OUI",command=finalisé_ajout_unité)).pack(side=tkinter.LEFT)
    (tkinter.Button(frame_ouinon_unité,text="NON",command=annulé_unité)).pack(side=tkinter.LEFT)
    
def enlever_produit_unité():
    global fen2
    fen2=tkinter.Toplevel()
    Label_code_barre_unité=tkinter.Label(fen2,text="Code barre :")
    Label_code_barre_unité.pack()
    Entry_code_barre_unité=tkinter.Entry(fen2)
    Entry_code_barre_unité.pack()
    Entry_code_barre_unité.focus()
    Label_quantité_unité=tkinter.Label(fen2,text="Quantité :")
    Label_quantité_unité.pack()  
    Entry_quantité_unité=tkinter.Entry(fen2)
    Entry_quantité_unité.pack()
    Entry_quantité_unité.insert(0,"1")
    Boutton_validé_unité=tkinter.Button(fen2,text="Validé",command=validé_ajout_unité)
    Boutton_validé_unité.pack()"""
    
###################################################################################################
####################################### INTERFACE #################################################
###################################################################################################
    
root=Tk()

nb = ttk.Notebook(root)
nb.grid(row=1,column=0,columnspan=50,rowspan=49,sticky='NESW')

############PAGE 1##################

page1= ttk.Frame(nb)
nb.add(page1,text="Vue d'ensemble")

############PAGE 2##################

page2= ttk.Frame(nb)
nb.add(page2,text="Gestion du stock")

Boutton_ajouter_produit=tkinter.Button(page2,text="Ajouter un produit au stock",command=ajouter_produit_unité)
Boutton_ajouter_produit.pack()
"""Boutton_enlever_produit=tkinter.Button(page2,text="Enlver un produit du stock",command=enlever_produit_unité)
Boutton_enlever_produit.pack()"""

############PAGE 3##################

page3= ttk.Frame(nb)
nb.add(page3,text="Edition du stock")
    
Boutton_ajouter_nouveau_produit=tkinter.Button(page3,text="Ajouter un nouveau produit",command=ajouter_nouveau_produit)
Boutton_ajouter_nouveau_produit.pack()

root.mainloop()

