import math
print("WELCOME TO THE CALCULATOR")
status=input('DO YOU WANT TO LOGIN ? \n YES OR NO : ')
while status=="YES" or status=="yes":
    option=input("Select Your Choice\n1 . ADDITION\n2 . SUBTRACTION\n3 . DIVISION\n4 . MULTIPLIACTION\n5 . SQURE\n6 . POWER\n7 . FLOOR DIVISION\n8 . COS\n9 . TAN\n10. FLOOR DIVISION\n11. EXIT\n")   
    if option=='1'or'2'or'3'or'4'or'5'or'6'or'7':
        a=int(input('Enter the first number= '))
        b=int(input('Enter the second number= '))
        def sum():print("Sum of the value is",a+b)
        def sub():print("Difference of the value is",a-b)
        def div():print("Quotient of the value is",a/b)
        def mul():print("Product of the value is",a*b)
        def sqr():print("Power of the value is",a**a)
        def pwr():print("Squre Root of the value is",math.sqrt(a))
        def flrdiv():print("FloorDivision of the value is",a//b) 
        if option=='1' or option=='ADDITION' or option=='addition':sum()    
        elif option=='2' or option=='SUBTRACTION' or option=='subtraction':sub()
        elif option=='3' or option=='DIVISION' or option=='division':div()
        elif option=='4' or option=='MULTIPLIACTION' or option=='multiplication':mul()
        elif option=='5' or option=='SQURE' or option=='squre':sqr()
        elif option=='6' or option=='POWER' or option=='power':pwr()
        elif option=='7' or option=='FLOOR DIVISION' or option=='floor division':
            flrdiv()
        exit()
    if option=='8'or'9'or'10':
        def cos():print("Cos of the value is",math.cos(a))
        def tan():print("Tan of the value is",math.tan(a))
        def sin():print("Sin of the value is",math.sin(a)) 
        a=int(input('Enter the number= '))
        if option=='8' or option=='COS' or option=='cos':cos()
        elif option=='9' or option=='TAN' or option=='tan':tan()
        elif option=='10' or option=='sin' or option=='sin':sin()
        if option=='11' or option=='EXIT' or option=='exit':
            a=("Thank You For Using This Calculator ")
            print("Thank You For Using This Calculator ")
            exit()

