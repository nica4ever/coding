# 9. Given log lines, return all lines between two timestamps.

logs = [
    "2024-03-15 09:55:01 INFO auth-service Pre-window event",
    "2024-03-15 10:00:05 ERROR payment-gateway Transaction declined",
    "2024-03-15 10:00:08 WARN db-primary Slow query",
    "2024-03-15 10:00:12 INFO api-server Request OK",
    "2024-03-15 10:15:18 ERROR auth-service Connection refused",
    "2024-03-15 10:30:22 INFO worker-queue Job completed",
    "2024-03-15 10:45:30 ERROR cache-redis Cache miss",
    "2024-03-15 11:00:35 WARN load-balancer High latency",
    "2024-03-15 11:15:40 INFO db-replica Replication OK",
    "2024-03-15 12:00:00 INFO auth-service Post-window event",
]

start = "2024-03-15 10:00:00"
end = "2024-03-15 11:00:00"

def filter_by_window(logs, start, end):
    result = []
    for line in logs:
        parts = line.split()
        timestamp = parts[0] + " " + parts[1]
        if start <= timestamp <= end:
            result.append(line)
    return result
print(filter_by_window(logs, start, end))
