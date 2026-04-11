# 11. Given a single log line "2024-03-15 10:00:01 [ERROR] [auth-service] Connection refused",
#     extract date, time, level, service, message into a dict.
#     Watch out for the bracketed fields.

log = "2024-03-15 10:00:01 [ERROR] [auth-service] Connection refused"

def parse_log(log):
    parts = log.split()
    parsed = {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2].strip("[]"),
            "service": parts[3].strip("[]"),
            "message": " ".join(parts[4:])
                }
    return parsed

print(parse_log(log))
