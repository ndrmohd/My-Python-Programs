even=0
for i in range(100,201):
    a=i//10
    b=i//100
    c=i//1
    d=a+b+c
    if d%2==0:
        print(i)
    else:
        continue
    
    