from tkinter import *
import qrcode
window=Tk()
l1=Label(window,text="Name ").grid(row=0)
l2=Label(window,text="age").grid(row=1)
e1=Entry(window,).grid(row=0,column=1)
e2=Entry(window,).grid(row=1,column=1)
bt=Button(text="Generate qrcode").grid(row=2)
details=e1.get(),e2.get()
mycode=qrcode.make(details)
mycode.save("code2.png")
window.mainloop()
