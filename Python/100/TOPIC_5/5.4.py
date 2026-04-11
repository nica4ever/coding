# 5.4  Split "key1=val1,key2=val2,key3=val3" into a dict.
#      Hint: split on "," first, then split each piece on "=".
string = "key1=val1,key2=val2,key3=val3"
split = string.split(",")

ls = []

for i in split:
    ls.append(i.split("=")) 

dic = {}

for i in ls:
    index = len(i)
    dic[i[0]] = i[index - 1]

print(dic)
