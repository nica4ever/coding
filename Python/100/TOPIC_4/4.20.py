# 4.20 Write a function that takes a list of strings and an integer n.
#      Returns a dict where keys are the strings and values are True if
#      the string length > n, False otherwise.
#      Example: check_lengths(["hi", "hello", "yo"], 3) -> {"hi": False, "hello": True, "yo": False}
import random
import string

def random_string():
    lst = []
    for i in range(1, 11):
        i = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        lst.append(i)
    return lst

string = random_string()
print(string)

n = int(input("Select lenght: "))

def function(x, n):
    dic = {}
    for i in x:
        lenght = len(i)
        dic[i] = True if lenght > n else False
    return dic
print(function(string, n))

