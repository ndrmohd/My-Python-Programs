string=input("Enter string: ")
count=0
s=0
for i in string:
 if i=='a' or i=='A':
    count=count+1
 if i=='b' or i=='B':    
    count=count-1   
 if count==0:
    s=s+1
          
print(s)