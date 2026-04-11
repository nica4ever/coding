# 12. Given log lines, count how many are ERROR vs WARN vs INFO.
#     Return as dict.

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
    "2024-03-15 10:00:45 ERROR worker-queue Task failed",
    "2024-03-15 10:00:50 INFO auth-service Login OK",
    "2024-03-15 10:00:55 WARN cache-redis Memory at 90%",
]

def count_levels(logs, allowed):
    counts = {}
    for line in logs:
        level = line.split()[2]
        if level not in allowed:
            continue
        counts[level] = counts.get(level, 0) + 1
    return counts

print(count_levels(logs, ("ERROR", "WARN", "INFO")))
print(count_levels(logs, ("ERROR",)))
print(count_levels(logs, ("DEBUG", "TRACE")))
