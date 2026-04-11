# 1. Given a list of log lines like "2024-03-15 10:00:01 INFO Started",
#    extract just the timestamps into a new list.

logs = [
    "2024-03-15 10:00:01 INFO Started",
    "2024-03-15 10:00:05 ERROR Connection refused",
    "2024-03-15 10:00:12 WARN High latency",
]

timestamps = []
for line in logs:
    parts = line.split()
    timestamp = parts[0] + " " + parts[1]
    timestamps.append(timestamp)

print(timestamps)
