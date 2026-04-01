# 3.13 Create an empty dict. Use a for loop with range(5) to add keys
#      "server-0", "server-1", ... "server-4" with value "online" for each.
#      Print the dict.
dic = {}
for i in range(1, 6):
    dic[f'server-{i}'] = "online"
print(dic)
