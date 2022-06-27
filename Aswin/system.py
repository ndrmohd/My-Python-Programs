import datetime,platform,os

print("                         SYSTEM INFORMATIONS")
print("                      ________________________          ")
option=input(" \n [1] CURRENT DATE AND TIME          |          [5] VERSION \n [2] ARCHITECURE                    |          [6] PROCESSOR \n [3] PLATFORM                       |          [7] USER  \n [4] OPERATING SYSTEM               |          [8] MACHINE \n\n                                [9] EXIT\n")
if option=='1':
    print(datetime.datetime.now())
elif option=='2':
    print(platform.architecture())
elif option=='3':   
    print(platform.platform())
elif option=='4':
    print(platform.system())
elif option=='5':
    print(platform.version())
elif option=='6':
    print(platform.processor())
elif option=='7':
    print(os.getlogin())
elif option=='8':
    print(platform.machine())
elif option=='9':
    exit()
