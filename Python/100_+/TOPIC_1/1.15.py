# 15. Given log lines, return them grouped by level into a dict
#     {"ERROR": [...], "WARN": [...], "INFO": [...]}.

from collections import defaultdict

logs = [
    "2024-03-15 10:00:01 INFO auth-service Started",
    "2024-03-15 10:00:05 ERROR payment-gateway Transaction declined",
    "2024-03-15 10:00:08 WARN db-primary Slow query",
    "2024-03-15 10:00:12 INFO api-server Request OK",
    "2024-03-15 10:00:18 ERROR auth-service Connection refused",
    "2024-03-15 10:00:22 INFO worker-queue Job completed",
    "2024-03-15 10:00:30 ERROR cache-redis Cache miss",
    "2024-03-15 10:00:35 WARN load-balancer High latency",
    "2024-03-15 10:00:40 INFO db-replica Replication OK",
]

def group_level(logs):
    groups = defaultdict(list)
    for line in logs:
        level = line.split()[2]
        groups[level].append(line)
    return dict(groups)

print(group_level(logs))
