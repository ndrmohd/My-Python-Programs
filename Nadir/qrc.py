from tkinter import *
import qrcode
qr=Tk()
qr.geometry("450x300")

def generateqr():
    name=num1.get()
    age=f1.get()

    mycode='Name: '+name+'\nAge: '+age

    getcode=qrcode.make(mycode)
    getcode.save("QR Code.png")


l1=Label(qr,text="Enter the name: ")
num1=Entry(qr,width=30)
num1.pack()
l1.pack()

l2=Label(qr,text="Enter the age: ")
f1=Entry(qr)
f1.pack()
l2.pack()

btn=Button(qr,text="Generate QR Code: ",width=30,command=generateqr)
btn.pack()
qr.mainloop()