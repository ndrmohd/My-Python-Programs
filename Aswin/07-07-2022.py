from tkinter import *

def addnumbers():
    res=int(e1.get())+int(e2.get())
    result.set(res)
def subnumbers():
    res=int(e1.get())-int(e2.get())
    result.set(res)
def mulnumbers():
    res=int(e1.get())*int(e2.get())
    result.set(res)
def divnumbers():
    res=int(e1.get())/int(e2.get())
    result.set(res)


window = Tk()
result=StringVar()    
window.title("Calculator")
window.config(bg="black")

l1=Label(window,text="1st number  " ,bg="orange").grid(row=0)
l2=Label(window,text="2nd number  " ,bg="orange").grid(row=1)
l3=Label(window,text="Result" ,bg="orange").grid(row=2)
res=Label(window,text='',textvariable=result).grid(row=2,column=1)

e1=Entry(window)
e2=Entry(window)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b=Button(window,text="ADD",command=addnumbers,bg="#8099E9")
b.grid(row=0,column=2)
b=Button(window,text="SUB",command=subnumbers,bg="skyblue")
b.grid(row=0,column=3)
b=Button(window,text="MUL",command=mulnumbers,bg="#75FD92")
b.grid(row=1,column=2)
b=Button(window,text="DIV",command=divnumbers,bg="#E99DCB")
b.grid(row=1,column=3)
window.mainloop()