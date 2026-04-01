# 3.16 Create two dicts. Merge them into one.
#      Hint: dict1.update(dict2) or {**dict1, **dict2}
dic_1 = {"name": "dic1"}
dic_2 = {"name_1": "dic2"}
dic_1.update(dic_2)
print(dic_1)
