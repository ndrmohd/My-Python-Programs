a=int(input("enter shape"))
if a==rectangle:
    l=int(input("enter the length"))
    b=int(input("enter the breath"))
    area=l*b
    print(area)
elif a==triangle:
     b=int(input("enter the breath"))
     h=int(input("enter the height"))
     i=0.5
     area=i*b*h
     print(area)
elif a==circle:
    r=int(input("enter the radius"))
    pi=3.14
    area=pi*r*r
    print(area)     
else:
    print("this shape not avilable")


