import random
from datetime import datetime

servers = [
        "new-dawn-1",
        "new-dawn-2",
        "new-dawn-3",
        "new-dawn-4"
        ]

now = datetime.now()

print(f'date: {now.strftime("%d-%m-%Y %H:%M:%S")} server: {random.choice(servers)}')
