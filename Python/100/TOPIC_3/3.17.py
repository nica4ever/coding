# 3.17 Create a dict of 5 servers and their CPU usage (integers, percentage).
#      Find the server with the highest CPU usage. Print its name and value.
#      Do NOT use max() — use a loop.
import random

dic = {}
percentage = None

for i in range(1,11):
    percentage = random.randint(1, 100)
    dic[f'server-{i}'] = percentage

for key,value in dic.items():
    print(f'{key}:{value}%')
print("")

print("Servers with highest value")
sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for i in sort[0:3]:
    print("")
    print(f'{i[0]}: {i[1]}%')
