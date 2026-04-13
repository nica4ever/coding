# 19. Given log lines, return only lines that DON'T contain certain noise keywords
#     (e.g., "heartbeat", "health-check", "ping").

logs = [
    "2024-03-15 10:00:01 INFO auth-service Started",
    "2024-03-15 10:00:02 INFO health-check Heartbeat OK",
    "2024-03-15 10:00:05 ERROR payment-gateway Transaction declined",
    "2024-03-15 10:00:07 INFO health-check ping",
    "2024-03-15 10:00:08 WARN db-primary Slow query",
    "2024-03-15 10:00:10 INFO monitoring heartbeat received",
    "2024-03-15 10:00:12 INFO api-server Request OK",
    "2024-03-15 10:00:15 DEBUG health-check Ping response 200",
    "2024-03-15 10:00:18 ERROR auth-service Connection refused",
    "2024-03-15 10:00:20 INFO load-balancer Heartbeat all backends OK",
    "2024-03-15 10:00:22 INFO worker-queue Job completed",
    "2024-03-15 10:00:25 DEBUG monitoring Health-Check executed",
    "2024-03-15 10:00:30 ERROR cache-redis Cache miss",
]

noise_keywords = ("heartbeat", "health-check", "ping")

def strip_noise(logs, noise_keywords):
    no_noise = []
    for line in logs:
        if any(noise in line.lower() for noise in noise_keywords):
            continue
        no_noise.append(line)
    return no_noise
print(strip_noise(logs, noise_keywords))
