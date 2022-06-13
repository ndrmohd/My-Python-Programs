a=input('Enter the month ')
b=int(input('Enter the year '))
if a=='January' or a=='March' or a=='May' or a=='July' or a=='August' or a=='October' or a=='December':
    print(a,'has 31 days.')
elif a=='April' or a=='June' or a=='September' or a=='November':
    print(a,'has 30 days.')
elif a=='February' and b%4==0:
    print(a,'has 29 days.')
elif a=='February' and b%4!=0:
    print(a,'has 28 days.')