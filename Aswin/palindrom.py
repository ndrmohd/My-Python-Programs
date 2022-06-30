string=input('Enter a string: ')
b=string[::-1]
print('Reverse of the string is:',b)
if string==b:
    print('It is a palindrom')
else:
    print('It is not a palindrom')