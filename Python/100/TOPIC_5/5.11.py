# 5.11 Given 5 lines of "key: value" format (multiline string or list of strings),
#      parse them into a single dict. Print.
import random

ls = []

for i in range(1, 6):
    ls.append(f'key-{i}: value-{i}')

dic = {}
for line in ls:
    dic[line.split(":")[0]] = line.split(":")[1]
print(dic)
