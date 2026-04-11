# 6. Given log lines, return lines where the message contains "timeout"
#    (case-insensitive).
logs = [
    "2024-03-15 10:00:01 INFO auth-service User login successful",
    "2024-03-15 10:00:05 ERROR payment-gateway Connection TIMEOUT exceeded",
    "2024-03-15 10:00:08 WARN db-primary Query slow",
    "2024-03-15 10:00:12 INFO api-server Request timeout reached",
    "2024-03-15 10:00:18 ERROR auth-service Database TimeOut on session",
    "2024-03-15 10:00:22 INFO worker-queue Job completed",
    "2024-03-15 10:00:30 ERROR cache-redis Cache miss for key",
    "2024-03-15 10:00:35 WARN load-balancer Backend timeout warning",
    "2024-03-15 10:00:40 INFO db-replica Replication lag normal",
    "2024-03-15 10:00:45 ERROR worker-queue Task TIMEOUT after 30s",
]

time_out = [line for line in logs if "timeout" in line.lower()]
print(time_out)
