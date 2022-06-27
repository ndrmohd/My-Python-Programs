firstlist=[8,4,2,1,9]
newlist=[]
while firstlist:
    max=firstlist[0]
    for i in firstlist:
        if i>max:
            max=i
    newlist.append(max)
    firstlist.remove(max)
print(newlist)