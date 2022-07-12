from tkinter import*
import qrcode

window=Tk()

def generateqr():
    d1=n1.get()
    d2=n2.get()

    myqr='Name is' + d1 + 'Age is' + d2
    getcode=qrcode.make(myqr)
    getcode.save("myqr.png")

l1=Label(window,text="Enter The Name : ")
n1=Entry(window,width=30)
l1.pack()
n1.pack()

l2=Label(window,text="Enter The Age : ")
n2=Entry(window)
l2.pack()
n2.pack()

b=Button(window,text="Generate QR Code",command=generateqr)
b.pack()
window.mainloop()
