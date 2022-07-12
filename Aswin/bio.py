import string
from tkinter import *
from unittest import result
import qrcode

def bio():
    data=(e1.get())(e2.get())  
    result.set(data)

window=Tk()
window.title("QrBio")

l1=Label(window,text="Enter your name ").grid(row=0)
l2=Label(window,text="Enter your age ").grid(row=1)
img= (qrcode.make(bio))
img.save('bio.png')

e1=Entry(window)
e2=Entry(window)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b=Button(window,text="Convert",command=bio)
b.grid(row=2)

window.mainloop()