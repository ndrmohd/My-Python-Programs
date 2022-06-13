a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))
if a==b and b==c:
    print("The triangle is equilateralal")
elif a==b or b==c:
    print("The triangle is issoceles")