file=input("enter the file name")
a=file.split(".")
c=a[1]
if c=="py":
    print("it is a python file")
elif c=="java":
    print("it is a java file")
elif c=="asp":
    print("it is a active server page")
elif c=="jsp":
    print("it is a java server page")
elif c=="php":
    print("it is a php file")