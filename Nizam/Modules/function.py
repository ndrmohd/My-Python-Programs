import functiondefinition
print('Welcome to My Calcultaor')
status=input('Do you want to Continue in our calculator:\nY or N:')
while status=='Y' or status=='y':
    option=input(('1.  Addition\n2.  Subtraction\n3.  Multiplication\n4.  Division\n5.  Power\n6.  Squareroot\n7.  Sin\n8.  Cos\n9.  Tan\n10. Floor Division\n11. Exit\nEnter your Option:'))
    if option=='1' or option=='Addition' or option=='add' or option=='2' or option=='Subtraction' or option=='sub' or option=='3' or option=='Multiplication' or option=='mul' or option=='4' or option=='Division' or option=='div' or option=='5' or option=='Power' or option=='power' or option=='10' or option=='Floordivision' or option=='flrdiv': 
        num1=int(input("Enter the first number:"))
        num2=int(input("Enter the second number:"))
    elif  option=='6' or option=='Squareroot' or option=='sqrt' or option=='7' or option=='Sin' or option=='sin' or option=='8' or option=='Cos' or option=='cos' or option=='9' or option=='Tan' or option=='tan': num1=int(input("Enter the number:"))
    if  option=='1' or option=='Addition' or option=='add':functiondefinition.sum(num1,num2)
    elif option=='2' or option=='Subtraction' or option=='sub':functiondefinition.sub(num1,num2)
    elif option=='3' or option=='Multiplication' or option=='mul':functiondefinition.product(num1,num2)
    elif option=='4' or option=='Division' or option=='div':functiondefinition.div(num1,num2)
    elif option=='5' or option=='Power' or option=='power':functiondefinition.pow(num1,num2)
    elif option=='6' or option=='Squareroot' or option=='sqrt':functiondefinition.sqrt(num1)
    elif option=='7' or option=='Sin' or option=='sin':functiondefinition.sin(num1)
    elif option=='8' or option=='Cos' or option=='cos':functiondefinition.cos(num1)
    elif option=='9' or option=='Tan' or option=='tan':functiondefinition.tan(num1)
    elif option=='10' or option=='Floordivision' or option=='flrdiv':functiondefinition.flrdiv(num1,num2)
    elif option=='11' or option=='Exit' or option=='exit':
        print('Thank you For Using our Calculator\nHave A Nice day!!')
        exit()
    else:print('Invalid Option')
if status=='N' or status=='n':exit()