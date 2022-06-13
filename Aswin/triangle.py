a=int(input("length of first side is"))
b=int(input("length of second side is"))
c=int(input("length of third side is"))
if a==b==c:
    print("the triangle is equilateral")
elif a==b or a==c or b==c:
    print("the triangle is isoceless")
else:
    print("the traingle is an scalane")
