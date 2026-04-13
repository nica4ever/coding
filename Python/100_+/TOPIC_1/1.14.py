# 14. Given log lines with timestamps, sort them chronologically.
logs = [
    "2024-03-15 10:30:22 INFO worker-queue Job completed",
    "2024-03-15 09:15:01 INFO auth-service Started",
    "2024-03-15 11:45:18 ERROR cache-redis Cache miss",
    "2024-03-15 08:00:05 WARN db-primary Pre-warmup",
    "2024-03-15 14:22:30 ERROR payment-gateway Declined",
    "2024-03-15 10:00:12 INFO api-server Request OK",
    "2024-03-15 13:55:40 INFO db-replica Replication OK",
    "2024-03-15 07:30:00 INFO auth-service Boot",
    "2024-03-15 12:15:08 WARN load-balancer Latency",
]

def sorted_logs(logs):
    return sorted(logs, key=lambda line: line.split()[0] + " " + line.split()[1])

print(sorted_logs(logs))
