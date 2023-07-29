l=[1,2,3,4]
print(isinstance(l,list))
data={'jay':['male',23,2000],'raj':[25],'vicky':['male',22],'ram':['male',23]}
count=0

for key in data:

    if isinstance(data[key],list):
        count=count+1
        print(f"key is:",key +" and value is ",data[key])

print(count)

