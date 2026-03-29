# 2.17 Create a list of 8 random numbers (hardcoded is fine).
#      Find and print the maximum WITHOUT using max(). Use a loop.
import random
ls = random.sample(range(1, 1000), 8)
sort = sorted(ls)
print(sort)
print(f'Highest number: {sort[-1]}')
