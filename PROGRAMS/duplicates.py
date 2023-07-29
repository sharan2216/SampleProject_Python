list1=['my','name','is','kant']
str1=''.join(list1)
print(str1)
dup=[]
for char in str1:
    if str1.count(char)>1 and char not in dup:
        dup.append(char)

print(dup)

print("------------------------")
# NO DUPLICATES--UNIQUE CHARACTER IN A STRING
str2="INDIA"
unique=[]
for char in str2:
    if str2.count(char)==1 and char not in unique:
        unique.append(char)

print(unique)
