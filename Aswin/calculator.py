from math import cos, sin, sqrt, tan
print("1.ADDITION\n2.SUBTRACTION\n3.DIVISION\n4.MULTIPLIACTION\n5.SQURE\n6.SQURE ROOT\n7.CUBE\n8.SIN\n9.COS\n10.TAN\n11.FLOOR DIVISION\n12.EXIT")
c=int(input("Select Your Choice"))
while c==1:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a+b)
if c==2:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a-b)
elif c==3:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a/b)
elif c==4:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a*b)
elif c==5:
    a=int(input('Enter the  number='))
    print(a*a)
elif c==6:
    a=int(input('Enter the number='))
    print(sqrt(a))
elif c==7:
    a=int(input('Enter the number='))
    print(a*a*a)
elif c==8:
    a=int(input('Enter the number='))
    print(sin(a))
elif c==9:
    a=int(input('Enter the number='))
    print(cos(a))
elif c==10:
    a=int(input('Enter the number='))
    print(tan(a))
elif c==11:
    a=int(input('Enter the first number='))
    b=int(input('Enter the second number='))
    print(a//b)
elif c==12:
    a=("exited")
    print(a)
else:
    print(c)

    
