# 5.15 Given "The quick brown fox jumps over the lazy dog"
#      Split into words, make a dict where key = word, value = word length.
string = "The quick brown fox jumps over the lazy dog"

dic = {}
for item in string.split():
    dic[item] = len(item)
print(dic)
