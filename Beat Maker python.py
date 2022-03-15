from tkinter import *
import tkinter
import time
import winsound
import threading


root = tkinter.Tk (className="8 Beat Maker v0,1")
  
    
#BPM======================================
def ChangeBPM () :
    t2BPM.config(text = int(eBPM.get()))
    BPM=int(eBPM.get())

fbpm=tkinter.Frame()
tBPM= tkinter.Label (fbpm,text ="TBN (time between notes) =")
tBPM.pack(side=tkinter.LEFT)
t2BPM= tkinter.Label (fbpm,text =" ? ")
t2BPM.pack(side=tkinter.LEFT)
eBPM = tkinter.Entry (fbpm)
eBPM.pack(side=tkinter.LEFT)
bBPM = tkinter.Button (fbpm,text = "Set",command = ChangeBPM )
bBPM.pack (side=tkinter.LEFT)
fbpm.pack()

#variable===============================

v11= tkinter.IntVar ()
v12= tkinter.IntVar ()
v13= tkinter.IntVar ()
v14= tkinter.IntVar ()
v15= tkinter.IntVar ()
v16= tkinter.IntVar ()
v17= tkinter.IntVar ()
v18= tkinter.IntVar ()

v21= tkinter.IntVar ()
v22= tkinter.IntVar ()
v23= tkinter.IntVar ()
v24= tkinter.IntVar ()
v25= tkinter.IntVar ()
v26= tkinter.IntVar ()
v27= tkinter.IntVar ()
v28= tkinter.IntVar ()

v31= tkinter.IntVar ()
v32= tkinter.IntVar ()
v33= tkinter.IntVar ()
v34= tkinter.IntVar ()
v35= tkinter.IntVar ()
v36= tkinter.IntVar ()
v37= tkinter.IntVar ()
v38= tkinter.IntVar ()

v41= tkinter.IntVar ()
v42= tkinter.IntVar ()
v43= tkinter.IntVar ()
v44= tkinter.IntVar ()
v45= tkinter.IntVar ()
v46= tkinter.IntVar ()
v47= tkinter.IntVar ()
v48= tkinter.IntVar ()

v51= tkinter.IntVar ()
v52= tkinter.IntVar ()
v53= tkinter.IntVar ()
v54= tkinter.IntVar ()
v55= tkinter.IntVar ()
v56= tkinter.IntVar ()
v57= tkinter.IntVar ()
v58= tkinter.IntVar ()

v61= tkinter.IntVar ()
v62= tkinter.IntVar ()
v63= tkinter.IntVar ()
v64= tkinter.IntVar ()
v65= tkinter.IntVar ()
v66= tkinter.IntVar ()
v67= tkinter.IntVar ()
v68= tkinter.IntVar ()

v71= tkinter.IntVar ()
v72= tkinter.IntVar ()
v73= tkinter.IntVar ()
v74= tkinter.IntVar ()
v75= tkinter.IntVar ()
v76= tkinter.IntVar ()
v77= tkinter.IntVar ()
v78= tkinter.IntVar ()

v81= tkinter.IntVar ()
v82= tkinter.IntVar ()
v83= tkinter.IntVar ()
v84= tkinter.IntVar ()
v85= tkinter.IntVar ()
v86= tkinter.IntVar ()
v87= tkinter.IntVar ()
v88= tkinter.IntVar ()

freq1=0;freq2=0;freq3=0;freq4=0;freq5=0;freq6=0;freq7=0;freq8=0
bit1=[];bit2=[];bit3=[];bit4=[];bit5=[];bit6=[];bit7=[];bit8=[]
gbit1=[freq1]
gbit2=[freq2]
gbit3=[freq3]
gbit4=[freq4]
gbit5=[freq5]
gbit6=[freq6]
gbit7=[freq7]
gbit8=[freq8]

#BIT=======================================

def editb1():
    
    def ChangeFreq1 () :
        global freq1
        t2freq1.config(text = int(efreq1.get()))
        freq1=int(efreq1.get())
    def ChangeFreq2 () :
        global freq2
        t2freq2.config(text = int(efreq2.get()))
        freq2=int(efreq2.get())
    def ChangeFreq3 () :
        global freq3
        t2freq3.config(text = int(efreq3.get()))
        freq3=int(efreq3.get())
    def ChangeFreq4 () :
        global freq4
        t2freq4.config(text = int(efreq4.get()))
        freq4=int(efreq4.get())
    def ChangeFreq5 () :
        global freq5
        t2freq5.config(text = int(efreq5.get()))
        freq5=int(efreq5.get())
    def ChangeFreq6 () :
        global freq6
        t2freq6.config(text = int(efreq6.get()))
        freq6=int(efreq6.get())
    def ChangeFreq7 () :
        global freq7
        t2freq7.config(text = int(efreq7.get()))
        freq7=int(efreq7.get())
    def ChangeFreq8 () :
        global freq8
        t2freq8.config(text = int(efreq8.get()))
        freq8=int(efreq8.get())

    def playbit1():
        global bit1
        bit1=[int(efreq1.get()),v11.get(),v12.get(),v13.get(),v14.get(),v15.get(),v16.get(),v17.get(),v18.get()]
        for i in range(0,9):
            if bit1[i]==1:
                 winsound.Beep(bit1[0],100)
            time.sleep((60/int(eBPM.get()))-0.1)
    def playbit2 ():
        global bit2
        bit2=[int(efreq2.get()),v21.get(),v22.get(),v23.get(),v24.get(),v25.get(),v26.get(),v27.get(),v28.get()]
        for i in range(0,9):
            if bit2[i]==1:
                winsound.Beep(bit2[0],100)
            time.sleep((60/int(eBPM.get()))-0.1)
    def playbit3 ():
        global bit3
        bit3=[int(efreq3.get()),v31.get(),v32.get(),v33.get(),v34.get(),v35.get(),v36.get(),v37.get(),v38.get()]
        for i in range(0,9):
            if bit3[i]==1:
                winsound.Beep(bit3[0],100)
            time.sleep((60/int(eBPM.get()))-0.1)
    def playbit4 ():
        global bit4
        bit4=[int(efreq4.get()),v41.get(),v42.get(),v43.get(),v44.get(),v45.get(),v46.get(),v47.get(),v48.get()]
        for i in range(0,9):
            if bit4[i]==1:
                winsound.Beep(bit4[0],100)
            time.sleep((60/int(eBPM.get()))-0.1)
    def playbit5 ():
        global bit5
        bit5=[int(efreq5.get()),v51.get(),v52.get(),v53.get(),v54.get(),v55.get(),v56.get(),v57.get(),v58.get()]
        for i in range(0,9):
            if bit5[i]==1:
                winsound.Beep(bit5[0],100)
            time.sleep((60/int(eBPM.get()))-0.1)
    def playbit6 ():
        global bit6
        bit6=[int(efreq6.get()),v61.get(),v62.get(),v63.get(),v64.get(),v65.get(),v66.get(),v67.get(),v68.get()]
        for i in range(0,9):
            if bit6[i]==1:
                winsound.Beep(bit6[0],100)
            time.sleep((60/int(eBPM.get()))-0.1)
    def playbit7 ():
        global bit7
        bit7=[int(efreq7.get()),v71.get(),v72.get(),v73.get(),v74.get(),v75.get(),v76.get(),v77.get(),v78.get()]
        for i in range(0,9):
            if bit7[i]==1:
                winsound.Beep(bit7[0],100)
            time.sleep((60/int(eBPM.get()))-0.1)
    def playbit8 ():
        global bit8
        bit8=[int(efreq8.get()),v81.get(),v82.get(),v83.get(),v84.get(),v85.get(),v86.get(),v87.get(),v88.get()]
        for i in range(0,9):
            if bit8[i]==1:
                winsound.Beep(bit8[0],100)
            time.sleep((60/int(eBPM.get()))-0.1)



            
    class ThreadBit1(threading.Thread):
        def __init__(self,bit1):
            threading.Thread.__init__(self)
            self.bit1=bit1    
        def run (self):
            for i in range(1,len(self.bit1)):
                if self.bit1[i]==1:
                     winsound.Beep(self.bit1[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
    class ThreadBit2(threading.Thread):
        def __init__(self,bit2):
            threading.Thread.__init__(self)
            self.bit2=bit2
        def run (self):
            for i in range(1,len(self.bit2)):
                if self.bit2[i]==1:
                     winsound.Beep(self.bit2[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
    class ThreadBit3(threading.Thread):
        def __init__(self,bit3):
            threading.Thread.__init__(self)
            self.bit3=bit3
        def run (self):
            for i in range(1,len(self.bit3)):
                if self.bit3[i]==1:
                     winsound.Beep(self.bit3[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
    class ThreadBit4(threading.Thread):
        def __init__(self,bit4):
            threading.Thread.__init__(self)
            self.bit4=bit4	
        def run (self):
            for i in range(1,len(self.bit4)):
                if self.bit4[i]==1:
                     winsound.Beep(self.bit4[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
    class ThreadBit5(threading.Thread):
        def __init__(self,bit5):
            threading.Thread.__init__(self)
            self.bit5=bit5	
        def run (self):
            for i in range(1,len(self.bit5)):
                if self.bit5[i]==1:
                     winsound.Beep(self.bit5[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
    class ThreadBit6(threading.Thread):
        def __init__(self,bit6):
            threading.Thread.__init__(self)
            self.bit6=bit6	
        def run (self):
            for i in range(1,len(self.bit6)):
                if self.bit6[i]==1:
                     winsound.Beep(self.bit6[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
    class ThreadBit7(threading.Thread):
        def __init__(self,bit7):
            threading.Thread.__init__(self)
            self.bit7=bit7	
        def run (self):
            for i in range(1,len(self.bit7)):
                if self.bit7[i]==1:
                     winsound.Beep(self.bit7[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
    class ThreadBit8(threading.Thread):
        def __init__(self,bit8):
            threading.Thread.__init__(self)
            self.bit8=bit8	
        def run (self):	
            for i in range(1,len(self.bit8)):
                if self.bit8[i]==1:
                     winsound.Beep(self.bit8[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
            
    def play():
        global bit1;global bit2;global bit3;global bit4;global bit5;global bit6;global bit7;global bit8
        bit1=[int(efreq1.get()),v11.get(),v12.get(),v13.get(),v14.get(),v15.get(),v16.get(),v17.get(),v18.get()]
        bit2=[int(efreq2.get()),v21.get(),v22.get(),v23.get(),v24.get(),v25.get(),v26.get(),v27.get(),v28.get()]
        bit3=[int(efreq3.get()),v31.get(),v32.get(),v33.get(),v34.get(),v35.get(),v36.get(),v37.get(),v38.get()]
        bit4=[int(efreq4.get()),v41.get(),v42.get(),v43.get(),v44.get(),v45.get(),v46.get(),v47.get(),v48.get()]
        bit5=[int(efreq5.get()),v51.get(),v52.get(),v53.get(),v54.get(),v55.get(),v56.get(),v57.get(),v58.get()]
        bit6=[int(efreq6.get()),v61.get(),v62.get(),v63.get(),v64.get(),v65.get(),v66.get(),v67.get(),v68.get()]
        bit7=[int(efreq7.get()),v71.get(),v72.get(),v73.get(),v74.get(),v75.get(),v76.get(),v77.get(),v78.get()]
        bit8=[int(efreq8.get()),v81.get(),v82.get(),v83.get(),v84.get(),v85.get(),v86.get(),v87.get(),v88.get()]
        PlayThreadBit1= ThreadBit1([int(efreq1.get()),v11.get(),v12.get(),v13.get(),v14.get(),v15.get(),v16.get(),v17.get(),v18.get()])
        PlayThreadBit2= ThreadBit2([int(efreq2.get()),v21.get(),v22.get(),v23.get(),v24.get(),v25.get(),v26.get(),v27.get(),v28.get()])
        PlayThreadBit3= ThreadBit3([int(efreq3.get()),v31.get(),v32.get(),v33.get(),v34.get(),v35.get(),v36.get(),v37.get(),v38.get()])
        PlayThreadBit4= ThreadBit4([int(efreq4.get()),v41.get(),v42.get(),v43.get(),v44.get(),v45.get(),v46.get(),v47.get(),v48.get()])
        PlayThreadBit5= ThreadBit5([int(efreq5.get()),v51.get(),v52.get(),v53.get(),v54.get(),v55.get(),v56.get(),v57.get(),v58.get()])
        PlayThreadBit6= ThreadBit6([int(efreq6.get()),v61.get(),v62.get(),v63.get(),v64.get(),v65.get(),v66.get(),v67.get(),v68.get()])
        PlayThreadBit7= ThreadBit7([int(efreq7.get()),v71.get(),v72.get(),v73.get(),v74.get(),v75.get(),v76.get(),v77.get(),v78.get()])
        PlayThreadBit8= ThreadBit8([int(efreq8.get()),v81.get(),v82.get(),v83.get(),v84.get(),v85.get(),v86.get(),v87.get(),v88.get()])
        PlayThreadBit1.start()
        PlayThreadBit2.start()
        PlayThreadBit3.start()
        PlayThreadBit4.start()
        PlayThreadBit5.start()
        PlayThreadBit6.start()
        PlayThreadBit7.start()
        PlayThreadBit8.start()
        
    def add():
        global x;global y
        global gbit1;global gbit2;global gbit3;global gbit4;global gbit5;global gbit6;global gbit7;global gbit8
        gbit1[0]=freq1
        gbit2[0]=freq2
        gbit3[0]=freq3
        gbit4[0]=freq4
        gbit5[0]=freq5
        gbit6[0]=freq6
        gbit7[0]=freq7
        gbit8[0]=freq8
        for i in range (1,9):
            gbit1.append(bit1[i])
        for i in range (1,9):
            gbit2.append(bit2[i])
        for i in range (1,9):
            gbit3.append(bit3[i])
        for i in range (1,9):
            gbit4.append(bit4[i])
        for i in range (1,9):
            gbit5.append(bit5[i])
        for i in range (1,9):
            gbit6.append(bit6[i])
        for i in range (1,9):
            gbit7.append(bit7[i])
        for i in range (1,9):
            gbit8.append(bit8[i])
        t2playg.config(text=len(gbit1)-1)
        canvasg.config(width=(len(gbit1)*10))
           
        x=((len(gbit1)-8)*10)
        print(x)
        y=3
        for i in range (1,9):
            if bit1[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
            else:
                x=x+10
        y=y+5
        x=((len(gbit1)-8)*10)
        print(x)
        for i in range (1,9):
            if bit2[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
            else:
                x=x+10
        y=y+5
        x=((len(gbit1)-8)*10)
        for i in range (1,9):
            if bit3[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
            else:
                x=x+10
        y=y+5
        x=((len(gbit1)-8)*10)
        print(x)
        for i in range (1,9):
            if bit4[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
            else:
                x=x+10
        y=y+5
        x=((len(gbit1)-8)*10)
        print(x)
        for i in range (1,9):
            if bit5[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
            else:
                x=x+10
        y=y+5
        x=((len(gbit1)-8)*10)
        print(x)
        for i in range (1,9):
            if bit6[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
            else:
                x=x+10
        y=y+5
        x=((len(gbit1)-8)*10)
        print(x)
        for i in range (1,9):
            if bit7[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
            else:
                x=x+10
        y=y+5
        x=((len(gbit1)-8)*10)
        print(x)
        for i in range (1,9):
            if bit8[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
            else:
                x=x+10
        
        
            
        print(gbit1);print(gbit2);print(gbit3);print(gbit4);print(gbit5);print(gbit6);print(gbit7);print(gbit8)
    
#bit1=======================   
    fbit=tkinter.Toplevel(root)
    bplay=tkinter.Button(fbit,text= "Check and play the sample",command = play)
    bplay.pack ()
    badd=tkinter.Button(fbit,text= "Add to your beat",command = add)
    badd.pack ()
    tbit1= tkinter.LabelFrame(fbit,text="Bit 1",padx=2,pady=2)

    tfreq1= tkinter.Label (tbit1,text ="frequency (Hz) =")
    tfreq1.pack(side=tkinter.LEFT)
    t2freq1= tkinter.Label (tbit1,text ="?")
    t2freq1.pack(side=tkinter.LEFT)
    efreq1 = tkinter.Entry (tbit1)
    efreq1.pack(side=tkinter.LEFT)
    bfreq1 = tkinter.Button (tbit1,text = "Set",command = ChangeFreq1 )
    bfreq1.pack (side=tkinter.LEFT)

    case11 = tkinter.Checkbutton (tbit1,variable = v11)
    case11.pack(side=tkinter.LEFT)

    case12 = tkinter.Checkbutton (tbit1,variable = v12)
    case12.pack(side=tkinter.LEFT)

    case13 = tkinter.Checkbutton (tbit1,variable = v13)
    case13.pack(side=tkinter.LEFT)

    case14 = tkinter.Checkbutton (tbit1,variable = v14)
    case14.pack(side=tkinter.LEFT)

    case15 = tkinter.Checkbutton (tbit1,variable = v15)
    case15.pack(side=tkinter.LEFT)

    case16 = tkinter.Checkbutton (tbit1,variable = v16)
    case16.pack(side=tkinter.LEFT)

    case17 = tkinter.Checkbutton (tbit1,variable = v17)
    case17.pack(side=tkinter.LEFT)

    case18 = tkinter.Checkbutton (tbit1,variable = v18)
    case18.pack(side=tkinter.LEFT)

    bbit1=tkinter.Button(tbit1,text="Try your bit",command = playbit1)
    bbit1.pack(side=tkinter.LEFT)
    tbit1.pack(expand="yes")

#bit2======================

    tbit2= tkinter.LabelFrame(fbit,text="Bit 2",padx=2,pady=2)

    tfreq2= tkinter.Label (tbit2,text ="frequency (Hz) =")
    tfreq2.pack(side=tkinter.LEFT)
    t2freq2= tkinter.Label (tbit2,text ="?")
    t2freq2.pack(side=tkinter.LEFT)
    efreq2 = tkinter.Entry (tbit2)
    efreq2.pack(side=tkinter.LEFT)
    bfreq2 = tkinter.Button (tbit2,text = "Set",command = ChangeFreq2 )
    bfreq2.pack (side=tkinter.LEFT)

    case21 = tkinter.Checkbutton (tbit2,variable = v21)
    case21.pack(side=tkinter.LEFT)

    case22 = tkinter.Checkbutton (tbit2,variable = v22)
    case22.pack(side=tkinter.LEFT)

    case23 = tkinter.Checkbutton (tbit2,variable = v23)
    case23.pack(side=tkinter.LEFT)

    case24 = tkinter.Checkbutton (tbit2,variable = v24)
    case24.pack(side=tkinter.LEFT)

    case25 = tkinter.Checkbutton (tbit2,variable = v25)
    case25.pack(side=tkinter.LEFT)

    case26 = tkinter.Checkbutton (tbit2,variable = v26)
    case26.pack(side=tkinter.LEFT)

    case27 = tkinter.Checkbutton (tbit2,variable = v27)
    case27.pack(side=tkinter.LEFT)

    case28 = tkinter.Checkbutton (tbit2,variable = v28)
    case28.pack(side=tkinter.LEFT)

    bbit2=tkinter.Button(tbit2,text="Try your bit",command = playbit2)
    bbit2.pack(side=tkinter.LEFT)
    tbit2.pack(expand="yes")

#bit3======================

    tbit3= tkinter.LabelFrame(fbit,text="Bit 3",padx=2,pady=2)

    tfreq3= tkinter.Label (tbit3,text ="frequency (Hz) =")
    tfreq3.pack(side=tkinter.LEFT)
    t2freq3= tkinter.Label (tbit3,text ="?")
    t2freq3.pack(side=tkinter.LEFT)
    efreq3 = tkinter.Entry (tbit3)
    efreq3.pack(side=tkinter.LEFT)
    bfreq3 = tkinter.Button (tbit3,text = "Set",command = ChangeFreq3 )
    bfreq3.pack (side=tkinter.LEFT)

    case31 = tkinter.Checkbutton (tbit3,variable = v31)
    case31.pack(side=tkinter.LEFT)

    case32 = tkinter.Checkbutton (tbit3,variable = v32)
    case32.pack(side=tkinter.LEFT)

    case33 = tkinter.Checkbutton (tbit3,variable = v33)
    case33.pack(side=tkinter.LEFT)

    case34 = tkinter.Checkbutton (tbit3,variable = v34)
    case34.pack(side=tkinter.LEFT)

    case35 = tkinter.Checkbutton (tbit3,variable = v35)
    case35.pack(side=tkinter.LEFT)

    case36 = tkinter.Checkbutton (tbit3,variable = v36)
    case36.pack(side=tkinter.LEFT)

    case37 = tkinter.Checkbutton (tbit3,variable = v37)
    case37.pack(side=tkinter.LEFT)

    case38 = tkinter.Checkbutton (tbit3,variable = v38)
    case38.pack(side=tkinter.LEFT)

    bbit3=tkinter.Button(tbit3,text="Try your bit",command = playbit3)
    bbit3.pack(side=tkinter.LEFT)
    tbit3.pack(expand="yes")

#bit4======================

    tbit4= tkinter.LabelFrame(fbit,text="Bit 4",padx=2,pady=2)

    tfreq4= tkinter.Label (tbit4,text ="frequency (Hz) =")
    tfreq4.pack(side=tkinter.LEFT)
    t2freq4= tkinter.Label (tbit4,text ="?")
    t2freq4.pack(side=tkinter.LEFT)
    efreq4 = tkinter.Entry (tbit4)
    efreq4.pack(side=tkinter.LEFT)
    bfreq4 = tkinter.Button (tbit4,text = "Set",command = ChangeFreq4 )
    bfreq4.pack (side=tkinter.LEFT)

    case41 = tkinter.Checkbutton (tbit4,variable = v41)
    case41.pack(side=tkinter.LEFT)

    case42 = tkinter.Checkbutton (tbit4,variable = v42)
    case42.pack(side=tkinter.LEFT)

    case43 = tkinter.Checkbutton (tbit4,variable = v43)
    case43.pack(side=tkinter.LEFT)

    case44 = tkinter.Checkbutton (tbit4,variable = v44)
    case44.pack(side=tkinter.LEFT)

    case45 = tkinter.Checkbutton (tbit4,variable = v45)
    case45.pack(side=tkinter.LEFT)

    case46 = tkinter.Checkbutton (tbit4,variable = v46)
    case46.pack(side=tkinter.LEFT)

    case47 = tkinter.Checkbutton (tbit4,variable = v47)
    case47.pack(side=tkinter.LEFT)

    case48 = tkinter.Checkbutton (tbit4,variable = v48)
    case48.pack(side=tkinter.LEFT)

    bbit4=tkinter.Button(tbit4,text="Try your bit",command = playbit4)
    bbit4.pack(side=tkinter.LEFT)
    tbit4.pack(expand="yes")

#bit5======================

    tbit5= tkinter.LabelFrame(fbit,text="Bit 5",padx=2,pady=2)

    tfreq5= tkinter.Label (tbit5,text ="frequency (Hz) =")
    tfreq5.pack(side=tkinter.LEFT)
    t2freq5= tkinter.Label (tbit5,text ="?")
    t2freq5.pack(side=tkinter.LEFT)
    efreq5 = tkinter.Entry (tbit5)
    efreq5.pack(side=tkinter.LEFT)
    bfreq5 = tkinter.Button (tbit5,text = "Set",command = ChangeFreq5 )
    bfreq5.pack (side=tkinter.LEFT)

    case51 = tkinter.Checkbutton (tbit5,variable = v51)
    case51.pack(side=tkinter.LEFT)

    case52 = tkinter.Checkbutton (tbit5,variable = v52)
    case52.pack(side=tkinter.LEFT)

    case53 = tkinter.Checkbutton (tbit5,variable = v53)
    case53.pack(side=tkinter.LEFT)

    case54 = tkinter.Checkbutton (tbit5,variable = v54)
    case54.pack(side=tkinter.LEFT)

    case55 = tkinter.Checkbutton (tbit5,variable = v55)
    case55.pack(side=tkinter.LEFT)

    case56 = tkinter.Checkbutton (tbit5,variable = v56)
    case56.pack(side=tkinter.LEFT)

    case57 = tkinter.Checkbutton (tbit5,variable = v57)
    case57.pack(side=tkinter.LEFT)

    case58 = tkinter.Checkbutton (tbit5,variable = v58)
    case58.pack(side=tkinter.LEFT)

    bbit5=tkinter.Button(tbit5,text="Try your bit",command = playbit5)
    bbit5.pack(side=tkinter.LEFT)
    tbit5.pack(expand="yes")

#bit6======================

    tbit6= tkinter.LabelFrame(fbit,text="Bit 6",padx=2,pady=2)

    tfreq6= tkinter.Label (tbit6,text ="frequency (Hz) =")
    tfreq6.pack(side=tkinter.LEFT)
    t2freq6= tkinter.Label (tbit6,text ="?")
    t2freq6.pack(side=tkinter.LEFT)
    efreq6 = tkinter.Entry (tbit6)
    efreq6.pack(side=tkinter.LEFT)
    bfreq6 = tkinter.Button (tbit6,text = "Set",command = ChangeFreq6 )
    bfreq6.pack (side=tkinter.LEFT)

    case61 = tkinter.Checkbutton (tbit6,variable = v61)
    case61.pack(side=tkinter.LEFT)

    case62 = tkinter.Checkbutton (tbit6,variable = v62)
    case62.pack(side=tkinter.LEFT)

    case63 = tkinter.Checkbutton (tbit6,variable = v63)
    case63.pack(side=tkinter.LEFT)

    case64 = tkinter.Checkbutton (tbit6,variable = v64)
    case64.pack(side=tkinter.LEFT)

    case65 = tkinter.Checkbutton (tbit6,variable = v65)
    case65.pack(side=tkinter.LEFT)

    case66 = tkinter.Checkbutton (tbit6,variable = v66)
    case66.pack(side=tkinter.LEFT)

    case67 = tkinter.Checkbutton (tbit6,variable = v67)
    case67.pack(side=tkinter.LEFT)

    case68 = tkinter.Checkbutton (tbit6,variable = v68)
    case68.pack(side=tkinter.LEFT)

    bbit6=tkinter.Button(tbit6,text="Try your bit",command = playbit6)
    bbit6.pack(side=tkinter.LEFT)
    tbit6.pack(expand="yes")
    
#bit7======================

    tbit7= tkinter.LabelFrame(fbit,text="Bit 7",padx=2,pady=2)

    tfreq7= tkinter.Label (tbit7,text ="frequency (Hz) =")
    tfreq7.pack(side=tkinter.LEFT)
    t2freq7= tkinter.Label (tbit7,text ="?")
    t2freq7.pack(side=tkinter.LEFT)
    efreq7 = tkinter.Entry (tbit7)
    efreq7.pack(side=tkinter.LEFT)
    bfreq7 = tkinter.Button (tbit7,text = "Set",command = ChangeFreq7 )
    bfreq7.pack (side=tkinter.LEFT)

    case71 = tkinter.Checkbutton (tbit7,variable = v71)
    case71.pack(side=tkinter.LEFT)

    case72 = tkinter.Checkbutton (tbit7,variable = v72)
    case72.pack(side=tkinter.LEFT)

    case73 = tkinter.Checkbutton (tbit7,variable = v73)
    case73.pack(side=tkinter.LEFT)

    case74 = tkinter.Checkbutton (tbit7,variable = v74)
    case74.pack(side=tkinter.LEFT)

    case75 = tkinter.Checkbutton (tbit7,variable = v75)
    case75.pack(side=tkinter.LEFT)

    case76 = tkinter.Checkbutton (tbit7,variable = v76)
    case76	.pack(side=tkinter.LEFT)

    case77 = tkinter.Checkbutton (tbit7,variable = v77)
    case77.pack(side=tkinter.LEFT)

    case78 = tkinter.Checkbutton (tbit7,variable = v78)
    case78.pack(side=tkinter.LEFT)

    bbit7=tkinter.Button(tbit7,text="Try your bit",command = playbit7)
    bbit7.pack(side=tkinter.LEFT)
    tbit7.pack(expand="yes")

#bit8======================

    tbit8= tkinter.LabelFrame(fbit,text="Bit 8",padx=2,pady=2)

    tfreq8= tkinter.Label (tbit8,text ="frequency (Hz) =")
    tfreq8.pack(side=tkinter.LEFT)
    t2freq8= tkinter.Label (tbit8,text ="?")
    t2freq8.pack(side=tkinter.LEFT)
    efreq8 = tkinter.Entry (tbit8)
    efreq8.pack(side=tkinter.LEFT)
    bfreq8 = tkinter.Button (tbit8,text = "Set",command = ChangeFreq8 )
    bfreq8.pack (side=tkinter.LEFT)

    case81 = tkinter.Checkbutton (tbit8,variable = v81)
    case81.pack(side=tkinter.LEFT)

    case82 = tkinter.Checkbutton (tbit8,variable = v82)
    case82.pack(side=tkinter.LEFT)

    case83 = tkinter.Checkbutton (tbit8,variable = v83)
    case83.pack(side=tkinter.LEFT)

    case84 = tkinter.Checkbutton (tbit8,variable = v84)
    case84.pack(side=tkinter.LEFT)

    case85 = tkinter.Checkbutton (tbit8,variable = v85)
    case85.pack(side=tkinter.LEFT)

    case86 = tkinter.Checkbutton (tbit8,variable = v86)
    case86.pack(side=tkinter.LEFT)

    case87 = tkinter.Checkbutton (tbit8,variable = v87)
    case87.pack(side=tkinter.LEFT)

    case88 = tkinter.Checkbutton (tbit8,variable = v88)
    case88.pack(side=tkinter.LEFT)

    bbit8=tkinter.Button(tbit8,text="Try your bit",command = playbit8)
    bbit8.pack(side=tkinter.LEFT)
    tbit8.pack(expand="yes")


        
#interface================================================
class ThreadGbit1(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            for i in range(1,len(gbit1)):
                if gbit1[i]==1:
                     winsound.Beep(gbit1[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)                
class ThreadGbit2(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            for i in range(1,len(gbit2)):
                if gbit2[i]==1:
                     winsound.Beep(gbit2[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
class ThreadGbit3(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            for i in range(1,len(gbit3)):
                if gbit3[i]==1:
                     winsound.Beep(gbit3[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
class ThreadGbit4(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            for i in range(1,len(gbit4)):
                if gbit4[i]==1:
                     winsound.Beep(gbit4[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
class ThreadGbit5(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            for i in range(1,len(gbit5)):
                if gbit5[i]==1:
                     winsound.Beep(gbit5[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
class ThreadGbit6(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)	
        def run (self):
            for i in range(1,len(gbit6)):
                if gbit6[i]==1:
                     winsound.Beep(gbit6[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
class ThreadGbit7(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            for i in range(1,len(gbit7)):
                if gbit7[i]==1:
                     winsound.Beep(gbit7[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)
class ThreadGbit8(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)	
        def run (self):	
            for i in range(1,len(gbit8)):
                if gbit8[i]==1:
                     winsound.Beep(gbit8[0],100)
                time.sleep((60/int(eBPM.get()))-0.1)

def globalplay():
    PlayThreadGbit1= ThreadGbit1()
    PlayThreadGbit2= ThreadGbit2()
    PlayThreadGbit3= ThreadGbit3()
    PlayThreadGbit4= ThreadGbit4()
    PlayThreadGbit5= ThreadGbit5()
    PlayThreadGbit6= ThreadGbit6()
    PlayThreadGbit7= ThreadGbit7()
    PlayThreadGbit8= ThreadGbit8()
    PlayThreadGbit1.start()
    PlayThreadGbit2.start()
    PlayThreadGbit3.start()
    PlayThreadGbit4.start()
    PlayThreadGbit5.start()
    PlayThreadGbit6.start()
    PlayThreadGbit7.start()
    PlayThreadGbit8.start()

def removesample():
    for i in range (0,8):
        del gbit1[-1];del gbit2[-1];del gbit3[-1];del gbit4[-1];del gbit5[-1];del gbit6[-1];del gbit7[-1];del gbit8[-1]
    print(gbit1);print(gbit2);print(gbit3);print(gbit4);print(gbit5);print(gbit6);print(gbit7);print(gbit8)

    canvasg.delete(ALL)
    
    x=10
    print(x)
    y=3
    for i in range (1,len(gbit1)):
        if gbit1[i]==1:
            canvasg.create_oval(x,y,x+3,y+3,fill="orange")
            x=x+10
        else:
            x=x+10
    y=y+5
    x=10
    print(x)
    for i in range (1,len(gbit2)):
        if gbit2[i]==1:
            canvasg.create_oval(x,y,x+3,y+3,fill="orange")
            x=x+10
        else:
            x=x+10
    y=y+5
    x=10
    for i in range (1,len(gbit3)):
        if gbit3[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
        else:
                x=x+10
    y=y+5
    x=10
    print(x)
    for i in range (1,len(gbit4)):
        if gbit4[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
        else:
                x=x+10
    y=y+5
    x=10
    print(x)
    for i in range (1,len(gbit5)):
        if gbit5[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
        else:
                x=x+10
    y=y+5
    x=10
    print(x)
    for i in range (1,len(gbit6)):
        if gbit6[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
        else:
                x=x+10
    y=y+5
    x=10
    print(x)
    for i in range (1,len(gbit7)):
        if gbit7[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
        else:
                x=x+10
    y=y+5
    x=10
    print(x)
    for i in range (1,len(gbit8)):
        if gbit8[i]==1:
                canvasg.create_oval(x,y,x+3,y+3,fill="orange")
                x=x+10
        else:
                x=x+10

beditb1=tkinter.Button(text= "Create",command= editb1)
beditb1.pack()
fplayg=tkinter.LabelFrame(text="Beat's settings")
bplayg=tkinter.Button(fplayg,text= "Play your beat",command= globalplay)
bplayg.pack(side=tkinter.LEFT)
bremoveg=tkinter.Button(fplayg,text="Remove last sample",command=removesample)
bremoveg.pack(side=tkinter.LEFT)
tplayg=tkinter.Label(fplayg,text="Beat's lenght :")
tplayg.pack(side=tkinter.LEFT)
t2playg=tkinter.Label(fplayg,text=len(gbit1)-1)
t2playg.pack(side=tkinter.LEFT)
t3playg=tkinter.Label(fplayg,text="Times")
t3playg.pack(side=tkinter.LEFT)
fplayg.pack()
ftrackg=tkinter.LabelFrame(text="Beat's track")
canvasg=Canvas(ftrackg,width=(len(gbit1)*10), height=40,background="lightgrey")
canvasg.pack()
ftrackg.pack()








root.mainloop ()

