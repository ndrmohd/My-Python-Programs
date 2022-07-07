from tkinter import *
window=Tk()
window.title("My Calculator")
window.geometry("600x400")
window.config(bg="yellow")
def sum():
    sum=int(e1.get())+int(e2.get())
    result.set(sum)
def sub():
    sub=int(e1.get())-int(e2.get())
    result.set(sub)
def mul():
    mul=int(e1.get())*int(e2.get())
    result.set(mul)
def div():
    div=int(e1.get())/int(e2.get())
    result.set(div)
def pow():
    pow=int(e1.get())**int(e2.get())
    result.set(pow)
def flr():
    flr=int(e1.get())//int(e2.get())
    result.set(flr)
result=StringVar()

l1=Label(window,text="Number1:",font="50").grid(row=0)
l2=Label(window,text="Number2:",font="50").grid(row=1)
l3=Label(window,text="Result",padx="10",font="50").grid(row=2)
e1=Entry(window)
e2=Entry(window)
e3=Entry(window,textvariable=result)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
btn=Button(window,text="Sum",padx="20",command=sum).grid(row=5,column=1)
btn=Button(window,text="Subtraction",padx="10",command=sub).grid(row=5,column=2)
btn=Button(window,text="Multiply",padx="10",command=mul).grid(row=6,column=1)
btn=Button(window,text="Division",padx="20",command=div).grid(row=6,column=2)
btn=Button(window,text="Power",padx="15",command=pow).grid(row=7,column=1)
btn=Button(window,text="floordivision",padx="10",command=flr).grid(row=7,column=2)
mainloop()