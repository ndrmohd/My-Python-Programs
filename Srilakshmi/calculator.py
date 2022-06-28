from cmath import cos, sin, sqrt, tan
print("CALCULATOR")
login=input("Y or N")
while login=="y" or login=="Y":
        print('1-add \n 2-substraction \n 3-multiplication \n 4-division \n 5-floor division \n 6-sin \n 7-cos \n 8-tan \n 9-power \n 10- square root')
        function=input("select the function")
        if function=="1" or function=="add":
            sum()
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
        elif function=="9" or function=="power":
            num1sq=int(input("enter the number"))
            power=int(input("enter the power"))
            print(num1sq**power)
        elif function=="10" or function=="square root":
            num1sqr=int(input("enter the number"))
            print(sqrt(num1sqr))
        quitting=input("Do you want to quit")
        if quitting=="yes" or quitting=="y" or quitting=="Y":
            print("Thank you")
            exit()
        elif quitting=="no" or quitting=="n" or quitting=="N":
            continue
if login=="N" or login=="n":
    exit()
    

