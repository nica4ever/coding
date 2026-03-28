# 1.12 Import datetime. Get current time. Print it formatted as "DD/MM/YYYY".
from datetime import datetime
now = datetime.now()
print(f'{now.strftime("%d-%m-%Y %H:%M:%S")}')

