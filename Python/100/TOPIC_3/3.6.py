# 3.5  Create a dict with 4 servers and statuses. Loop through it and print all keys.
# 3.6  Same dict. Loop through and print all values.
dic = {
        "server-1": "online",
        "server-2": "offline",
        "server-3": "online",
        "server-4": "degraded"
        }
for key, value in dic.items():
    print(f'{key}: {value}')

for key,value in dic.items():
    print(value)
