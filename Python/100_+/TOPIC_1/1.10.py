# 10. Given log lines with format "LEVEL: message", parse each into
#     a dict {"level": ..., "message": ...} and return list of dicts.

logs = [
    "INFO: User login successful",
    "ERROR: Connection refused",
    "WARN: High latency detected",
    "INFO: Health check passed",
    "ERROR: Database timeout",
    "WARN: Disk usage at 85%",
    "INFO: Backup completed",
    "ERROR: Authentication failed",
]

def parse_logs(logs):
    parsed = []
    for line in logs:
        parts = line.split(":", 1)
        entry = {
                "level": parts[0],
                "message": parts[1].strip()
            }
        parsed.append(entry)
    return parsed

print(parse_logs(logs))
