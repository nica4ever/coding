# 4.16 Write a function that takes a list of numbers and returns a new list
#      with duplicates removed. Order doesn't matter.
import random

ls = []

def gen_lst(x):
    for i in range(1, 5):
        i = random.randint(1, 5)
        x.append(i)
    return x

lst = gen_lst(ls)
print(lst)

def remove_duplicates(x):
    ls = []
    for i in x:
        if i in ls:
            pass
        else:
            ls.append(i)
    return ls

print(remove_duplicates(lst))
