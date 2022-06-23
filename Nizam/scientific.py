import math
print('Welcome to My Calcultaor')
status=input('Do you want to Continue in our calculator:\nY or N:')
while status=='Y' or status=='y':
    option=input(('1.  Addition\n2.  Subtraction\n3.  Multiplication\n4.  Division\n5.  Power\n6.  Squareroot\n7.  Sin\n8.  Cos\n9.  Tan\n10. Floor Division\n11. Exit\nEnter your Option:'))
    if  option=='1' or option=='Addition' or option=='add':
        num1=int(input("Enter the first number:"))
        num2=int(input("Enter the second number:"))
        print('Sum=',num1+num2)
    elif option=='2' or option=='Subtraction' or option=='sub':
        num1=int(input("Enter the first number:"))
        num2=int(input("Enter the second number:"))
        print('Difference=',num1-num2)
    elif option=='3' or option=='Multiplication' or option=='mul':
        num1=int(input("Enter the first number:"))
        num2=int(input("Enter the second number:"))
        print('Product=',num1*num2)
    elif option=='4' or option=='Division' or option=='div':
        num1=int(input("Enter the first number:"))
        num2=int(input("Enter the second number:"))
        print('Quotient=',num1/num2)
    elif option=='5' or option=='Power' or option=='power':
        num1=int(input("Enter the number:"))
        num2=int(input("Enter the power:"))
        print('Power=',num1**num2)
    elif option=='6' or option=='Squareroot' or option=='sqrt':
        num1=int(input("Enter the number:"))
        print('Squareroot=',math.sqrt(num1))
    elif option=='7' or option=='Sin' or option=='sin':
        num1=int(input("Enter the number:"))
        print('Sin=',math.sin(num1))
    elif option=='8' or option=='Cos' or option=='cos':
        num1=int(input("Enter the number:"))
        print('Cos=',math.cos(num1))
    elif option=='9' or option=='Tan' or option=='tan':
        num1=int(input("Enter the number:"))
        print('Tan=',math.tan(num1))
    elif option=='10' or option=='Floordivision' or option=='flrdiv':
        num1=int(input("Enter the first number:"))
        num2=int(input("Enter the second number:"))
        print('Floordivision=',num1//num2)
    elif option=='11' or option=='Exit' or option=='exit':
        print('Thank you For Using our Calculator\nHave A Nice day!!')
        exit()
    else:
        print('Invalid Option')
if status=='N' or status=='n':
    exit()