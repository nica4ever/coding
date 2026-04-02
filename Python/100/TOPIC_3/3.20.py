# 3.20 Create a dict of 5 people and their ages.
#      Print them sorted by age (youngest first).
#      Hint: sorted() with key=lambda
dic = {"Alex": 25, "Andrew": 16, "Andra": 27, "Sara": 18, "Rob": 5}
dic_sorted = sorted(dic.items(), key=lambda x: x[1], reverse=False)
print(dic_sorted)


