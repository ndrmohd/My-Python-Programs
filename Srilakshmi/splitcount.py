s=input("enter string") #aaab(ba)bb(ba)(aabb)(ab)
count=0                 #3  2 1 2 0 -1 0 1 1 0 
ab=0
for i in s:
    if i=="a":
        count+=1      
    if i=='b':
        count-=1
    if count==0:
        ab+=1
print(ab) 