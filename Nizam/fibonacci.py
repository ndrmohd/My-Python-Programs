limit=int(input("Enter the limit"))
if limit>1:
    a=0
    print(a)
    b=1
    print(b)
    for i in range(limit-2):
        c=a+b
        a=b
        b=c
        print(c)
else:
    print(0)