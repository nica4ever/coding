# 4. Given log lines, return only lines from a specific date "2024-03-15".

logs = [
    "2024-03-15 10:00:01 INFO Started",
    "2024-03-14 23:59:55 WARN Pre-deploy check",
    "2024-03-15 10:00:05 ERROR Connection refused",
    "2024-03-16 00:00:12 INFO New day rollover",
    "2024-03-15 10:00:18 ERROR Database timeout",
    "2024-03-13 14:22:00 INFO Backup completed",
    "2024-03-15 10:00:22 INFO Health check passed",
    "2024-03-15 10:00:30 ERROR Authentication failed",
    "2024-03-16 01:15:44 WARN High latency",
    "2024-03-15 10:00:35 WARN Disk usage at 85%",
]

date_line = [line for line in logs if line.split()[0] == "2024-03-15"]
print(date_line)
