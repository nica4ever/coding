# 21. Given a list of HTTP status codes [200, 404, 500, 200, 200, 404],
#     count occurrences of each. Return dict.
from collections import Counter

status_codes = [200, 404, 500, 200, 200, 404, 200, 301, 500, 200, 404, 503, 200, 502]

def count(status):
    return dict(Counter(status))
print(count(status_codes))
