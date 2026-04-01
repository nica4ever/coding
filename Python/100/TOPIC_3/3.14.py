# 3.14 Create a dict of 5 servers and statuses.
#      Count how many are "online". Print the count.
import random
servers = {}
value = ["online", "offline"]

def pick_random_val(val):
        rndm = random.choice(val)
        return rndm

def make_servers(dic):
    for i in range(1, 21):
        dic[f'server-{i}'] = pick_random_val(value)
    return dic

print("")
print("All servers:")
[print(f'{key}: {value}') for key, value in make_servers(servers).items()]

print("")
print("Offline:")
for key,value in make_servers(servers).items():
    if value == "offline":
        print(key, value)
