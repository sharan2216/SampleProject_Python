dict2={}
dict1={2:"apple",4:"banana",3:"mango",1:"grapes"}
dict1=sorted(dict1.keys())
print(dict1.keys())
for i in dict1:
    dict2[i]=dict1[i]

print(dict2)