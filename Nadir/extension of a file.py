from posixpath import splitext
a=input("Enter the filename ")
b=splitext(a)
if b[1]=='.py':
    print(a,'is a Python extension file.')
elif b[1]=='.java':
    print(a,'is a JAVA extension file.')
elif b[1]=='.php':
    print(a,'is a PHP extension file.')
elif b[1]=='.txt':
    print(a,'is a Text extension file.')
elif b[1]=='.jar':
    print(a,'is a JAVA ARchive extension file.')
elif b[1]=='.asp':
    print(a,'is a Active Server Pages extension file.')
elif b[1]=='.jsp':
    print(a,'is a JAVA Server Pages extension file.')
else:
    print(a,'is a',b[1],'extension file')