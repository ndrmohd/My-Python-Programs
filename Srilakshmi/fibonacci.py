num=int(input("enter the number"))
if num>1:
    a=0
    print(a)
    b=1
    print(b)
    for i in range(num-2):
        c=a+b
        a=b
        b=c
        print(c)
else:
    print("invalid")