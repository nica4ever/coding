# 4.5  Write a function that takes a number and RETURNS "even" or "odd". Test with 3 numbers.
import random

x = random.randint(1, 1000)

print(f'Number is: {x}')
print("")

def even_odd(n):
    if n % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"

print(even_odd(x))

