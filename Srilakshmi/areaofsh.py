from math import tan
shape=input('enter the shape')
if shape=="circle":
    r=int(input("enter radius"))
    area=3.14*r*r
    print(area)
elif shape=="triangle":
    b=int(input("enter the breadth"))
    h=int(input("enter the height"))
    areaT=.5*b*h
elif shape=="sqaure":
    l=int(input("enter the length"))
    areaS=l*l
    print(areaS)
elif shape=="rectangle":
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))
    areaR=l*b
    print(areaR)
