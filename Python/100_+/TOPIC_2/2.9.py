# 29. Same list. Return the top 5 processes by CPU usage.
from collections import defaultdict

processes = [
    {"pid": 1234, "cpu": 45.2, "name": "nginx"},
    {"pid": 1235, "cpu": 12.8, "name": "postgres"},
    {"pid": 1236, "cpu": 78.5, "name": "nginx"},
    {"pid": 1237, "cpu": 8.3, "name": "systemd"},
    {"pid": 1238, "cpu": 92.1, "name": "python3"},
    {"pid": 1239, "cpu": 34.6, "name": "postgres"},
    {"pid": 1240, "cpu": 2.1, "name": "cron"},
    {"pid": 1241, "cpu": 55.4, "name": "nginx"},
    {"pid": 1242, "cpu": 18.9, "name": "redis-server"},
    {"pid": 1243, "cpu": 67.2, "name": "python3"},
]

def top_five(logs):
    for line in logs:
        return sorted(logs, key=lambda p: p["cpu"], reverse=True)[:5]
print(top_five(processes))
