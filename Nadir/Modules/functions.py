import module
print('Welcome to MY CALCULATOR')
status=input('Do you want to Login..? \nYes or No: ')
while status=='Yes' or status=='Y' or status=='yes' or status=='y':
    option=(input('\n 1  . Addition\n\n 2  . Subtraction\n\n 3  . Product\n\n 4  . Division\n\n 5  . Square root\n\n 6  . Power\n\n 7  . Sin\n\n 8  . Cos\n\n 9  . Tan\n\n 10 . Floor Division\n\n 11 . Exit\n\nSelect the operation=> '))
    if option=='1' or option=='Addition' or option=='add' or option=='2' or option=='Difference' or option=='sub' or option=='3' or option=='Product' or option=='product' or option=='mul' or option=='4' or option=='Division' or option=='divison' or option=='10' or option=='Floor division':
        num1=int(input('Enter the first number= '))
        num2=int(input('Enter the second number= '))
    elif option=='6' or option=='Power' or option=='power':
        num1=int(input('Enter the number= '))
        num2=int(input('Enter the power= '))
    elif option=='5' or option=='Square root' or option=='square root' or option=='sqrt' or option=='7' or option=='Sin' or option=='sin' or option=='8' or option=='Cos' or option=='cos' or option=='9' or option=='Tan' or option=='tan': num1=int(input('Enter the number= '))
    if option=='1' or option=='Addition' or option=='add':module.sum(num1,num2)
    elif option=='2' or option=='Difference' or option=='sub':module.sub(num1,num2)
    elif option=='3' or option=='Product' or option=='product' or option=='mul': module.mul(num1,num2)
    elif option=='4' or option=='Division' or option=='divison': module.div(num1,num2)
    elif option=='5' or option=='Square root' or option=='square root' or option=='sqrt': module.sqrt(num1)
    elif option=='6' or option=='Power' or option=='power': module.power(num1,num2)
    elif option=='7' or option=='Sin' or option=='sin': module.sin(num1)
    elif option=='8' or option=='Cos' or option=='cos': module.cos(num1)
    elif option=='9' or option=='Tan' or option=='tan': module.tan(num1)
    elif option=='10' or option=='Floor division': module.flrdiv(num1,num2)
    elif option=='11':
        print('Thank you for using this calculator..!! \nHave a nice day..!!')
        exit()
    else: print('Invalid option..!')
if status=='No' or status=='N' or status=='no' or status=='n': exit()