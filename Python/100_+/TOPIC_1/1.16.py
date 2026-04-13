# 16. Given log lines, find the longest message (by character count).

logs = [
    "2024-03-15 10:00:01 INFO auth-service Started",
    "2024-03-15 10:00:05 ERROR payment-gateway Transaction declined after multiple retries due to upstream service unavailability",
    "2024-03-15 10:00:05 ERROR payment-gateway Transaction declined after multiple retries due to upstream service unavailability THIS SHOULD BE THE LONGEST LINE",
    "2024-03-15 10:00:08 WARN db-primary Slow query",
    "2024-03-15 10:00:12 INFO api-server Request OK",
    "2024-03-15 10:00:18 ERROR auth-service Connection refused",
    "2024-03-15 10:00:22 INFO worker-queue Job completed in 1.2s",
    "2024-03-15 10:00:30 ERROR cache-redis Cache miss for session_token_xyz_user_4892",
    "2024-03-15 10:00:35 WARN load-balancer High latency detected on backend pool with circuit breaker engaging soon",
    "2024-03-15 10:00:40 INFO db-replica Replication OK",
]
def longest_line(logs):
    tracker = 1
    longest = None
    for line in logs:
        parts = line.split()
        group = " ".join(parts[4:])
        if tracker < len(group):
            tracker = len(group)
            longest = group
    return longest
print(longest_line(logs))
