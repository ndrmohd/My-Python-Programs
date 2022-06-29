import modules
print("WELCOME TO THE CALCULATOR")
status=input('DO YOU WANT TO LOGIN ? \n YES OR NO : ')
while status=="YES" or status=="yes":
    option=input("Select Your Choice\n1 . ADDITION\n2 . SUBTRACTION\n3 . DIVISION\n4 . MULTIPLIACTION\n5 . SQURE\n6 . POWER\n7 . FLOOR DIVISION\n8 . COS\n9 . TAN\n10. FLOOR DIVISION\n11. EXIT\n")   
    if option=='1' or option=='ADDITION' or option=='addition'or option=='2' or option=='SUBTRACTION' or option=='subtraction'or option=='3' or option=='DIVISION' or option=='division'or option=='4' or option=='MULTIPLIACTION' or option=='multiplication'or option=='6' or option=='POWER' or option=='power' or option=='7' or option=='FLOOR DIVISION' or option=='floor division':
        a=int(input('Enter the first number= '))
        b=int(input('Enter the second number= '))
    elif option=='5' or option=='SQURE ROOT' or option=='squre root'or option=='8' or option=='COS' or option=='cos' or option=='9' or option=='TAN' or option=='tan'or option=='10' or option=='sin' or option=='sin':
        a=int(input('Enter the number= '))
    if option=='1' or option=='ADDITION' or option=='addition':modules.sum(a,b)
    elif option=='2' or option=='SUBTRACTION' or option=='subtraction':modules.sub(a,b)
    elif option=='3' or option=='DIVISION' or option=='division':modules.div(a,b)
    elif option=='4' or option=='MULTIPLIACTION' or option=='multiplication':modules.mul(a,b)
    elif option=='5' or option=='SQURE ROOT' or option=='squre root':modules.sqr(a,b)
    elif option=='6' or option=='POWER' or option=='power':modules.pwr(a,b)
    elif option=='7' or option=='FLOOR DIVISION' or option=='floor division':modules.flrdiv(a,b)
    elif option=='8' or option=='COS' or option=='cos':modules.cos(a)
    elif option=='9' or option=='TAN' or option=='tan':modules.tan(a)
    elif option=='10' or option=='sin' or option=='sin':modules.sin(a)
    elif option=='11' or option=='EXIT' or option=='exit':
            a=("Thank You For Using This Calculator ")
            print("Thank You For Using This Calculator ")
            exit()

