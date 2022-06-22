from math import cos, sin, sqrt, tan
print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square root\n6.Square\n7.Cube\n8.Sin\n9.Cos\n10.Tan\n11.Floor Division\n12.Exit')
p=int(input('Select the operation=> '))
while p==1:
    a=int(input('Enter the first number= '))
    b=int(input('Enter the second number= '))
    print(a+b)
while p==2:
    a=int(input('Enter the first number= '))
    b=int(input('Enter the second number= '))
    print(a-b)
while p==3:
    a=int(input('Enter the first number= '))
    b=int(input('Enter the second number= '))
    print(a*b)
while p==4:
    a=int(input('Enter the first number= '))
    b=int(input('Enter the second number= '))
    print(a/b)
while p==5:
    a=int(input('Enter the number= '))
    print(sqrt(a))
while p==6:
    a=int(input('Enter the number= '))
    print(a*a)
while p==7:
    a=int(input('Enter the number= '))
    print(a*a*a)
while p==8:
    a=int(input('Enter the number= '))
    print(sin(a))
while p==9:
    a=int(input('Enter the number= '))
    print(cos(a))
while p==10:
    a=int(input('Enter the number= '))
    print(tan(a))
while p==11:
    a=int(input('Enter the first number= '))
    b=int(input('Enter the second number= '))
    print(a//b)
while p==12:
    print('Exit')
    break