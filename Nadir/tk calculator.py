from tkinter import *

def addNumber():
    sum=a+b

add=Tk()
add.title('Calculator')
a=Label(text='Enter the 1st number: ')
b=Label(text='Enter the 2nd number: ')
e1=Entry(add)
e2=Entry(add)

btn=Button(add,text='Add',width=10,command=addNumber)
a.pack()
b.pack()
btn.pack()
add.mainloop()