from cmath import cos, sin, sqrt, tan
from logging import root
import math
while calc=="new":
        a="there"
        print(a)
        print("1","add","\n","2","substraction","\n","3","multiplication","\n","4","division","\n","5","floor division","\n","6","sin","\n","7","cos","\n","8","tan","\n","9","square","\n","10","square root")
        function=input("select the function")
        if function=="1" or function=="add":
            num1=int(input("enter the number"))
            num2=int(input("enter the number"))
            print(num1+num2)
        elif function=="2" or function=='substraction':
            num1s=int(input("enter the number"))
            num2s=int(input("enter the number"))
            print(num1s-num2s)
        elif function=="3" or function=="multiplication":
            num1m=int(input("enter the number"))
            num2m=int(input("enter the number"))
            print(num1m*num2m)
        elif function=="4" or function=="division":
            num1d=int(input("enter the number"))
            num2d=int(input("enter the number"))
            print(num1d/num2d)
        elif function=="5" or function=="floor division":
            num1f=int(input("enter the number"))
            num2f=int(input("enter the number"))
            print(num1f//num2f)
        elif function=="6" or function=="sin":
            num1si=int(input("enter the number"))
            print(sin(num1si))
        elif function=="7" or function=="cos":
            num1co=int(input("enter the number"))
            print(cos(num1co))
        elif function=="8" or function=="tan":
            num1ta=int(input("enter the number"))
            print(tan(num1ta))
        elif function=="9" or function=="square":
            num1sq=int(input("enter the number"))
            print(num1sq*num1sq)
        elif function=="10" or function=="square root":
            num1sqr=int(input("enter the number"))
            print(sqrt(num1sqr))
