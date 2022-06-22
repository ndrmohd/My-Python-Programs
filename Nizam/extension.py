from posixpath import splitext
a=input("enter the file name")
b=(a.split("."))
if b[1]=='py':
    print(a,"is a python file ")
elif b[1]=='asp':
    print(a,"is a Active Server Page  ")
elif b[1]=='jsp':
    print(a,"is a JavaServer Page ")
elif b[1]=='jar':
    print(a,"is a Java ARchive file ")
elif b[1]=='txt':
     print(a,"is a text file ")
else:
     print(a,'is a',b[1],'extension file')