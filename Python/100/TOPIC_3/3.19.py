# 3.19 Given the string "hello world hello python hello world"
#      Create a dict that counts how many times each word appears.
#      Hint: split the string first, then loop.
string = "hello world hello python hello world"
dic = {}
for i in string.split():
    if dic.get(i) == None:
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1
print(dic)
