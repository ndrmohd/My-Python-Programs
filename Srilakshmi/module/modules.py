from cmath import cos, sin, sqrt, tan
def multtab(a):
    for i in range(1,11):
        print(i,"*",a,"=",a*i)
def pt1(a,b):
    for i in range(a):
        print(i*b)
def lorc():
    para= "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrstandard dummy text ever since the 1500s when an unknown printer took a galley of type scrambled it to make a type specimen book It has survived  only five centuries but also the leap into electronic typesetting, remaining essentially unchanged It was popularised the 1960s  the release of Letraset sheets containing Lorem Ipsum passages more recently desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
    print(para.count("Lorem Ipsum"))
def pattern2():
    a=[6,2,5,3,8]
    for i in a :
        print(i*"*")
def fib(num):
    if num>1:
        a=0
        print(a)
        b=1
        print(b)
        for i in range(num-2):
            c=a+b
            a=b
            b=c
            print(c)
    else:
        print("invalid")
def sum(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mult(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2)
def floordiv(num1,num2):
    print(num1//num2)
def sinn(num1):
    print(sin(num1))
def cosn(num1):
    print(cos(num1))
def tann(num1):
    print(tan(num1))
def power(num1,num2):
    print(num1**num2)
def squarert(num1):
    print(sqrt(num1))
def listrev(a):
    print(a.reverse)
def primerange(start,end):
    for i in range(start,end):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
def largestli(l2):
    print(max(l2))
def printiingext(file):
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
def pattern3():
    for i in range(a):
        print(i*"*")
    for j in range(a,0,-1):
        print(j*"*")