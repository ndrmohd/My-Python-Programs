from math import cos, sin, sqrt, tan
from re import X
print("1.ADDITION\n2.SUBTRACTION\n3.DIVISION\n4.MULTIPLIACTION\n5.SQURE\n6.SQURE ROOT\n7.CUBE\n8.SIN\n9.COS\n10.TAN\n11.FLOOR DIVISION\n12.EXIT")
x=int(input("Select Your Choice"))
while X==1:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a+b)
if x==2:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a-b)
elif x==3:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a/b)
elif x==4:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a*b)
elif x==5:
    a=int(input('Enter the  number='))
    print(a*a)
elif x==6:
    a=int(input('Enter the number='))
    print(sqrt(a))
elif x==7:
    a=int(input('Enter the number='))
    print(a*a*a)
elif x==8:
    a=int(input('Enter the number='))
    print(sin(a))
elif x==9:
    a=int(input('Enter the number='))
    print(cos(a))
elif x==10:
    a=int(input('Enter the number='))
    print(tan(a))
elif x==11:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a//b)
elif x==12:
    a=("exited")
    print(a)
else:
    print(x)

    
