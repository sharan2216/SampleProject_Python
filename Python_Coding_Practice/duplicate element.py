l=["hello",1,2,1,3,4,4,5,5,6,6]
d=[]
for i in range(0,len(l)):
    for j in range((i+1),len(l)):
        if l[i]==l[j] and l[i] not in d:
            print(l[i],end=' ')

print("----------------")
for i in l:
    if l.count(i)>1 and i not in d:
        d.append(i)
print(d)
