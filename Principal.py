from tkinter import *
import tkinter
import time
import random

biomes=["Forêt","Désert","Montagne","Taiga","Messa"]
inmine=0

#texture_stone=PhotoImage(file='./Texture/stone.png')

inventaire=[]


Menu=Tk()
#############################################################
#########################INVENTAIRE##########################
#############################################################
def INVENTAIRE():
    Inventaire=tkinter.Toplevel(Menu)
#############################################################
#########################OVERWORLD###########################
#############################################################
def GO_TO_OVERWORLD():
    Overworld=tkinter.Toplevel(Menu)
#############################################################
###############################MINE##########################
#############################################################
def OUT_MINE():
    afficheur_menu.config(text="Tu quittes la mine")
    in_mine=0
    Mine.destroy()
    
def MINE():
    loot=random.randint(1,200)
    if loot==1:
        loot="Diamant"
    elif 4>=loot>=2:
        loot="Lapis lazuli"
    elif 12>=loot>=5:
        loot="Poudre de redstone"
    elif 14>=loot>=13:
        loot="Minerai d'or"
    elif 20>=loot>=15:
        loot="Minerai de fer"
    elif 30>=loot>=21:
        loot="Charbon"
    else:
        loot="Pierre travaillé" 
    inventaire.append(loot)
    afficheur_mine.config(text="Tu obtients 1 "+loot)

    
def GO_TO_MINE():
    global Mine
    global afficheur_mine
    in_mine=1
    afficheur_menu.config(text="Tu entres dans la mine")
    Mine=tkinter.Toplevel(Menu)
    frame_afficheur_mine=tkinter.Frame(Mine,borderwidth=2,relief=GROOVE)
    afficheur_mine=tkinter.Label(frame_afficheur_mine,text="")
    afficheur_mine.pack()
    frame_afficheur_mine.pack()
    Mine.protocol("WM_DELETE_WINDOW", OUT_MINE)
    button_miner=tkinter.Button(Mine,text="Miner",command=MINE)
    button_miner.pack()

    
    canvas=Canvas(Mine,width="400",height="400",bg="lightblue")
    canvas.pack()

#############################################################
###############################MENU##########################
#############################################################
def EXIT_OUI():
    Securite.destroy()
    Menu.destroy()

def EXIT_NON():
    Securite.destroy()

def SAVE():
    print("Sauvegarde à faire")
    
def EXIT():
    global Securite
    Securite=tkinter.Toplevel(Menu)
    msg_secu=tkinter.Label(Securite,text="Est tu sûr de vouloir quitter ?")
    msg_secu.pack()
    button_exit_oui=tkinter.Button(Securite,text="Oui",command=EXIT_OUI)
    button_exit_oui.pack(side=tkinter.LEFT)
    button_exit_save=tkinter.Button(Securite,text="Sauvegarder",command=SAVE)
    button_exit_save.pack(side=tkinter.LEFT)
    button_exit_non=tkinter.Button(Securite,text="Non",command=EXIT_NON)
    button_exit_non.pack(side=tkinter.LEFT)
    
frame_afficheur_menu=tkinter.Frame(Menu,borderwidth=2,relief=GROOVE)
afficheur_menu=tkinter.Label(frame_afficheur_menu,text="")
afficheur_menu.pack()
frame_afficheur_menu.pack()
button_go_to_overworld=tkinter.Button(Menu,text="Explorer le monde",command=GO_TO_OVERWORLD)
button_go_to_overworld.pack()
button_go_to_mine=tkinter.Button(Menu,text="Aller à dans la mine",command=GO_TO_MINE)
button_go_to_mine.pack()
button_inventaire=tkinter.Button(Menu,text="Inventaire",command=INVENTAIRE)
button_inventaire.pack()


Menu.protocol("WM_DELETE_WINDOW", EXIT)
Menu.mainloop()
