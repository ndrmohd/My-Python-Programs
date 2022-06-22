from math import cos, sin, sqrt, tan
print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.squareroot\n6.Square\n7.Sine\n8.Cos\n9.Cube\n10.Tan\n11.Floor Division')
c=int(input("Enter your option:"))
while c>=1:
    if c==1:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print('Sum=',a+b)
    elif c==2:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print('Difference=',a-b)
    elif c==3:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print('product=',a*b)
    elif c==4:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print('Quotient=',a/b)
    elif c==5:
        a=int(input("Enter the number:"))
        print('Square Root=',sqrt(a))
    elif c==6:
        a=int(input("Enter the number:"))
        print('Square=',a*a)
    elif c==7:
        a=int(input("Enter the number:"))
        print('Sin=',sin(a))
    elif c==8:
        a=int(input("Enter the number:"))
        print('Cos=',cos(a))
    elif c==9:
        a=int(input("Enter the number:"))
        print('Cube=',a*a*a)
    elif c==10:
        a=int(input("Enter the number:"))
        print('Tan=',tan(a))
    elif c==11:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print('Floor Division=',a//b)
    else: 
        print('Exited')
    break