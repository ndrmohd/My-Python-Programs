from math import tan
shape=input('enter the shape')
if shape=="circle":
    r=int(input("enter radius"))
    area=3.14*r*r
    print(area)
elif shape!="circle":
    n=int(input("enter the number of sides"))
    l=int(input("lenth of one side"))
    apothem=l/(2*(tan(180/n)))
    area2=n*l*apothem
    print(area2)