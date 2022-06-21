from posixpath import splitext
a=input("enter the file name")
b=(a.split("."))
if b[1]=='py':
    print(a,"its a python extension file ")
elif b[1]=='asp':
    print(a,"its a Active Server Pages extension file ")
elif b[1]=='jsp':
    print(a,"its a JavaServer Pages extension file ")
elif b[1]=='jar':
    print(a,"its a Java ARchive extension file ")
elif b[1]=='txt':
     print(a,"its a text extension file ")
else:
     print(a,'its a',b[1],'extension file')