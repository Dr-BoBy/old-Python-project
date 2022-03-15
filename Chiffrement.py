import tkinter
from tkinter import *

src="abcdefghijklmnopqrstuvwxyz"

text="..."
text_cle="..."
all_cle=[]

def cpt():
    global all_cle
    global text
    all_cle=[]
    try :
        msg_output=[]
        cle_ok=0
        msg=(Entry_message.get()).lower()
        cle_a=int(Entry_cle_a.get())
        cle_b=int(Entry_cle_b.get())
        for i in range(len(msg)):
            index=cle_a*src.index(msg[i])+cle_b
            while index>=len(src):
                index-=len(src)
            msg_output.append(src[index])
        text="".join(msg_output)
        Label_message_final2.config(text=text)
    except:
        text="Une des données n'est pas prise en charge par le programme"
        Label_message_final2.config(text=text)
    for cle_a2 in range(0,100):
        for cle_b2 in range(0,100):
            cle_ok=0
            for i in range(len(msg)):
                if (cle_a2*(cle_a*src.index(msg[i])+cle_b)+cle_b2)%26==src.index(msg[i]):
                    cle_ok+=1
            if cle_ok==len(msg):
                all_cle.append((str(cle_a2),str(cle_b2)))
    text_cle=" ".join(all_cle[0])
    Label_cle2.config(text=text_cle)

def dcpt():
    global all_cle
    global text
    try :
        msg_output=[]
        msg=(Entry_message.get()).lower()
        cle_a=int(Entry_cle_a.get())
        cle_b=int(Entry_cle_b.get())
        for i in range(len(msg)):
            index=cle_a*src.index(msg[i])+cle_b
            while index>=len(src):
                index-=len(src)
            msg_output.append(src[index])
        text="".join(msg_output)
        Label_message_final2.config(text=text)
        Label_cle2.config(text="...")
    except:
        text="Une des données n'est pas prise en charge par le programme"
        Label_message_final2.config(text=text)
        
def print_all_cle():
    for i in range(len(all_cle)):
        print(all_cle[i][0],all_cle[i][1])

def copier():
    root.clipboard_clear()
    root.clipboard_append(text)
    
root=Tk()

Frame_cle=tkinter.Frame()

Frame_cle_a=tkinter.Frame(Frame_cle)
Label_cle_a=tkinter.Label(Frame_cle_a,text="Coefficient de la clé")
Label_cle_a.pack(side=tkinter.LEFT)
Entry_cle_a=tkinter.Entry(Frame_cle_a)
Entry_cle_a.pack(side=tkinter.LEFT)
Frame_cle_a.pack()

Frame_cle_b=tkinter.Frame(Frame_cle)
Label_cle_b=tkinter.Label(Frame_cle_b,text="Ordonnée de la clé")
Label_cle_b.pack(side=tkinter.LEFT)
Entry_cle_b=tkinter.Entry(Frame_cle_b)
Entry_cle_b.pack(side=tkinter.LEFT)
Frame_cle_b.pack()

Frame_cle.pack()


Frame_all_message=tkinter.Frame()

Frame_message=tkinter.Frame(Frame_all_message)
Label_message=tkinter.Label(Frame_message,text="Message original :")
Label_message.pack()
Entry_message=tkinter.Entry(Frame_message,)
Entry_message.pack()
Frame_message.pack(side=tkinter.LEFT)

Frame_message_final=tkinter.Frame(Frame_all_message)
Label_message_final=tkinter.Label(Frame_message_final,text="Message chiffré/déchiffré :")
Label_message_final.pack()
Label_message_final2=tkinter.Label(Frame_message_final,text=text)
Label_message_final2.pack()
Frame_message_final.pack(side=tkinter.LEFT)

Frame_cle=tkinter.Frame(Frame_all_message)
Label_cle=tkinter.Label(Frame_cle,text="Clé de déchiffrage :")
Label_cle.pack()
Label_cle2=tkinter.Label(Frame_cle,text=text_cle)
Label_cle2.pack()
Frame_cle.pack(side=tkinter.LEFT)
Frame_all_message.pack()


Frame_button=tkinter.Frame()
Button_cpt=tkinter.Button(Frame_button,text="Chiffrer",command=cpt)
Button_cpt.pack(side=tkinter.LEFT)
Button_dcpt=tkinter.Button(Frame_button,text="Dechiffrer",command=dcpt)
Button_dcpt.pack(side=tkinter.LEFT)
Button_copier=tkinter.Button(Frame_button,text="Copier le texte final",command=copier)
Button_copier.pack(side=tkinter.LEFT)
Button_cle=tkinter.Button(Frame_button,text="Afficher toutes les clés",command=print_all_cle)
Button_cle.pack(side=tkinter.LEFT)
Frame_button.pack()


root.mainloop()
