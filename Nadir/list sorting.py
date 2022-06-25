l=[8,4,2,1,9]
nl=[]
while l:
    max=l[0]
    for i in l:
        if i>max:
            max=i
    nl.append(max)
    l.remove(max)
print(nl)