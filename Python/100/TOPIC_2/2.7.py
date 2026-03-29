# 2.7  Create a list of 5 server names. Use enumerate to print index and name.
servers = [
        "new-dawn-1",
        "new-dawn-2",
        "new-dawn-3",
        "new-dawn-4",
        "new-dawn-5"
        ]
for i, item in enumerate(servers, start=1):
    print(f'{i}:{item}')
