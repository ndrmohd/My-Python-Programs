from tkinter import *
import qrcode
window=Tk()
def qr():
    name=e1.get()
    age=e2.get()
    details=name+age
    mycode=qrcode.make(details)
    mycode.save("code2.png")
l1=Label(window,text="Name").grid(row=0)
l2=Label(window,text="age").grid(row=1)
e1=Entry(window)
e1.grid(row=0,column=1)
e2=Entry(window)
e2.grid(row=1,column=1)
bt=Button(text="Generate qrcode",command=qr).grid(row=2)
window.mainloop()
