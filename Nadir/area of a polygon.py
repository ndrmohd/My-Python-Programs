from math import sqrt
a=int(input("Enter the number of sides of the polygon= "))
if a==0:
    r=int(input('Enter the radius of the circle= '))
    area=3.14*r*r
    print(area)
elif a==3:
    c=int(input('Enter the length of one side of triangle= '))
    s=(3*c)/2
    area=sqrt(s*((s-c)*(s-c)*(s-c)))
    print(area)
elif a==4:
    l=int(input('Enter the length of the quadrilateral= '))
    b=int(input('Enter the breadth of the quadrilateral= '))
    area=l*b
    print(area)
else:
    print("There is no polygon with sides",a)