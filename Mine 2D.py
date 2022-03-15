from tkinter import *
import tkinter
import time
import random
import threading

root=Tk()
inmine=1
x_joueur=232
y_joueur=72
y_spawn=0
texture_stone=PhotoImage(file='./Texture/stone.png')
texture_coal_ore=PhotoImage(file='./Texture/coal_ore.png')
texture_iron_ore=PhotoImage(file='./Texture/iron_ore.png')
texture_gold_ore=PhotoImage(file='./Texture/gold_ore.png')
texture_redstone_ore=PhotoImage(file='./Texture/redstone_ore.png')
texture_diamond_ore=PhotoImage(file='./Texture/diamond_ore.png')
texture_lapis_ore=PhotoImage(file='./Texture/lapis_ore.png')
texture_grass_side=PhotoImage(file='./Texture/grass_side.png')
texture_dirt=PhotoImage(file='./Texture/dirt.png')
texture_bedrock=PhotoImage(file='./Texture/bedrock.png')


def CREATE_MINING_COLUMN(x):
    for y in range(2+y_spawn,962+y_spawn,16):
        random_ore=random.randint(1,500)
        if y==2+y_spawn:
            canvas_mine.create_image(x,y,image=texture_grass_side,anchor="nw")
        elif 34+y_spawn>=y>=18+y_spawn:
            canvas_mine.create_image(x,y,image=texture_dirt,anchor="nw")
        elif random_ore==1 and 866+y_spawn>y>754+y_spawn: #diamant
            canvas_mine.create_image(x,y,image=texture_diamond_ore,anchor="nw") 
        elif 4>=random_ore>=2 and 722+y_spawn>y>690+y_spawn :#lapis
            canvas_mine.create_image(x,y,image=texture_lapis_ore,anchor="nw") 
        elif 12>=random_ore>=5 and 880+y_spawn>y>754+y_spawn :#redstone
            canvas_mine.create_image(x,y,image=texture_redstone_ore,anchor="nw") 
        elif 14>=random_ore>=13 and 880+y_spawn>y>434+y_spawn :#or
            canvas_mine.create_image(x,y,image=texture_gold_ore,anchor="nw") 
        elif 20>=random_ore>=15 and 880+y_spawn>y>96+y_spawn : #fer
            canvas_mine.create_image(x,y,image=texture_iron_ore,anchor="nw")     
        elif 30>=random_ore>=21 and 880+y_spawn>y>128+y_spawn : #charbon
            canvas_mine.create_image(x,y,image=texture_coal_ore,anchor="nw")
        elif y==946+y_spawn:
            canvas_mine.create_image(x,y,image=texture_bedrock,anchor="nw")
        else:
            canvas_mine.create_image(x,y,image=texture_stone,anchor="nw")
        canvas_mine.update()
        
    

def UPDATE_MINE():
    for x in range(2,482,16):
        obj=list(canvas_mine.find_overlapping(x,-960,x+16,960))
        if steve in obj:
             obj.remove(steve)
        if obj==[]:
            CREATE_MINING_COLUMN(x)

def MINE_BLOCK(event):
    X=event.x
    Y=event.y
    block_to_destroy = canvas_mine.find_closest(X, Y)
    if steve not in block_to_destroy:
        canvas_mine.delete(block_to_destroy)

def FOCUS_DROITE():
    obj=list(canvas_mine.find_overlapping(-10000,-960,10000,960))
    if steve in obj:
        obj.remove(steve)
    for i in range(len(obj)):
        co=canvas_mine.coords(obj[i])
        canvas_mine.coords(obj[i],co[0]+16,co[1])
    UPDATE_MINE()
        
def FOCUS_GAUCHE():
    obj=list(canvas_mine.find_overlapping(-10000,-960,10000,960))
    if steve in obj:
        obj.remove(steve)
    for i in range(len(obj)):
        co=canvas_mine.coords(obj[i])
        canvas_mine.coords(obj[i],co[0]-16,co[1])
    UPDATE_MINE()

def FOCUS_HAUT():
    global y_spawn
    obj=list(canvas_mine.find_overlapping(-10000,-960,10000,960))
    if steve in obj:
        obj.remove(steve)
    for i in range(len(obj)):
        co=canvas_mine.coords(obj[i])
        canvas_mine.coords(obj[i],co[0],co[1]-16)
    y_spawn-=16

def FOCUS_BAS():
    global y_spawn
    obj=list(canvas_mine.find_overlapping(-10000,-960,10000,960))
    if steve in obj:
        obj.remove(steve)
    for i in range(len(obj)):
        co=canvas_mine.coords(obj[i])
        canvas_mine.coords(obj[i],co[0],co[1]+16)
    y_spawn+=16

class GRAVITY(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global y_joueur
            while inmine==1:
                try:
                    time.sleep(0.5)
                    while canvas_mine.find_overlapping(x_joueur-5,y_joueur+11,x_joueur+5,y_joueur+21)==():
                        if y_joueur>400:
                            FOCUS_HAUT()
                            
                        else:
                            co_steve=canvas_mine.coords(steve)
                            canvas_mine.coords(steve,co_steve[0],co_steve[1]+16,co_steve[2],co_steve[3]+16)
                            y_joueur+=16
                            time.sleep(0.1)         
                except:
                    continue
            
def MOVE (event):
    global y_joueur
    global x_joueur
    co_steve=canvas_mine.coords(steve)
    if event.keysym=="Up":
        if y_joueur<80 and canvas_mine.find_overlapping(x_joueur,y_joueur-32,x_joueur,y_joueur-32)==():
            FOCUS_BAS()
        else:
            if canvas_mine.find_overlapping(x_joueur,y_joueur-32,x_joueur,y_joueur-32)==():
                canvas_mine.coords(steve,co_steve[0],co_steve[1]-16,co_steve[2],co_steve[3]-16)
                y_joueur-=16
            
    if event.keysym=="Right":
        if x_joueur>400 and canvas_mine.find_overlapping(x_joueur+11,y_joueur,x_joueur+21,y_joueur-16)==():        
                FOCUS_GAUCHE()
        else:
            if canvas_mine.find_overlapping(x_joueur+11,y_joueur,x_joueur+21,y_joueur-16)==():
                canvas_mine.coords(steve,co_steve[0]+16,co_steve[1],co_steve[2]+16,co_steve[3])
                x_joueur+=16
        canvas_mine.update()
    if event.keysym=="Left":
        if x_joueur<80 and canvas_mine.find_overlapping(x_joueur-11,y_joueur,x_joueur-21,y_joueur-16)==():
            FOCUS_DROITE()
        else:
            if canvas_mine.find_overlapping(x_joueur-11,y_joueur,x_joueur-21,y_joueur-16)==():
                canvas_mine.coords(steve,co_steve[0]-16,co_steve[1],co_steve[2]-16,co_steve[3])
                x_joueur-=16
        canvas_mine.update()
        
        
            
        
canvas_mine=Canvas(width="480",height="480",bg="black")
canvas_mine.pack()

canvas_mine.bind('<Button-1>', MINE_BLOCK)
canvas_mine.bind_all('<KeyRelease-Up>', MOVE)
canvas_mine.bind_all('<KeyRelease-Left>', MOVE)
canvas_mine.bind_all('<KeyRelease-Right>', MOVE)

for x in range(2,482,16):
    CREATE_MINING_COLUMN(x)

x_to_destroy=168
y_to_destroy=8
for i in range(0,5):
    bloc_to_destroy=canvas_mine.find_overlapping(x_to_destroy,y_to_destroy,x_to_destroy+2,y_to_destroy-32)
    for j in range (len(bloc_to_destroy)):
        canvas_mine.delete(bloc_to_destroy[j])
    x_to_destroy+=16
    y_to_destroy+=16
        

steve=canvas_mine.create_rectangle(x_joueur-5,y_joueur-15,x_joueur+5,y_joueur+5,fill="blue")

gravity=GRAVITY()
gravity.start()
root.mainloop()
