a=int(input("enter the range"))
for i in range(2,a):
    if a%i==0:
        print(i)
    elif i%i==0 and i%1==0:
        print(i)
    elif i%2!=0 and i%3!=0:
        print(i)