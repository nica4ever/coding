# 4.4  Write a function that takes a list of numbers and RETURNS the largest one.
#      Do NOT use max() — use a loop inside the function.
import random
a = 0
ls = []

for i in range(1, 15):
    a = random.randint(1, 1000)
    ls.append(a)
print(ls)
print("")

def largest_n(x):
    y = 0
    for i in x:
        if i > y:
            y = i
    return y

print(f'Largest number from list is {largest_n(ls)}')

