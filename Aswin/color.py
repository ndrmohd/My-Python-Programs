from cProfile import label
from curses.textpad import Textbox
from logging import root
from tkinter import*
import tkinter
from turtle import width
window = Tk() 
window.title("Calculator")
Canvas=tkinter.Canvas(width=200,height=200)
Canvas.pack()
label(window,Text= "Enter first number ")
label(window,Text= "Enter second number ")
label.pack()
Entry=tkinter.Entry(width=20,height=10)
Entry.pack()
button=tkinter.Button(window,text='Exit',width=10,command=window.destroy)
button.pack()
window.mainloop()