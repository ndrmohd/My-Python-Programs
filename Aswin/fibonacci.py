x=int(input("enter the limit"))
if x>1:
 a=0
 print(a)
 b=1
 print(b)
 for i in range(x-2):
    c=a+b
    a=b
    b=c
    print(c)
else:
    print(0)