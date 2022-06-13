a=int(input('Enter the year'))
b=input('Enter the month')
if  b=='february':
    if a%4==0:
        print('29')
    else:
        print('28')
elif b=='january' or b=='march' or b=='may' or b=='july' or b=='august' or b=='october' or b=='december':
    print('31')
else:
    print('30') 