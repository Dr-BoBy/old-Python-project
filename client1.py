import socket
import threading
import tkinter
import time

hote = "localhost"
port = 12800
name = "BoBy"
detectmsg=1
codeco="co"

msg_a_envoyer = b""

class MSGRECU(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run (self):
            while detectmsg==1:
                msg_recu = connexion_avec_serveur.recv(1024)
                print(msg_recu.decode())
            
def SENDMSG ():
    msg_a_envoyer = Emsg.get()
    msg=[name]
    msg.append(msg_a_envoyer)
    msg=" : ".join(msg)
    msg = msg.encode()
    connexion_avec_serveur.send(msg)


root=tkinter.Tk()
Emsg=tkinter.Entry(text="")
Emsg.pack()
btsend=tkinter.Button(text="Envoyer",command=SENDMSG)
btsend.pack()


connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
msg=[name]
msg.append("vient de se connecter")
msg=" ".join(msg)
msg = msg.encode()
connexion_avec_serveur.send(msg)
    
msgrecu=MSGRECU()
msgrecu.start()



