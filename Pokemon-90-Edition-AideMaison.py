Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> M0=["+","-","-","-","-","-","-","-","-","+","|","%","║"," ","&","&"," ","║","%","|","|"," ","╚","═","═","═","═","╝"," ","|","|"," "," "," "," "," "," "," "," ","|","|","░"," "," "," "," "," "," ","●","|","|"," "," "," "," "," "," "," ","ⓞ","|","|"," "," "," "," "," "," "," ","●","|","|","═","═","═","╗"," "," "," "," ","|","|"," ","&"," ","║"," "," "," ","%","|","+","-","-","-","-","-"," ","-","-","+"]

y=0
T=M0
print(" ")
for i in range (0,10):
    print(" ".join(T[y:y+10]))
    y=y+10
y=0

