a=int(input("Enter the limit:"))
for i in range(2,a):
    if a>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)