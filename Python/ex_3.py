servers_status = {
         "new-dawn-1": "online",
         "new-dawn-2": "offline",
         "new-dawn-3": "offline",
         "new-dawn-4": "online",
         "new-dawn-5": "offline",
         "new-dawn-6": "degraded",
         }

ofl = 0

for key, value in servers_status.items():
    print(key, value)
    if value == "offline":
        ofl += 1
print(f'Offline: {ofl}')

if "new-dawn-3" in servers_status:
    print("new-dawn-3 was found")
else:
    print("new-dawn-3 was not found")


