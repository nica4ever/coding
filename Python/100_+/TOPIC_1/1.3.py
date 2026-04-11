# 3. Given mixed log levels, return only the ERROR lines.

logs = [
    "2024-03-15 10:00:01 INFO Started",
    "2024-03-15 10:00:05 ERROR Connection refused",
    "2024-03-15 10:00:12 WARN High latency",
    "2024-03-15 10:00:18 ERROR Database timeout",
    "2024-03-15 10:00:22 INFO Health check passed",
    "2024-03-15 10:00:30 ERROR Authentication failed",
    "2024-03-15 10:00:35 WARN Disk usage at 85%",
]

error_lines = []

for line in logs:
    part = line.split()
    if part[2] == "ERROR":
        error_lines.append(line)

print(error_lines)


