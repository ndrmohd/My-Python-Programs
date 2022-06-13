a=int(input('Length of the 1st side of triangle '))
b=int(input('Length of the 2nd side of triangle '))
c=int(input('Length of the 3rd side of triangle '))
if a==b==c:
    print('The given triangle is equilateral.')
elif a==b or a==c or b==c:
    print('The given triangle is isosceles.')
else:
    print('The given triangle is scalene.')