from tkinter import *
import tkinter
import random
import time
import threading

#VARIABLES=====================================================================================================
#=====================================================================================================
#=====================================================================================================

x=random.randint(0,1000)
y=random.randint(0,1000)
bg=0
cl=0
fd=0
draw=0
ldraw=[]
rdmfcl1=1
rdmfcl2=1
rdmfcl3=1
rdmfcl4=1
rdmfcl5=1

hmg1=1
hmg2=1
#FENETRE=========================================================================================================
#=====================================================================================================
#=====================================================================================================

root=tkinter.Tk()
fen=tkinter.Frame(bg="black")
drawingframe=tkinter.LabelFrame(fen,bg="black",text="Drawing",fg="white")
btframe=tkinter.LabelFrame(fen,bg="black",text="Random and Fun",fg="white")


#COULEUR=========================================================================================================
#=====================================================================================================
#=====================================================================================================

lcolor = ['white','gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

lcolor2=['black','white','dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4']

#FREE_DRAW=====================================================================================================
#=====================================================================================================
#=====================================================================================================
def changepencil():
    global fd
    if fd==0:
        fd=1
        button0.config(text="Square")
    elif fd==1:
        fd=0
        button0.config(text="Circle")
    
    
def Clic(event):
    global free
    X=event.x
    Y=event.y
    if fd==0:
        draw=canvas.create_oval(X-((1/2)*int(width0.get())),Y-((1/2)*int(width0.get())),X+((1/2)*int(width0.get())),Y+((1/2)*int(width0.get())),fill=v.get(),outline=v.get())
    if fd==1:
        draw=canvas.create_rectangle(X-((1/2)*int(width0.get())),Y-((1/2)*int(width0.get())),X+((1/2)*int(width0.get())),Y+((1/2)*int(width0.get())),fill=v.get(),outline=v.get())
    ldraw.append(draw)
    
ffreedraw=tkinter.Frame(drawingframe,bg="black")
button0=tkinter.Button(ffreedraw,text="Circle",command=changepencil)
button0.pack(side=tkinter.LEFT)
listecolor = sorted(lcolor2)
v = StringVar()
v.set(listecolor[0])
color0 = OptionMenu(ffreedraw, v, *listecolor)
color0.pack(side=tkinter.LEFT)
width0=tkinter.Scale(ffreedraw, orient='horizontal', from_=1, to=200,resolution=5, tickinterval=50, length=150,label='Size',bg='black',fg="white")
width0.pack(side=tkinter.LEFT)
ffreedraw.pack()
            
#LINE RANDOM=========================================================================================================
#=====================================================================================================
#=====================================================================================================
def rdmfillcolor1():
    global rdmfcl1
    if rdmfcl1==0:
        rdmfcl1=1
        randomfillcolor1.config(text="Random Fill Color : Enable")
    elif rdmfcl1==1:
        rdmfcl1=0
        randomfillcolor1.config(text="Random Fill Color : Disabled")
        
def randomline ():

    for i in range(0,int(number1.get())):
        global x
        global y
        global cl
        c=random.randint(-35,35)
        d=random.randint(0,1)
        cl+=1
        if cl>(len(lcolor2)-1):
            cl=cl-(len(lcolor2)-1)
        color=lcolor2[cl]
        if d==0:
            a=c ; b=0
        if d==1:
            a=0 ; b=c
        if rdmfcl1==1:
            draw=canvas.create_line(x,y,x+a,y+b,fill=color,width=int(width1.get()))
        else :
            draw=canvas.create_line(x,y,x+a,y+b,fill="black",width=int(width1.get()))
        ldraw.append(draw)
        x=x+a
        y=y+b
        if x>1000:
            x=0
        if x<0:
            x=1000
        if y>1000:
            y=0
        if y<0:
            y=1000
        time.sleep(0.01)
        canvas.update()

frandomline=tkinter.Frame(btframe,bg="black")
button1=tkinter.Button(frandomline,text="Random Line",command=randomline)
button1.pack(side=tkinter.LEFT)
randomfillcolor1=tkinter.Button(frandomline,text="Random Fill Color : Enable",command=rdmfillcolor1)
randomfillcolor1.pack(side=tkinter.LEFT)
number1=tkinter.Scale(frandomline, orient='horizontal', from_=1, to=1000,resolution=100, tickinterval=500, length=100,label='Number of line',bg='black',fg="white")
number1.pack(side=tkinter.LEFT)
width1=tkinter.Entry(frandomline)
width1.pack(side=tkinter.LEFT)
frandomline.pack()

#RANDOMRECT=========================================================================================================
#=====================================================================================================
#=====================================================================================================

def rdmfillcolor2():
    global rdmfcl2
    if rdmfcl2==0:
        rdmfcl2=1
        randomfillcolor2.config(text="Random Fill Color : Enable")
    elif rdmfcl2==1:
        rdmfcl2=0
        randomfillcolor2.config(text="Random Fill Color : Disabled")
        
def homog1 ():
    global hmg1
    if hmg1==0:
        hmg1=1
        homogene1.config(text="homogeneity: Enable")
    elif hmg1==1:
        hmg1=0
        homogene1.config(text="homogeneity: Disabled")
        
def randomrect():
    for i in range (0,int(number2.get())):
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        a=random.randint(-1000+x,1000-x)
        b=random.randint(-1000+y,1000-y)
        cl=random.randint(0,len(lcolor2)-1)
        cl2=random.randint(0,len(lcolor2)-1)
        if hmg1==1:
            cl2=cl
        if rdmfcl2==1:
            draw=canvas.create_rectangle(x,y,x+a,x+b,fill=lcolor2[cl2],outline=lcolor2[cl],width=int(width2.get()))
        else :
             draw=canvas.create_rectangle(x,y,x+a,x+b,outline=lcolor2[cl],width=int(width2.get()))
        ldraw.append(draw)
        time.sleep(0.1)
        canvas.update()

frandomrect=tkinter.Frame(btframe,bg="black")
button2=tkinter.Button(frandomrect,text="Random Rectangle",command=randomrect)
button2.pack(side=tkinter.LEFT)
randomfillcolor2=tkinter.Button(frandomrect,text="Random Fill Color : Enable",command=rdmfillcolor2)
randomfillcolor2.pack(side=tkinter.LEFT)
homogene1=tkinter.Button(frandomrect,text="homogeneity : Enable",command=homog1)
homogene1.pack(side=tkinter.LEFT)
number2=tkinter.Scale(frandomrect, orient='horizontal', from_=1, to=100,resolution=10, tickinterval=50, length=100,label='Number of rectangle',bg='black',fg="white")
number2.pack(side=tkinter.LEFT)
width2=tkinter.Entry(frandomrect)
width2.pack(side=tkinter.LEFT)
frandomrect.pack()

#RANDOMARC=========================================================================================================
#=====================================================================================================
#=====================================================================================================

def rdmfillcolor3():
    global rdmfcl3
    if rdmfcl3==0:
        rdmfcl3=1
        randomfillcolor3.config(text="Random Fill Color : Enable")
    elif rdmfcl3==1:
        rdmfcl3=0
        randomfillcolor3.config(text="Random Fill Color : Disabled")

def homog2 ():
    global hmg2
    if hmg2==0:
        hmg1=2
        homogene2.config(text="homogeneity: Enable")
    elif hmg2==1:
        hmg2=0
        homogene2.config(text="homogeneity: Disabled")

def randomarc():
    for i in range (0,int(number3.get())):
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        a=random.randint(-1000+x,1000-x)
        b=random.randint(-1000+y,1000-y)
        c=random.randint(-180,180)
        cl=random.randint(0,len(lcolor2)-1)
        cl2=random.randint(0,len(lcolor2)-1)
        if hmg2==1:
            cl2=cl
        if rdmfcl3==1:
            draw=canvas.create_arc(x,y,x+a,x+b,fill=lcolor2[cl2],outline=lcolor2[cl],width=int(width3.get()),start=c)
        else :
            draw=canvas.create_arc(x,y,x+a,x+b,outline=lcolor2[cl],width=int(width3.get()),start=c)
        ldraw.append(draw)
        time.sleep(0.1)
        canvas.update()

frandomarc=tkinter.Frame(btframe,bg="black")
button3=tkinter.Button(frandomarc,text="Random Arc",command=randomarc)
button3.pack(side=tkinter.LEFT)
randomfillcolor3=tkinter.Button(frandomarc,text="Random Fill Color : Enable",command=rdmfillcolor3)
randomfillcolor3.pack(side=tkinter.LEFT)
homogene2=tkinter.Button(frandomarc,text="homogeneity : Enable",command=homog2)
homogene2.pack(side=tkinter.LEFT)
number3=tkinter.Scale(frandomarc, orient='horizontal', from_=1, to=100,resolution=10, tickinterval=50, length=100,label='Number of arc',bg='black',fg="white")
number3.pack(side=tkinter.LEFT)
width3=tkinter.Entry(frandomarc)
width3.pack(side=tkinter.LEFT)
frandomarc.pack()

#RANDOMOVAL=========================================================================================================
#=====================================================================================================
#=====================================================================================================
def rdmfillcolor4():
    global rdmfcl4
    if rdmfcl4==0:
        rdmfcl4=1
        randomfillcolor4.config(text="Random Fill Color : Enable")
    elif rdmfcl4==1:
        rdmfcl4=0
        randomfillcolor4.config(text="Random Fill Color : Disabled")

def randomoval():
    for i in range (0,int(number4.get())):
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        a=random.randint(-1000+x,1000-x)
        b=random.randint(-1000+y,1000-y)
        cl=random.randint(0,len(lcolor2)-1)
        cl2=random.randint(0,len(lcolor2)-1)
        if rdmfcl3==1:
            draw=canvas.create_oval(x,y,x+a,x+b,fill=lcolor2[cl2],outline=lcolor2[cl],width=int(width4.get()))
        else :
            draw=canvas.create_arc(x,y,x+a,x+b,outline=lcolor2[cl],width=int(width3.get()),start=c)
        ldraw.append(draw)
        time.sleep(0.1)
        canvas.update()

frandomoval=tkinter.Frame(btframe,bg="black")
button4=tkinter.Button(frandomoval,text="Random Oval",command=randomoval)
button4.pack(side=tkinter.LEFT)
randomfillcolor4=tkinter.Button(frandomoval,text="Random Fill Color : Enable",command=rdmfillcolor4)
randomfillcolor4.pack(side=tkinter.LEFT)
number4=tkinter.Scale(frandomoval, orient='horizontal', from_=1, to=100,resolution=10, tickinterval=50, length=100,label='Number of oval',bg='black',fg="white")
number4.pack(side=tkinter.LEFT)
width4=tkinter.Entry(frandomoval)
width4.pack(side=tkinter.LEFT)
frandomoval.pack()

#RANDOMPOLYGONE=========================================================================================================
#=====================================================================================================
#=====================================================================================================
def rdmfillcolor5():
    global rdmfcl5
    if rdmfcl5==0:
        rdmfcl5=1
        randomfillcolor5.config(text="Random Fill Color : Enable")
    elif rdmfcl5==1:
        rdmfcl5=0
        randomfillcolor5.config(text="Random Fill Color : Disabled")

def randompolygone():
    for i in range (0,int(number5.get())):
        pts=[]
        pt=()
        n=random.randint(3,11)
        cl=random.randint(0,len(lcolor2)-1)
        cl2=random.randint(0,len(lcolor2)-1)
        for i in range(0,n):
            x=random.randint(0,1000)
            y=random.randint(0,1000)
            pt=(x,y)
            pts.append(pt)
        if rdmfcl3==1:
             draw=canvas.create_polygon(pts,fill=lcolor2[cl2],outline=lcolor2[cl],width=int(width5.get()))
        else :
            draw=canvas.create_polygon(pts,fill="white",outline=lcolor2[cl],width=int(width5.get()))
        ldraw.append(draw)
        time.sleep(0.1)
        canvas.update()

frandompolygone=tkinter.Frame(btframe,bg="black")
button5=tkinter.Button(frandompolygone,text="Random Polygon",command=randompolygone)
button5.pack(side=tkinter.LEFT)
randomfillcolor5=tkinter.Button(frandompolygone,text="Random Fill Color : Enable",command=rdmfillcolor5)
randomfillcolor5.pack(side=tkinter.LEFT)
number5=tkinter.Scale(frandompolygone, orient='horizontal', from_=1, to=100,resolution=10, tickinterval=50, length=100,label='Number of polygon',bg='black',fg="white")
number5.pack(side=tkinter.LEFT)
width5=tkinter.Entry(frandompolygone)
width5.pack(side=tkinter.LEFT)
frandompolygone.pack()


#BACKGROUND=========================================================================================================
#=====================================================================================================
#=====================================================================================================
        
def bgonoff():
    global bg
    if bg==1:
        bg=0
        buttonbg.config(text="Background OFF")
    elif bg==0:
        bg=1
        background=Background()
        background.start() 
        buttonbg.config(text="Background ON")

def whitebackground():
    canvas.config(bg="white")

def blackbackground():
    canvas.config(bg="black")

def randombackground():
    cl=random.randint(0,len(lcolor2)-1)
    canvas.config(bg=lcolor2[cl])
    
class Background(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)	
        def run (self):
            colorbg=0
            while bg==1:
                canvas.config(bg=lcolor[colorbg])
                canvas.update()
                time.sleep(0.01)
                colorbg=colorbg+1
                if colorbg>(len(lcolor)-1):
                    colorbg=colorbg-(len(lcolor)-1)
                    lcolor.reverse()
                
def background():
    background=Background()
    background.start()   

fbackground=tkinter.Frame(btframe,bg="black")
buttonbg=tkinter.Button(fbackground,text="Background ON/OFF",command=bgonoff)
buttonbg.pack(side=tkinter.LEFT)
buttonbg2=tkinter.Button(fbackground,text="White Background",command=whitebackground)
buttonbg2.pack(side=tkinter.LEFT)
buttonbg3=tkinter.Button(fbackground,text="Black Background",command=blackbackground)
buttonbg3.pack(side=tkinter.LEFT)
buttonbg4=tkinter.Button(fbackground,text="Random Background",command=randombackground)
buttonbg4.pack(side=tkinter.LEFT)
fbackground.pack()


#OTHER=========================================================================================================
#=====================================================================================================
#=====================================================================================================
    
def reset():
    canvas.config(bg="white")
    canvas.delete(ALL)

def remove():
    canvas.delete(ldraw[-1])
    del ldraw[-1]

other=tkinter.Frame(btframe,bg="black")
buttonreset=tkinter.Button(other,text="Reset",command=reset)
buttonreset.pack(side=tkinter.LEFT)
buttonremove=tkinter.Button(other,text="Remove last draw",command=remove)
buttonremove.pack(side=tkinter.LEFT)
other.pack()



#INTERFACE=========================================================================================================
#=====================================================================================================
#=====================================================================================================        

drawingframe.pack(pady=10,padx=10)
canvas=Canvas(fen,width=1000,height=1000,bg="white",borderwidth=0)
canvas.pack(side=tkinter.RIGHT,pady=10,padx=10)
canvas.bind('<B1-Motion>', Clic)
canvas.bind('<Button-1>', Clic)
#.pack fenetre principal=======
btframe.pack(side=tkinter.LEFT,pady=10,padx=10)
fen.pack()

root.mainloop()
