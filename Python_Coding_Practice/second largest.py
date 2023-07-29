

my_list=[['jay', 80], ['viru', 85], ['basanti', 95], ['thakur', 83], ['sambha', 85]]
mydict = dict(my_list)
marks = set(mydict.values())
sorted_marks = sorted(marks)
second_largest = sorted_marks[-2]
print(second_largest)
for ele in my_list:
    if ele[1] == second_largest:
        print(ele[0])
