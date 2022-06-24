import math
print("WELCOME TO THE CALCULATOR")
status=input('DO YOU WANT TO LOGIN ? \n YES OR NO : ')
while status=="YES" or status=="yes":
    option=input("Select Your Choice\n1 . ADDITION\n2 . SUBTRACTION\n3 . DIVISION\n4 . MULTIPLIACTION\n5 . SQURE\n6 . POWER\n7 . SIN\n8 . COS\n9 . TAN\n10. FLOOR DIVISION\n11. EXIT\n")
    if option=='1' or option=='ADDITION' or option=='addition':
        a=int(input('Enter the first number= '))
        b=int(input('Enter the second number= '))
        print("Sum of the value is",a+b)

    if option=='2' or option=='SUBTRACTION' or option=='subtraction':
        a=int(input('Enter the first number= '))
        b=int(input('Enter the second number= '))
        print("Difference of the value is",a-b)

    elif option=='3' or option=='DIVISION' or option=='division':
        a=int(input('Enter the first number= '))
        b=int(input('Enter the second number= '))
        print("Quotient of the value is",a/b)

    elif option=='4' or option=='MULTIPLIACTION' or option=='multiplication':
        a=int(input('Enter the first number= '))
        b=int(input('Enter the second number= '))
        print("Product of the value is",a*b)

    elif option=='5' or option=='SQURE' or option=='squre':
        a=int(input('Enter the  number= '))
        b=int(input('Enter the  Powerr= '))
        print("Power of the value is",a*a)

    elif option=='6' or option=='POWER' or option=='power':
        a=int(input('Enter the number= '))
        print("Squre Root of the value is",math.sqrt(a))

    elif option=='7' or option=='SIN' or option=='sin':
        a=int(input('Enter the number= '))
        print("Sin of the value is",math.sin(a))

    elif option=='8' or option=='COS' or option=='cos':
        a=int(input('Enter the number= '))
        print("Cos of the value is",math.cos(a))

    elif option=='9' or option=='TAN' or option=='tan':
        a=int(input('Enter the number= '))
        print("Tan of the value is",math.tan(a))

    elif option=='10' or option=='FLOOR DIVISION' or option=='floor division':
        a=int(input('Enter the first number= '))
        b=int(input('Enter the second number= '))
        print("FloorDivision of the value is",a//b)

    elif option=='11' or option=='EXIT' or option=='exit':
        a=("Thank You For Using This Calculator ")
        print("Thank You For Using This Calculator ")
        exit()
    else:
        print('Invalid operation')
if status=='no' or status=='NO':exit()

    
