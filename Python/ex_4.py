servers_status = {
         "new-dawn-1": "online",
         "new-dawn-2": "offline",
         "new-dawn-3": "offline",
         "new-dawn-4": "online",
         "new-dawn-5": "offline",
         "new-dawn-6": "degraded",
         }

def check_server(name, dic):
    return dic.get(name, "not found")

def count_by_status(dic, status):
    i = 0
    for key, value in dic.items():
        if value == status:
            i += 1
    return i
        
print(f'new-dawn-3: {check_server("new-dawn-3", servers_status)}')
print(f'new-dawn-XD: {check_server("new-dawn-XD", servers_status)}')

print(count_by_status(servers_status, "online"))
print(count_by_status(servers_status, "offline"))
print(count_by_status(servers_status, "degraded"))
