class A:
    def met():
        str1 = input("enter a first string :")
        str2 = input("eneter second string : ")
        str1 = set(str1)
        str2 = set(str2)
        print(str1 & str2)

obj=A
obj.met()