from cmath import cos, sin, sqrt, tan
def sum(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mult(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2)
def floordiv(num1,num2):
    print(num1//num2)
def sinn():
    print(sin(num1))
def cosn():
    print(cos(num1))
def tann():
    print(tan(num1))
def power():
    print(num1**num2)
def squarert():
    print(sqrt(num1))
print("CALCULATOR")
login=input("Y or N")
while login=="y" or login=="Y":
        print('1-add \n 2-substraction \n 3-multiplication \n 4-division \n 5-floor division \n 6-sin \n 7-cos \n 8-tan \n 9-power \n 10- square root')
        function=input("select the function")
        if function=="1" or function=="add" or function=="2" or function=='substraction' or function=="3" or function=="multiplication" or function=="4" or function=="division" or function=="5" or function=="floor division":
            num1=int(input("enter num1"))  
            num2=int(input("enter num2"))
            if function=="1" or function=="add": 
                sum(num1,num2)
            elif function=="2" or function=='substraction':
                    sub(num1,num2)
            elif function=="3" or function=="multiplication":
                    mult(num1,num2)
            elif function=="4" or function=="division":
                    div(num1,num2)
            elif function=="5" or function=="floor division":
                floordiv(num1,num2)
        elif function=="6" or function=="sin" or function=="7" or function=="cos" or function=="8" or function=="tan" or function=="10" or function=="square root":
            num1=int(input("entre a num1"))
            if function=="6" or function=="sin":
                    sinn(num1)
            elif function=="7" or function=="cos":
                    cosn(num1)
            elif function=="8" or function=="tan":
                    tann(num1)
            elif function=="9" or function=="power":
                    power(num1,num2)
            elif function=="10" or function=="square root":
                    squarert(num1)
        quitting=input("Do you want to quit")
        if quitting=="yes" or quitting=="y" or quitting=="Y":
                print("Thank you")
                exit()
        elif quitting=="no" or quitting=="n" or quitting=="N":
                continue
if login=="N" or login=="n":
    exit()
    

