# 4.10 Write a function that takes a dict and a value.
#      It RETURNS a list of all keys that have that value.
#      Example: find_keys({"a": 1, "b": 2, "c": 1}, 1) -> ["a", "c"]

import random
import string

rdic = {}

def random_dic(dic):
    for letter in string.ascii_lowercase[:4]:
        x = random.randint(1, 2) 
        dic[letter] = x
    return dic
x = random_dic(rdic)
print(x)
def count(dic, y):
    ls = []
    for key, value in dic.items():
        if value == y:
            ls.append(key)
    return ls
print(f'1 -> {count(x, 1)}')
