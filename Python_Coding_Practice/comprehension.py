#expression for variable in iterable if condition :--

nums=[2,3,4,5,6]
sq=[]
print([num*num for num in nums])
print([num*num for num in nums if num%2==0])
print([num*num for num in nums if num%2==0 if num%3==0])

for num in nums:
    sq.append(num*num)

print("square of numbers is :",sq)

print([num*num if num%2==0 else num*num*num for num in nums ])