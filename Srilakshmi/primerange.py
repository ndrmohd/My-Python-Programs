r1=int(input("enter the start range"))
r2=int(input("enter the end range"))
for i in range(r1,r2):
    for j in range(i+1,r2):
        if j%i!=0:
            print(i)
            break
        else:
           print("not a prime")