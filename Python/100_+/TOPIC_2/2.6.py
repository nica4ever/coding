# 26. Given a list of (service, response_time_ms) tuples,
#     return average response time per service.
from collections import defaultdict

response_times = [
    ("auth-service", 120),
    ("payment-gateway", 450),
    ("auth-service", 85),
    ("api-server", 200),
    ("payment-gateway", 380),
    ("auth-service", 95),
    ("db-primary", 15),
    ("api-server", 180),
    ("payment-gateway", 520),
    ("auth-service", 110),
    ("db-primary", 22),
    ("api-server", 190),
    ("cache-redis", 5),
    ("cache-redis", 8),
    ("db-primary", 18),
]

def average_time(logs):
    groups = defaultdict(list)
    for service, time in logs:
        groups[service].append(time)
    return {service: sum(times) / len(times) for service, times in groups.items()}

print(average_time(response_times))
