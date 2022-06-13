a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))
if a==b==c :
    print('equilateral triangle')
elif a==b or b==c or a==c:
    print('isosceless triangle') 
else:
    print('scalen triangle')   