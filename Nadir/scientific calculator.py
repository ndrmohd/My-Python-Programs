from math import cos, sin, sqrt, tan
print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square root\n6.Square\n7.Cube\n8.Sin\n9.Cos\n10.Tan\n11.Floor Division\n12.Exit')
p=int(input('Select the operation=> '))
while p>0:
    for i in range(1,13):
        
        if p==1 or p=='Addition':
            a=int(input('Enter the first number= '))
            b=int(input('Enter the second number= '))
            print(a+b)
        if p==2 or p=='Subtraction':
            a=int(input('Enter the first number= '))
            b=int(input('Enter the second number= '))
            print(a-b)
        elif p==3 or p=='Multiplication':
            a=int(input('Enter the first number= '))
            b=int(input('Enter the second number= '))
            print(a*b)
        elif p==4 or p=='Division':
            a=int(input('Enter the first number= '))
            b=int(input('Enter the second number= '))
            print(a/b)
        elif p==5:
            a=int(input('Enter the number= '))
            print(sqrt(a))
        elif p==6:
            a=int(input('Enter the number= '))
            print(a*a)
        elif p==7:
            a=int(input('Enter the number= '))
            print(a*a*a)
        elif p==8:
            a=int(input('Enter the number= '))
            print(sin(a))
        elif p==9:
            a=int(input('Enter the number= '))
            print(cos(a))
        elif p==10:
            a=int(input('Enter the number= '))
            print(tan(a))
        elif p==11:
            a=int(input('Enter the first number= '))
            b=int(input('Enter the second number= '))
            print(a//b)
        elif p==12:
            print('Exit')