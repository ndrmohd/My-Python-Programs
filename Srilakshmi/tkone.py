from cProfile import label
from cgitb import text
from doctest import master
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN
from tkinter.ttk import Entry 
main=Tk()
l1=label(main, text="number1").grid(Row=0)
l2=label(main,text="number2").grid(Row=1)
e1=Entry(main)
e2=Entry(main)
e1.grid(row=0,column=1)
e1.grid(row=1,column=1)
main.mainloop()