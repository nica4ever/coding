# 2.14 Create a list [10, 20, 30, 40, 50].
#      Use a for loop to calculate the sum. Print it.
#      Do NOT use the sum() function — do it manually with a variable.
ls = [10, 20, 30, 40, 50]
i = 0
for items in ls:
    i = items + items + items
print(i)
