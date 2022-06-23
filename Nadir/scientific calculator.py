import math
print('Welcome to MY CALCULATOR')
status=input('Do you want to Login..? \nYes or No: ')
while status=='Yes' or status=='Y' or status=='yes' or status=='y':
    option=(input(' 1  . Addition\n 2  . Subtraction\n 3  . Product\n 4  . Division\n 5  . Square root\n 6  . Power\n 7  . Sin\n 8  . Cos\n 9  . Tan\n 10 . Floor Division\n 11 . Exit\nSelect the operation=>'))
    if option=='1' or option=='Addition' or option=='add':
        num1=int(input('Enter the first number= '))
        num2=int(input('Enter the second number= '))
        print('Sum of the values= ',num1+num2)
    elif option=='2' or option=='Difference' or option=='sub':
        num1=int(input('Enter the first number= '))
        num2=int(input('Enter the second number= '))
        print('Difference of the values= ',num1-num2)
    elif option=='3' or option=='Product' or option=='product' or option=='mul':
        num1=int(input('Enter the first number= '))
        num2=int(input('Enter the second number= '))
        print('Product of the values =',num1*num2)
    elif option=='4' or option=='Division' or option=='divison':
        num1=int(input('Enter the first number= '))
        num2=int(input('Enter the second number= '))
        print('Quotient of the values= ', num1/num2)
        print('Remainder of the values= ', num1%num2)
    elif option=='5' or option=='Square root' or option=='square root' or option=='sqrt':
        num1=int(input('Enter the number= '))
        print('Square root of the number is= ',math.sqrt(num1))
    elif option=='6' or option=='Power' or option=='power':
        num1=int(input('Enter the number= '))
        num2=int(input('Enter the power= '))
        print('Power of the number is= ',num1**num2)
    elif option=='7' or option=='Sin' or option=='sin':
        num1=int(input('Enter the number= '))
        print(math.sin(num1))
    elif option=='8' or option=='Cos' or option=='cos':
        num1=int(input('Enter the number= '))
        print(math.cos(num1))
    elif option=='9' or option=='Tan' or option=='tan':
        num1=int(input('Enter the number= '))
        print(math.tan(num1))
    elif option=='10' or option=='Floor division':
        num1=int(input('Enter the first number= '))
        num2=int(input('Enter the second number= '))
        print('Floor division of the values= ',num1//num2)
    elif option=='11':
        print('Thank you for using this calculator..!! \nHave a nice day..!!')
        exit()
    else: print('Invalid option..!')
if status=='No' or status=='N' or status=='no' or status=='n': exit()