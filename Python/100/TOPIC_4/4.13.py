# 4.13 Write a function that takes a list of strings and returns a new list
#      containing only strings that are longer than 5 characters.
import random
import string

ls = []

def random_string(lst):
    for i in range(1, 11):
        i = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        lst.append(i)
    return lst

def function(x):
    lst = []
    for i in x:
        if len(i) > 5:
            lst.append(i)
    return lst

rls = random_string(ls)
print(rls)
print("Longer than five")
print(function(rls))
