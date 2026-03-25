import random

servers = [
        "new-dawn-1",
        "new-dawn-2",
        "new-dawn-3",
        "new-dawn-4",
        "new-dawn-5",
        "new-dawn-6",
        ]
servers.append('new-dawn-7')

for i, value in enumerate(servers, start=1):
    print(f'{i}: {value}')

print(f'Total servers: {len(servers)}')
