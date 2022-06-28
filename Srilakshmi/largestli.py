l=[2,4,11,12,1,9]
nl=[]
while l:
    max=l[0]
    for i in l:
        if i>max:
            max=i
    nl.append(max)
    l.remove(max)
print(nl)
maximum=print(nl[0])

l2=[2,4,11,12,1,9]
print(max(l2))