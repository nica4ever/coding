# 2.16 Create a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
#      Use a loop to build a NEW list containing only numbers greater than 5.
#      Print the new list.
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls2 = []
for items in ls:
    if items > 5:
        ls2.append(items)
print(ls2)
