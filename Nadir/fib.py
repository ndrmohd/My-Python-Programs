n=int(input('Enter the 1st n terms '))
a=0
b=1
if n>1:
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)
else:
    print(0)