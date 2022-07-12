from tkinter import*
import qrcode
top = Tk()
top.geometry("450x300")

def generateqr():
    name=n1.get()
    age=f1.get()

    mycode='Name:'+name+'\nAge:'+age

    getcode=qrcode.make(mycode)

    getcode.save("trycode.png")

    
l1=Label(top,text="ENTER THE NAME:")
n1=Entry(top,width=30)
n1.pack()
l1.pack()

l2=Label(top,text="ENTER THE AGE:")
f1=Entry(top)
f1.pack()
l2.pack()

btn=Button(top,text="GENERATE QR CODE",bg="blue",width=30,command=generateqr)
btn.pack()
top.mainloop()
    