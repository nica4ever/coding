servers_status = {
         "new-dawn-1": "online",
         "new-dawn-2": "offline",
         "new-dawn-3": "offline",
         "new-dawn-4": "online",
         "new-dawn-5": "offline",
         "new-dawn-6": "degraded",
         }
def check_server("new-dawn-3", serve:
    for key, value in dic.items():
        print(f'Server: {key} Status: {value}')

check_server(servers_status)
