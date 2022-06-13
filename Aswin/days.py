a=input("enter the month")
b=int(input("enter the year"))
if a=='february':
   if b%4==0:
    print("the month have 29 days")
   else:
        print("the month have 28 days")
elif a=='april' or a=='june' or a=='september' or a=='november':
    print("month have 30 days")
else:
    print("month have 31 days")
