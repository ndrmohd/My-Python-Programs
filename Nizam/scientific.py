from math import cos, sin, sqrt, tan
print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.squareroot\n6.Square\n7.Sine\n8.Cos\n9.Cube\n10.Tan\n11.Floor Division\n12.Exit')
c=int(input("Enter your option:"))
while c==1:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print('Sum=',a+b)
    break
while c==2:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print('Difference=',a-b)
    break
while c==3:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print('product=',a*b)
    break
while c==4:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print('Quotient=',a/b)
    break
while c==5:
    a=int(input("Enter the number:"))
    print('Square Root=',sqrt(a))
    break
while c==6:
    a=int(input("Enter the number:"))
    print('Square=',a*a)
    break
while c==7:
    a=int(input("Enter the number:"))
    print('Sin=',sin(a))
    break
while c==8:
    a=int(input("Enter the number:"))
    print('Cos=',cos(a))
    break
while c==9:
    a=int(input("Enter the number:"))
    print('Cube=',a*a*a)
    break
while c==10:
    a=int(input("Enter the number:"))
    print('Tan=',tan(a))
    break
while c==11:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print('Floor Division=',a//b)
    break
while c==12:
    print('Exited')
    break