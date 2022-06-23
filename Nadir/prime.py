a=int(input("Enter the limit:"))
for i in range(2,a):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)