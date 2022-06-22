from math import cos, sin, sqrt, tan
print("1.ADDITION\n2.SUBTRACTION\n3.DIVISION\n4.MULTIPLIACTION\n5.SQURE\n6.SQURE ROOT\n7.CUBE\n8.SIN\n9.COS\n10.TAN\n11.FLOOR DIVISION\n12.EXIT")
a=int(input("Select Your Choice"))
if a==1:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a+b)
elif a==2:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a-b)
elif a==3:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a/b)
elif a==4:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a*b)
elif a==5:
    a=int(input('Enter the  number='))
    print(a*a)
elif a==6:
    a=int(input('Enter the number='))
    print(sqrt(a))
elif a==7:
    a=int(input('Enter the number='))
    print(a*a*a)
elif a==8:
    a=int(input('Enter the number='))
    print(sin(a))
elif a==9:
    a=int(input('Enter the number='))
    print(cos(a))
elif a==10:
    a=int(input('Enter the number='))
    print(tan(a))
elif a==11:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a//b)