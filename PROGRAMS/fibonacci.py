def meth():
    a=0
    b=1
    while True:
        yield a
        a,b=b,a+b

f=meth()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

print("*"*50)


l1=[3,2,1,5,4,7,6,8]
n=len(l1)
for i in range(0,n):
    for j in range(i+1,n):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]

print(l1)