# 27. Given the same list, return the slowest response time per service.
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

def slowest_time(logs):
    groups = defaultdict(list)
    for service, time in logs:
        groups[service].append(time)
    return {service: max(time) for service, time in groups.items()}
        

print(slowest_time(response_times))
        
