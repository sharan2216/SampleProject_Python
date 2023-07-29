mylist=[1,2,2,3,3,4,5,5,6,6]
newlist=[]
for num in mylist:
    if mylist.count(num)==1:
        newlist.append(num)

print(newlist)