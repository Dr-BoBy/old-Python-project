import tkinter
from tkinter import *
import time
import random
import threading
import math
import copy

#VARIABLE=================================
pi=3.141592653897932384626433
x1=400
y1=400
x2=400
y2=400
angle=0
angle2=0
ship=""
lship=[]
p1=(round(x1+math.cos(angle+(pi/2))*15),round(y1-math.sin(angle+(pi/2))*15))
p2=(round(x1+math.cos(angle-(pi/3))*15),round(y1-math.sin(angle-(pi/3))*15))
p3=(round(x1+math.cos(angle-(pi/2))*10),round(y1-math.sin(angle-(pi/2))*10))
p4=(round(x1+math.cos(angle-(2*pi/3))*15),round(y1-math.sin(angle-(2*pi/3))*15))
pts=[p1,p2,p3,p4]

#FONCTION=================================

def VAISSEAU():
    global lship
    global p1; global p2; global p3; global p4
    p1=(round(x1+math.cos(angle+(pi/2))*15),round(y1-math.sin(angle+(pi/2))*15))
    p2=(round(x1+math.cos(angle-(pi/3))*15),round(y1-math.sin(angle-(pi/3))*15))
    p3=(round(x1+math.cos(angle-(pi/2))*10),round(y1-math.sin(angle-(pi/2))*10))
    p4=(round(x1+math.cos(angle-(2*pi/3))*15),round(y1-math.sin(angle-(2*pi/3))*15))
    pts=[p1,p2,p3,p4]
    ship=canvas.create_polygon(pts,outline="white")
    lship.append(ship)
    canvas.delete(lship[0])
    del lship[0]
    canvas.update()
          
class THREAD_ROTATE_RIGHT(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global angle
            angle=round(angle-0.2,1)
            VAISSEAU()

class THREAD_ROTATE_LEFT(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global angle
            angle=round(angle+0.2,1)
            VAISSEAU()
            
            

class THREAD_MOVE(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global x1
            global y1
            global direction
            x1+=math.cos(angle+(pi/2))*5
            y1-=math.sin(angle+(pi/2))*5  
            if p1[0]>800 and p2[0]>800 and p3[0]>800 and p4[0]>800:
                x1-=800
            if p1[0]<0 and p2[0]<0 and p3[0]<0 and p4[0]<0:
                x1+=800
            if p1[1]>800 and p2[1]>800 and p3[1]>800 and p4[1]>800:
                y1-=800
            if p1[1]<0 and p2[1]<0 and p3[1]<0 and p4[1]<0:
                y1+=800
            VAISSEAU()
            

class THREAD_FIRE(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global x2
            global y2
            global angle2
            x2=copy.copy(x1)
            y2=copy.copy(y1)
            angle2=copy.copy(angle)
            for i in range(100):
                bullet=canvas.create_line(x2,y2,x2+math.cos(angle2+(pi/2))*5,y2-math.sin(angle2+(pi/2))*5,fill="white")  
                x2=x2+math.cos(angle2+(pi/2))*5
                y2=y2-math.sin(angle2+(pi/2))*5
                time.sleep(0.01)
                canvas.delete(bullet)
            
def ROTATE_RIGHT(event):
    thread_rotate_right=THREAD_ROTATE_RIGHT()
    thread_rotate_right.start()

def ROTATE_LEFT(event):
    thread_rotate_left=THREAD_ROTATE_LEFT()
    thread_rotate_left.start()
    
def MOVE(event):
    thread_move=THREAD_MOVE()
    thread_move.start()
 
def FIRE(event):
    thread_fire=THREAD_FIRE()
    thread_fire.start()
    
def START():
    canvas.bind_all('<space>',FIRE)
    canvas.bind_all('<Up>',MOVE)
    canvas.bind_all('<Left>',ROTATE_LEFT)
    canvas.bind_all('<Right>',ROTATE_RIGHT)
    
    
    
    
    
    
    
root=Tk()
canvas=Canvas(height=800,width=800,bg="black")
canvas.pack()



ship=canvas.create_polygon(pts,outline="white")
lship.append(ship)
VAISSEAU()
START()

root.mainloop()
