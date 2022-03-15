import tkinter
from tkinter import *
import time
import threading
import copy
import random

root=tkinter.Tk(className= " RETRO EDITION : Space Invaders")

x1=400
x2=70
y2=300
y3=600
v=10
l1=[1,1,1,1,1,1,1,1]
l2=[1,1,1,1,1,1,1,1]
l3=[1,1,1,1,1,1,1,1]
l4=[1,1,1,1,1,1,1,1]
l=[l1,l2,l3,l4]
maxdecale=0
win=0



canon= PhotoImage(file="./texture/canon.png")
tir= PhotoImage(file="./texture/tir.png")
alien1= PhotoImage(file="./texture/alien1.png")
alien2= PhotoImage(file="./texture/alien2.png")
alien3= PhotoImage(file="./texture/alien3.png")
alien4= PhotoImage(file="./texture/alien4.png")
lalien=[alien1,alien2,alien3,alien4]

    
def CLIC(event):
    X=event.x
    Y=event.y




def RIGHT(event):
    global x1
    global tcanon
    x1=x1+v
    canvas.delete(tcanon)
    tcanon=canvas.create_image(x1,750,image=canon)
    canvas.update()

def LEFT(event):
    global x1
    global tcanon
    x1=x1-v
    canvas.delete(tcanon)
    tcanon=canvas.create_image(x1,750,image=canon)
    canvas.update()

class TEMPOTIR(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            canvas.unbind_all('<space>')
            time.sleep(2)
            canvas.bind_all('<space>',DTIR)
            
            
class TIR(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global y3
            global x3
            global i1
            global i2
            y3=750
            x3=copy.copy(x1)
            while y3>0:
                ttir=canvas.create_image(x3,y3-20,image=tir)
                time.sleep(0.01)
                canvas.delete(ttir)
                y3=y3-5
                if len(canvas.find_overlapping(x3-2,y3-5,x3+2,y3+5))>=1 and y3<650:
                    canvas.delete(canvas.find_overlapping(x3-2,y3-5,x3+2,y3+5)[0])
                    if y2-10<y3<y2+45:
                        i1=0
                    elif y2-85<y3<y2-30:
                        i1=1
                    elif y2-160<y3<y2-105:
                        i1=2
                    elif y2-235<y3<y2-180:
                        i1=3
                    if 35<x3<105:
                        i2=0
                    elif 130<x3<200:
                        i2=1
                    elif 225<x3<275:
                        i2=2
                    elif 300<x3<370:
                        i2=3
                    elif 395<x3<465:
                        i2=4
                    elif 490<x3<560:
                        i2=5
                    elif 585<x3<655:
                        i2=6
                    elif 680<x3<750:
                        i2=7
                    l[i1][i2]=0
                    break

class TIRINVADERS(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            y4=y2-(random.randint(1,3)*75)
            x4=x2+(random.randint(1,7)*95)
            while y4<800:
                ttirinvaders=canvas.create_rectangle(x4-5,y4-15,x4+5,y4+15,outline="lightgreen",fill="lightgreen")
                time.sleep(0.01)
                canvas.delete(ttirinvaders)
                y4=y4+5
                
def DTIR(event): #Déclencher tir
    tir=TIR()
    tir.start()
    tempotir=TEMPOTIR()
    tempotir.start()

def INVADERS():
    global x2;global y2
    for j in range(0,4):
        for i in range(0,8):
            if l[j][i]==1:
                canvas.create_image(x2,y2,image=lalien[j])
            x2=x2+95
        y2=y2-75
        x2=x2-8*95
    y2=y2+300


class TIMER(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global x2; global y2; global maxdecale
            timerg=0
            timert=0
            r1=random.randint(10,15)
            r4=random.randint(1,1)
            while win==0:
                time.sleep(1)
                timerg=timerg+1
                timert=timert+1
                if timerg==r1:
                    allobject=canvas.find_overlapping(0,0,800,650)
                    for i in range (0,len(allobject)):
                        canvas.delete(allobject[i])
                    r2=random.randint(5,35)
                    r3=random.randint(-35,35)
                    y2=y2+r2
                    if x2<50 and r3<0:
                        r3=-r3
                    if x2>100 and r3>0:
                        r3=-r3
                    x2=x2+r3
                    INVADERS()
                    timerg=0
                if timert==r4:
                    tirinvader=TIRINVADERS()
                    tirinvader.start()
                    timert=0
                    
                    
                    
                    
                
    

def PLAY ():
    global tcanon
    canvas.bind('<ButtonRelease>',CLIC)
    canvas.bind_all('<Right>',RIGHT)
    canvas.bind_all('<Left>',LEFT)
    canvas.bind_all('<space>',DTIR)
    tcanon=canvas.create_image(x1,750,image=canon)
    INVADERS()
    timer=TIMER()
    timer.start()

canvas=Canvas(height=800,width=800,bg="black")
canvas.pack()

#canvas.create_rectangle(0,0,800,650,outline="red")

PLAY()



root.mainloop()


