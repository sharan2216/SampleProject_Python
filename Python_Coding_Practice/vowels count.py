name=input("enter a name : ")
l=['a','e','i','o','u']
count=0
for i in name:
    if i in l:
        count=count+1

print("no of vowels in a name is :",count)