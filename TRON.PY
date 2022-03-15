from tkinter import *
import tkinter
import random
import time
import threading




x1= 770
y1= 770
x2=30
y2=30
x3=0
y3=800
x4=0
y4=0
win=0
lmoto1=[]
lmoto2=[]
dead1=[]
dead2=[]
direction1="q1"
direction2="d2"
lcolor=["blue","red","aqua","violet","navy","silver","green","olive","teal","lime","purple","white","fuchsia","maroon","yellow"]
icolor1=0
icolor2=1
icolor=random.randint(0,len(lcolor)-1)
setup=0
bot1=0
v=0.026

root=tkinter.Tk(className=" RETRO EDITION : Tron the Game ")





save = PhotoImage(file='./text/save.png')
save2 = PhotoImage(file='./text/save2.png')
settings = PhotoImage(file='./text/settings.png')
settings2 = PhotoImage(file='./text/settings2.png')
player1mini= PhotoImage(file='./text/player1mini.png')
player2mini= PhotoImage(file='./text/player2mini.png')
credit = PhotoImage(file='./text/credits.png')
idea = PhotoImage(file='./text/original idea.png')
boby1 = PhotoImage(file='./text/boby1.png')
program = PhotoImage(file='./text/program by.png')
boby2 = PhotoImage(file='./text/boby2.png')
widea = PhotoImage(file='./text/with the ideas of.png')
papy = PhotoImage(file='./text/papy.png')
player = PhotoImage(file='./text/player.png')
bot = PhotoImage(file='./text/bot.png')





class End1(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            player2= PhotoImage(file='./text/player2.png')
            tplayer2=canvas.create_image(400, 350, image=player2)
            twin= PhotoImage(file='./text/win.png')
            ttwin=canvas.create_image(400, 450, image=twin)
            newgame= PhotoImage(file='./text/newgame.png')
            tnewgame=canvas.create_image(400,775,image=newgame)
            canvas.update()
            while win==1:
                canvas.delete(tplayer2)
                canvas.delete(ttwin)
                time.sleep(1)
                canvas.create_rectangle(0,0,800,800,fill="black")
                tnewgame=canvas.create_image(400,775,image=newgame)
                player2= PhotoImage(file='./text/player2.png')
                tplayer2=canvas.create_image(400, 350, image=player2)
                twin= PhotoImage(file='./text/win.png')
                ttwin=canvas.create_image(400, 450, image=twin)
                time.sleep(1.5)

class End2(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            player1= PhotoImage(file='./text/player1.png')
            tplayer1=canvas.create_image(400, 350, image=player1)
            twin= PhotoImage(file='./text/win.png')
            ttwin=canvas.create_image(400, 450, image=twin)
            newgame= PhotoImage(file='./text/newgame.png')
            tnewgame=canvas.create_image(400,775,image=newgame)
            canvas.update()
            while win==1:
                canvas.delete(tplayer1)
                canvas.delete(ttwin)
                time.sleep(1)
                canvas.create_rectangle(0,0,800,800,fill="black")
                tnewgame=canvas.create_image(400,775,image=newgame)
                player1= PhotoImage(file='./text/player1.png')
                tplayer1=canvas.create_image(400, 350, image=player1)
                twin= PhotoImage(file='./text/win.png')
                ttwin=canvas.create_image(400, 450, image=twin)
                time.sleep(1.5)




    
def Dead1 ():
    global win
    win=1
    time.sleep(0.25)
    canvas.delete(ALL)
    end1=End1()
    end1.start()

def Dead2 ():
    global win
    win=1
    time.sleep(0.25)
    canvas.delete(ALL)
    end2=End2()
    end2.start()





class CheckDead1(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global dead1
            while win==0:
                dead1=list(canvas.find_overlapping(x1,y1,x1,y1))
                if len(dead1)>4:
                    Dead1()

class CheckDead2(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global dead2
            while win==0:
                dead2=list(canvas.find_overlapping(x2,y2,x2,y2))
                if len(dead2)>4:
                    Dead2()




           

def DIRECTION1 (event):
    global direction1
    if event.keysym=="Up":
        direction1="z1"
    if event.keysym=="Down":
        direction1="s1"
    if event.keysym=="Right":
        direction1="d1"
    if event.keysym=="Left":
        direction1="q1"

def DIRECTION2 (event):
    global direction2
    if event.keysym=="z":
        direction2="z2"
    if event.keysym=="s":
        direction2="s2"
    if event.keysym=="d":
        direction2="d2"
    if event.keysym=="q":
        direction2="q2"



class TIMER(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
                global blocs
                global v
                gtimer=0
                blocs=[]
                n=0
                while win==0:
                        time.sleep(1)
                        gtimer=gtimer+1
                        if gtimer==6:
                                gtimer=0
                                n=n+1
                                if v>0.001:
                                        v=v-0.005
                                for i in range (0,n):
                                        r5=random.randint(0,15)
                                        r6=random.randint(0,15)
                                        time.sleep(0.5)
                                        bloc=canvas.create_rectangle(r5*50,r6*50,r5*50+50,r6*50+50,fill=lcolor[icolor],outline=lcolor[icolor])
                                        blocs.append(bloc)
                                        time.sleep(0.5)
                                        bloc=canvas.create_rectangle(r5*50,r6*50,r5*50+50,r6*50+50,fill="black",outline="black")
                                        blocs.append(bloc)
                                        time.sleep(0.5)
                                        bloc=canvas.create_rectangle(r5*50,r6*50,r5*50+50,r6*50+50,fill=lcolor[icolor],outline=lcolor[icolor])
                                        bloc=canvas.create_rectangle(r5*50,r6*50,r5*50+50,r6*50+50,fill=lcolor[icolor],outline=lcolor[icolor])
                                        blocs.append(bloc)
                                
    
class MoveAuto1(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global x1; global y1; global lmoto1; 
            while win==0:
                if direction1=="z1":
                    y1=y1-3
                    if y1<0:
                        y1=800
                if direction1=="s1":
                    y1=y1+3
                    if y1>800:
                        y1=0
                if direction1=="d1":
                    x1=x1+3
                    if x1>800:
                        x1=0
                if direction1=="q1":
                    x1=x1-3
                    if x1<0:
                        x1=800
                time.sleep(v)
                moto1=canvas.create_rectangle(x1-5,y1-5,x1+5,y1+5,fill=lcolor[icolor1],outline=lcolor[icolor1])
                canvas.update()
                lmoto1.append(moto1)
                if len(lmoto1)>100:
                    canvas.delete(lmoto1[0])
                    del lmoto1[0]

class MoveAuto2(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            global x2; global y2; global lmoto2
            while win==0:
                if direction2=="z2":
                    y2=y2-3
                    if y2<0:
                        y2=800
                if direction2=="s2":
                    y2=y2+3
                    if y2>800:
                        y2=0
                if direction2=="d2":
                    x2=x2+3
                    if x2>800:
                        x2=0
                if direction2=="q2":
                    x2=x2-3
                    if x2<0:
                        x2=800
                time.sleep(v)
                moto2=canvas.create_rectangle(x2-5,y2-5,x2+5,y2+5,fill=lcolor[icolor2],outline=lcolor[icolor2])
                canvas.update()
                lmoto2.append(moto2)
                if len(lmoto2)>100:
                    canvas.delete(lmoto2[0])
                    del lmoto2[0]

class TIMERIA(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
                global direction2
                di=["z2","s2","d2","q2"]
                r2=random.randint(1,3)
                r3=random.randint(1,5)
                timer=0
                timer2=0
                while win==0:
                        time.sleep(1)
                        timer=timer+1
                        timer2=timer2+1
                        if timer==r2:
                                a=len(canvas.find_overlapping(x2,y2-11,x2,y2-150))#z
                
                                b=len(canvas.find_overlapping(x2,y2+11,x2,y2+150))#s
                                        
                                c=len(canvas.find_overlapping(x2+11,y2,x2+150,y2))#d
                                        
                                d=len(canvas.find_overlapping(x2-11,y2,x2-150,y2))#q
                                bestoption =[a,b,c,d]
                                bestoption.sort()
                                
                                if bestoption[0]==a and direction2!="z2" :
                                        choix=0
                                elif bestoption[0]==b and direction2!="s2":
                                        choix=1
                                elif bestoption[0]==c and direction2!="d2":
                                        choix=2
                                elif bestoption[0]==d and direction2!="q2":
                                        choix=3
                                direction2=di[choix]
                                r2=random.randint(1,5)
                                timer=0
                        if timer2==r3:
                                timer2=0
                                r4=random.randint(0,1)
                                if r4==0:
                                        if y2-y1<0:
                                                direction2="s2"
                                        else:
                                                direction2="z2"
                                if r4==1:
                                        if x2-x1<0:
                                                direction2="d2"
                                        else:
                                                direction2="q2"
                        
class IA(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
                global direction2
                while win==0:
                        a=len(canvas.find_overlapping(x2,y2-11,x2,y2-150))#z
                
                        b=len(canvas.find_overlapping(x2,y2+11,x2,y2+150))#s
                                        
                        c=len(canvas.find_overlapping(x2+11,y2,x2+150,y2))#d
                                        
                        d=len(canvas.find_overlapping(x2-11,y2,x2-150,y2))#q
                        
                        if direction2=="z2":
                                if len(canvas.find_overlapping(x2,y2-10,x2,y2-30))>1:
                                        if d>c:
                                                direction2="d2"
                                        elif d<c:
                                                direction="q2"
                                        else :
                                                r1=random.randint(0,1)
                                                if r1==0:
                                                        direction2="d2"
                                                else:
                                                        direction2="q2"
                                        
                        if direction2=="s2":
                                if len(canvas.find_overlapping(x2,y2+10,x2,y2+30))>1:
                                        if d>c:
                                                direction2="d2"
                                        elif d<c:
                                                direction="q2"
                                        else :
                                                r1=random.randint(0,1)
                                                if r1==0:
                                                        direction2="d2"
                                                else:
                                                        direction2="q2"
                        if direction2=="d2":
                                if len(canvas.find_overlapping(x2+10,y2,x2+30,y2))>1:
                                        if b>a:
                                                direction2="z2"
                                        elif b<a:
                                                direction="s2"
                                        else :
                                                r1=random.randint(0,1)
                                                if r1==0:
                                                        direction2="z2"
                                                else:
                                                        direction2="s2"
                        if direction2=="q2":
                                if len(canvas.find_overlapping(x2-10,y2,x2-30,y2))>1:
                                        if b>a:
                                                direction2="z2"
                                        elif b<a:
                                                direction="s2"
                                        else :
                                                r1=random.randint(0,1)
                                                if r1==0:
                                                        direction2="z2"
                                                else:
                                                        direction2="s2"

def BG():
    global x3; global y3; global x4; global y4
    for i in range(1,17):
        canvas.create_line(0,i*50,800,i*50,fill=lcolor[icolor])
    for i in range(1,17):
        canvas.create_line(i*50,0,i*50,800,fill=lcolor[icolor])
    time.sleep(1)
                
def CAR():
    i3= PhotoImage(file='./text/3.png')
    t3=canvas.create_image(400, 400, image=i3)
    canvas.update()
    time.sleep(1)
    canvas.delete(t3)
    i2= PhotoImage(file='./text/2.png')
    t2=canvas.create_image(400, 400, image=i2)
    canvas.update()
    time.sleep(1)
    canvas.delete(t2)
    i1= PhotoImage(file='./text/1.png')
    t1=canvas.create_image(400, 400, image=i1)
    canvas.update()
    time.sleep(1)
    canvas.delete(t1)
    go= PhotoImage(file='./text/go.png')
    tgo=canvas.create_image(400, 400, image=go)
    canvas.update()
    time.sleep(0.5)
    canvas.delete(tgo)
    canvas.update()
    
    
def PLAY ():
    if setup==0:
        canvas.delete(ALL)
        canvas.update()
        BG()
        moto1=canvas.create_rectangle(x1-5,y1-5,x1+5,y1+5,fill=lcolor[icolor1],outline=lcolor[icolor1])
        moto2=canvas.create_rectangle(x2-5,y2-5,x2+5,y2+5,fill=lcolor[icolor2],outline=lcolor[icolor2])
        lmoto1.append(moto1)
        lmoto2.append(moto2)
        canvas.update()
        CAR()
        startautomove1=MoveAuto1()
        startautomove1.start()
        startautomove2=MoveAuto2()
        startautomove2.start()
        startcheckdead1=CheckDead1()
        startcheckdead1.start()
        startcheckdead2=CheckDead2()
        startcheckdead2.start()
        timer=TIMER()
        timer.start()
        if bot1==0:
                canvas.bind_all('<z>', DIRECTION2)
                canvas.bind_all('<s>', DIRECTION2)
                canvas.bind_all('<q>', DIRECTION2)
                canvas.bind_all('<d>', DIRECTION2)
        if bot1==1:
                canvas.unbind_all('<z>')
                canvas.unbind_all('<s>')
                canvas.unbind_all('<q>')
                canvas.unbind_all('<d>')
                ia=IA()
                ia.start()
                timeria=TIMERIA()
                timeria.start()




def CLIC2 (event):
    global setup
    global icolor1
    global icolor2
    global canvas2
    global tbot
    global tplayer
    global bot1
    X=event.x
    Y=event.y
    if 160<X<340 and 400<Y<450:
        rootsettings.destroy()
        setup=0
    if 200<X<250 and 125<Y<175:
        icolor1=icolor1-1
        if icolor1<0:
             icolor1=len(lcolor)-1
        rendu1=canvas2.create_rectangle(275,125,325,175,fill=lcolor[icolor1],outline=lcolor[icolor1])
    if 350<X<400 and 125<Y<175 :
        icolor1=icolor1+1
        if icolor1>len(lcolor)-1:
             icolor1=0
        rendu1=canvas2.create_rectangle(275,125,325,175,fill=lcolor[icolor1],outline=lcolor[icolor1])
    if 200<X<250 and 300<Y<350:
        icolor2=icolor2-1
        if icolor2<0:
             icolor2=len(lcolor)-1
        rendu2=canvas2.create_rectangle(275,300,325,350,fill=lcolor[icolor2],outline=lcolor[icolor2])
    if 350<X<400 and 300<Y<350:
        icolor2=icolor2+1
        if icolor2>len(lcolor)-1:
             icolor2=0
        rendu2=canvas2.create_rectangle(275,300,325,350,fill=lcolor[icolor2],outline=lcolor[icolor2])
    if (350<X<400 and 215<Y<265) or (100<X<150 and 215<Y<265):
        canvas2.create_rectangle(160,215,340,265,fill="black")
        if bot1==0:
                bot1=1
                tbot=canvas2.create_image(250,240,image=bot)
        elif bot1==1:
                tplayer=canvas2.create_image(250,240,image=player)
                bot1=0
                
        
    
def CLIC (event):
    global setup
    global canvas2
    global Credits
    X=event.x
    Y=event.y
    if 250<X<550 and 450<Y<550:
        PLAY()
    if 175<X<625 and 575<Y<625 and setup==0:
        global rootsettings
        setup=1
        rootsettings=tkinter.Toplevel(root)
        rootsettings.overrideredirect(1)
        canvas2=Canvas(rootsettings,width=500,height=500,bg="black")
        canvas2.pack()
        canvas2.bind('<ButtonRelease>',CLIC2)
        tsettings=canvas2.create_image(250, 50, image=settings)
        tplayer1mini=canvas2.create_image(75,150,image=player1mini)
        tplayer2mini=canvas2.create_image(75,325,image=player2mini)
        rendu1=canvas2.create_rectangle(275,125,325,175,fill=lcolor[icolor1],outline=lcolor[icolor1])
        rendu2=canvas2.create_rectangle(275,300,325,350,fill=lcolor[icolor2],outline=lcolor[icolor2])
        if bot1==0:
                tplayer=canvas2.create_image(250,240,image=player)
        else:
                tbot=canvas2.create_image(250,240,image=bot)  
        canvas2.create_polygon((200,150),(250,125),(250,175),outline="white",width=2,activefill="#2a2a2a")
        canvas2.create_polygon((400,150),(350,125),(350,175),outline="white",width=2,activefill="#2a2a2a")
        canvas2.create_polygon((100,240),(150,265),(150,215),outline="white",width=2,activefill="#2a2a2a")
        canvas2.create_polygon((400,240),(350,265),(350,215),outline="white",width=2,activefill="#2a2a2a")
        canvas2.create_polygon((200,325),(250,300),(250,350),outline="white",width=2,activefill="#2a2a2a")
        canvas2.create_polygon((400,325),(350,300),(350,350),outline="white",width=2,activefill="#2a2a2a")
        tsave=canvas2.create_image(250,425,image=save,activeimage=save2)
        #canvas2.create_rectangle(350,215,400,265,outline="red")
    if 150<X<650 and 175<Y<325:
        rootcredits=tkinter.Toplevel(root)
        canvas3=Canvas(rootcredits,width=500,height=500,bg="black")
        canvas3.pack()
        tcredit=canvas3.create_image(250,50,image=credit)
        tidea=canvas3.create_image(150,125,image=idea)
        tboby1=canvas3.create_image(425,125,image=boby1)
        tprogram=canvas3.create_image(150,225,image=program)
        tboby2=canvas3.create_image(425,225,image=boby2)
        twidea=canvas3.create_image(250,325,image=widea)
        tpapy=canvas3.create_image(250,425,image=papy)
        

        
        

       
def ECHAP (event):
    global win
    global x1; global y1; global lmoto1; global dead1; global direction1
    global x2; global y2; global lmoto2; global dead2; global direction2
    global x3; global y3; global x4; global y4; global icolor
    if win==1:
        canvas.delete(ALL)
        x1= 770
        y1= 770
        x2=30
        y2=30
        win=0
        lmoto1=[]
        lmoto2=[]
        dead1=[]
        dead2=[]
        direction1="q1"
        direction2="d2"
        x3=0
        y3=800
        x4=0
        y4=0
        icolor=random.randint(0,len(lcolor)-1)
        time.sleep(3)
        PLAY()



                

canvas=Canvas(width=800,height=800,bg="black")
canvas.pack()

for i in range(-1600,2000,20):
        canvas.create_line(i,800,400,600,fill="red")
h=5
for i in range(0,10):
        canvas.create_line(0,650+h,800,650+h,fill="red")
        h=1.5*h
canvas.create_rectangle(0,650,800,600,fill="black")
canvas.create_line(0,650,800,650,fill="red",width=3)

for i in range(-1600,2000,20):
        canvas.create_line(i,0,400,200,fill="#42d9f4")
h=5
for i in range(0,10):
        canvas.create_line(0,150-h,800,150-h,fill="#42d9f4")
        h=1.5*h
canvas.create_rectangle(0,150,800,200,fill="black")
canvas.create_line(0,150,800,150,fill="#42d9f4",width=3)

logo = PhotoImage(file='./text/logo2.png')
logo2= PhotoImage(file='./text/logo.png')
logo1=canvas.create_image(400, 250, image=logo,activeimage=logo2)
textplay= PhotoImage(file='./text/play.png')
textplay2= PhotoImage(file='./text/play2.png')
textplay1=canvas.create_image(400, 500, image=textplay,activeimage=textplay2)

tsettings=canvas.create_image(400, 590, image=settings,activeimage=settings2)

#canvas.create_rectangle(150,175,650,325,outline="red")

canvas.bind_all('<Up>', DIRECTION1)
canvas.bind_all('<Down>', DIRECTION1)
canvas.bind_all('<Left>', DIRECTION1)
canvas.bind_all('<Right>', DIRECTION1)
canvas.bind('<ButtonRelease>',CLIC)
canvas.bind_all('<Escape>',ECHAP)


root.mainloop()
