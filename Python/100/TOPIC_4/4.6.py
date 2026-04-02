# 4.6  Write a function that takes a list and RETURNS the list reversed.
#      Do NOT use .reverse() or [::-1]. Build a new list with a loop.
import random

n = 0 

ls = []

for i in range(1, 15):
    n = random.randint(1, 1000)
    ls.append(n)
print(ls)

def rev(x):
    lsr = []
    for i in range(len(x)-1, -1, -1):
        lsr.append(x[i])
    return lsr
print(rev(ls))
