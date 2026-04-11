# 2. Same list. Extract just the log levels (INFO, WARN, ERROR).
logs = [
    "2024-03-15 10:00:01 INFO Started",
    "2024-03-15 10:00:05 ERROR Connection refused",
    "2024-03-15 10:00:12 WARN High latency",
]

log_level = []

for line in logs:
    part = line.split()
    level = part[2]
    log_level.append(level)
print(log_level)
