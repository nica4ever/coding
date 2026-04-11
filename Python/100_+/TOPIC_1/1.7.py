# 7. Given log lines, return the FIRST ERROR line found, or None if no errors.

logs = [
    "2024-03-15 10:00:01 INFO auth-service Started",
    "2024-03-15 10:00:05 INFO api-server Request OK",
    "2024-03-15 10:00:08 WARN db-primary Slow query",
    "2024-03-15 10:00:12 ERROR payment-gateway Transaction declined",
    "2024-03-15 10:00:18 INFO worker-queue Job completed",
    "2024-03-15 10:00:22 ERROR auth-service Connection refused",
    "2024-03-15 10:00:30 ERROR cache-redis Cache miss",
]

def find_error(log):
    for line in log:
        if line.split()[2] == "ERROR":
            return line
    return None

result = find_error(logs)
if result is None:
    print("No ERROR found")
else:
    print(result)
