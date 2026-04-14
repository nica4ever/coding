# 22. Given the same list, return the percentage of error codes (4xx and 5xx).
from collections import Counter

status_codes = [200, 404, 500, 200, 200, 404, 200, 301, 500, 200, 404, 503, 200, 502]

def count(status):
    if not status:
        return 0.0
    total = len(status)
    errors = sum(1 for c in status if 400 <= c < 600)
    return round((errors / total) * 100, 2) 
print(count(status_codes))
