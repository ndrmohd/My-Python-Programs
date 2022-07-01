from module import modules
print("CALCULATOR")
login=input("Y or N")
while login=="y" or login=="Y":
        print('1-add \n 2-substraction \n 3-multiplication \n 4-division \n 5-floor division \n 6-sin \n 7-cos \n 8-tan \n 9-power \n 10- square root')
        function=input("select the function")
        if function=="1" or function=="add" or function=="2" or function=='substraction' or function=="3" or function=="multiplication" or function=="4" or function=="division" or function=="5" or function=="floor division":
            num1=int(input("enter num1"))  
            num2=int(input("enter num2"))
            if function=="1" or function=="add": modules.sum(num1,num2)
            elif function=="2" or function=='substraction':modules.sub(num1,num2)
            elif function=="3" or function=="multiplication":modules.mult(num1,num2)
            elif function=="4" or function=="division":modules.div(num1,num2)
            elif function=="5" or function=="floor division":modules.floordiv(num1,num2)
        elif function=="6" or function=="sin" or function=="7" or function=="cos" or function=="8" or function=="tan" or function=="10" or function=="square root":
            num1=int(input("entre a num1"))
            if function=="6" or function=="sin":modules.sinn(num1)
            elif function=="7" or function=="cos":modules.cosn(num1)
            elif function=="8" or function=="tan":modules.tann(num1)
            elif function=="9" or function=="power":modules.power(num1,num2)
            elif function=="10" or function=="square root":modules.squarert(num1)
        quitting=input("Do you want to quit")
        if quitting=="yes" or quitting=="y" or quitting=="Y":
                print("Thank you")
                exit()
        elif quitting=="no" or quitting=="n" or quitting=="N":
                continue
if login=="N" or login=="n":
    exit()
    

