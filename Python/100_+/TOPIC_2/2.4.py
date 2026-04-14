# 24. Given a list of IPs, find IPs that made more than N requests
#     (N is a function argument).
from collections import Counter

access_log_ips = [
    "10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.5", "10.0.0.3",
    "10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.4", "10.0.0.2",
    "10.0.0.1", "10.0.0.3", "10.0.0.2", "10.0.0.5", "10.0.0.1",
    "10.0.0.2", "10.0.0.4", "10.0.0.1", "10.0.0.2", "10.0.0.3",
    "10.0.0.6", "10.0.0.1", "10.0.0.2", "10.0.0.7", "10.0.0.3",
]

def noisy_ip(logs, N):
    return sorted([key for key, value in Counter(logs).items() if value > N])

print(noisy_ip(access_log_ips, 3))
print(noisy_ip(access_log_ips, 5))
print(noisy_ip(access_log_ips, 100))
