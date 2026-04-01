# 3.15 Create a dict {"a": 1, "b": 2, "c": 3}.
#      Print all the keys as a list.
#      Print all the values as a list.
dic = {"a": 1, "b": 2, "c": 3}

key_list = []
value_list = []

for key, value in dic.items():
    key_list.append(key)
    value_list.append(value)
print(key_list)
print(value_list)
