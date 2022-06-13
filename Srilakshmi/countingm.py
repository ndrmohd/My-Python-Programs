month=input("enter the month")
year=int(input('enter the year'))
if month=="January" or month=="March" or month=="May"or month=="July" or month=="August" or month=="October" or month=="December":
    print("31 days")
elif month=="November" or month=="April" or month=="June" or month=="September":
    print("30 days")
elif year%4==0 and month=="February":
    print("29 days")
elif year%4!=0 and month=="February":
    print("28 days")