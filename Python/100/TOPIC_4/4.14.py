# 4.14 Write a function that takes two lists and returns a list of items
#      that appear in BOTH lists.
#      Example: common([1,2,3], [2,3,4]) -> [2, 3]
import random

ls_1 = []
ls_2 = []

def random_string(lst):
    for i in range(1, 6):
        i = random.randint(1, 5) 
        lst.append(i)
    return lst

x = random_string(ls_1)
y = random_string(ls_2)

def same(a, b):
    ls = []
    for i in a:
        if i in b and i not in ls:
            ls.append(i)
    return ls


print("Lists:")
print(x)
print(y)
print("")
print("Numbers in both lists:")
print(same(ls_1, ls_2))

