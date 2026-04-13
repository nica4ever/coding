# 13. Given log lines, return only lines that have a 4xx or 5xx HTTP status code
#     at the end (assume status is the last token).
logs = [
    "10.0.0.1 GET /index.html 200",
    "10.0.0.2 POST /api/login 401",
    "10.0.0.3 GET /style.css 200",
    "10.0.0.1 GET /missing.html 404",
    "10.0.0.4 POST /api/payment 500",
    "10.0.0.2 GET /admin 403",
    "10.0.0.5 GET /home 200",
    "10.0.0.3 PUT /api/users/1 204",
    "10.0.0.1 GET /broken 500",
    "10.0.0.6 GET /old-page 301",
]

def filter_errors(logs):
    result = []
    for line in logs:
        status = int(line.split()[-1])
        if 400 <= status < 600:
            result.append(line)
    return result

print(filter_errors(logs))
