from tkinter import *
import tkinter
import time
import threading
import random

root=Tk(className=" RETRO EDITION : SNAKE ")

direction="z"
x1=400
y1=400
lose=0
lsnake=[]
lenght=1
frut=0

play= PhotoImage(file='./text/play.png')
play2= PhotoImage(file='./text/play2.png')
snake= PhotoImage(file='./text/snake.png')
snake2= PhotoImage(file='./text/snake2.png')
credit= PhotoImage(file='./text/credit.png')
boby= PhotoImage(file='./text/boby.png')
img1= PhotoImage(file='./text/1.png')
img2= PhotoImage(file='./text/2.png')
img3= PhotoImage(file='./text/3.png')
game_over= PhotoImage(file='./text/game_over.png')


def DIRECTION (event):
    global direction
    if event.keysym=="Up" and direction!="s":
        direction="z"
    if event.keysym=="Down" and direction!="z":
        direction="s"
    if event.keysym=="Right" and direction!="q":
        direction="d"
    if event.keysym=="Left" and direction!="d":
        direction="q"

def END():
    canvas.unbind_all('<Up>')
    canvas.unbind_all('<Down>')
    canvas.unbind_all('<Right>')
    canvas.unbind_all('<Left>')
    tgame_over=canvas.create_image(400,400,image=game_over)

def PLAY():
    canvas.delete(tplay)
    canvas.delete(tsnake)
    canvas.bind_all('<Up>',DIRECTION)
    canvas.bind_all('<Down>',DIRECTION)
    canvas.bind_all('<Right>',DIRECTION)
    canvas.bind_all('<Left>',DIRECTION)
    canvas.unbind_all('<ButtonRelease>')
    t3=canvas.create_image(400,400,image=img3)
    canvas.update()
    time.sleep(1)
    canvas.delete(t3)
    t2=canvas.create_image(400,400,image=img2)
    canvas.update()
    time.sleep(1)
    canvas.delete(t2)
    t1=canvas.create_image(400,400,image=img1)
    canvas.update()
    time.sleep(1)
    canvas.delete(t1)
    AUTOMOVE=Automove()
    AUTOMOVE.start()
    SPAWNAPPLE=SpawnApple()
    SPAWNAPPLE.start()

def CLIC (event):
    X=event.x
    Y=event.y
    if 190<X<610 and 210<Y<300:
        rootcredits=tkinter.Toplevel(root)
        canvas2=Canvas(rootcredits,height=500,width=500,bg="black")
        canvas2.pack()
        tcredit=canvas2.create_image(250,150,image=credit)
        tboby=canvas2.create_image(250,350,image=boby)
    if 220<X<580 and 510<Y<600:
        PLAY()
        
class Automove(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global x1; global y1; global lenght; global frut; global lose
            while lose==0:
                if direction=="z":
                    y1=y1-2
                    if y1<0:
                        y1=800
                elif direction=="s":
                    y1=y1+2
                    if y1>800:
                        y1=0
                elif direction=="q":
                    x1=x1-2
                    if x1<0:
                        x1=800
                elif direction=="d":
                    x1=x1+2
                    if x1>800:
                        x1=0
                snake=canvas.create_rectangle(x1-5,y1-5,x1+5,y1+5,fill="blue",outline="blue")
                lsnake.append(snake)
                time.sleep(0.01)
                while len(lsnake)>lenght:
                    canvas.delete(lsnake[0])
                    del lsnake[0]
                if x2-10<x1<x2+10 and y2-10<y1<y2+10:
                    canvas.delete(apple)
                    frut=0
                    lenght=lenght+1
                if len(canvas.find_overlapping(x1,y1,x1,y1))>5: 
                    lose=1
                    canvas.delete(ALL)
                    END()
                    
class SpawnApple(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global frut; global apple; global x2; global y2
            while lose==0:
                while frut==0:
                    x2=random.randint(10,790)
                    y2=random.randint(10,790)
                    apple=canvas.create_rectangle(x2-10,y2-10,x2+10,y2+10,fill="red",outline="red")
                    frut=1
                time.sleep(1)

                
canvas=Canvas(width=800,height=800,bg="black")
canvas.pack()
canvas.bind('<ButtonRelease>',CLIC)
tsnake=canvas.create_image(400,250,image=snake,activeimage=snake2)
tplay=canvas.create_image(400,550,image=play,activeimage=play2)
#canvas.create_rectangle(220,510,580,600,outline="red")



root.mainloop()
