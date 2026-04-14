# 23. Given a list of IPs from access logs, find the top 3 most frequent IPs.
from collections import Counter

access_log_ips = [
    "10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.5", "10.0.0.3",
    "10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.4", "10.0.0.2",
    "10.0.0.1", "10.0.0.3", "10.0.0.2", "10.0.0.5", "10.0.0.1",
    "10.0.0.2", "10.0.0.4", "10.0.0.1", "10.0.0.2", "10.0.0.3",
    "10.0.0.6", "10.0.0.1", "10.0.0.2", "10.0.0.7", "10.0.0.3",
]

def most_used_ips(logs, n=3):
    return Counter(logs).most_common(n)

print(most_used_ips(access_log_ips, ))
print(most_used_ips(access_log_ips, 2))
print(most_used_ips(access_log_ips, 5))
