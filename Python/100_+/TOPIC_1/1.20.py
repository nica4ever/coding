# 20. Given log lines, find duplicates (lines that appear more than once)
#     and return them with their counts.
from collections import Counter

logs = [
    "2024-03-15 10:00:01 INFO auth-service Started",
    "2024-03-15 10:00:05 ERROR payment-gateway Transaction declined",
    "2024-03-15 10:00:08 WARN db-primary Slow query",
    "2024-03-15 10:00:01 INFO auth-service Started",
    "2024-03-15 10:00:12 INFO api-server Request OK",
    "2024-03-15 10:00:08 WARN db-primary Slow query",
    "2024-03-15 10:00:18 ERROR auth-service Connection refused",
    "2024-03-15 10:00:01 INFO auth-service Started",
    "2024-03-15 10:00:22 INFO worker-queue Job completed",
    "2024-03-15 10:00:30 ERROR cache-redis Cache miss",
    "2024-03-15 10:00:05 ERROR payment-gateway Transaction declined",
    "2024-03-15 10:00:35 WARN load-balancer High latency",
]

def duplicates(logs):
    counts = Counter(logs)
    return {line: count for line, count in counts.items() if count > 1}
print(duplicates(logs))
