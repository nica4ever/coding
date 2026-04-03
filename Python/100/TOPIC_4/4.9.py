# 4.9  Write a function that takes a list of numbers and RETURNS two values:
#      the minimum and maximum. Use tuple unpacking when calling it:
#      lo, hi = min_max([3, 1, 4, 1, 5])
import random
ls = []
def random_ls(y):
    for i in range(1, 20):
        x = random.randint(1, 1000) 
        y.append(x)
    return y

def min_max(y):
    lo = min(y)
    hi = max(y)
    return lo, hi

lst = random_ls(ls)
print(lst)
print("Min_max:")
lo, hi = min_max(lst)
print(lo, hi)
