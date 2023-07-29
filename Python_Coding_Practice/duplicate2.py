# arr1=[1,2,1,3,4,4,5,5,6,6]
# arr2=[]
# count=0
# l=len(arr1)
# for i in range(0,l):
#     for j in range((i+1),l):
#         if arr1[i]==arr1[j] and arr1[i] not in arr2:
#             print(i, end=' ')
#             # arr2.append(i)
#             # count=count+1
#
# # print(count)
# # remove duplicates-------------------
# arr=[1,2,3,4,4,5,5,6,7]
# arr2=[]
# for i in arr:
#     if i not in arr2:
#         arr2.append(i)
#
# print(arr2)
# -----------------------------

arr=[1,2,3,4,4,5,5,6,7]
arr3=[]
for i in range(0,len(arr)):
    for j in range((i+1),len(arr)):
        if arr[i]==arr[j] and i not in arr3:
            arr3.append(i)


print(arr3)

