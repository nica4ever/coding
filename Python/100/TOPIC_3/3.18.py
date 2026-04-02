# 3.18 Create a dict where keys are letters and values are how many times
#      that letter appears in the string "banana".
#      Do it manually with a loop, not Counter.
string = "banana"
dic = {}
for i in string:
    if dic.get(i) == None:
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1
print(dic)
