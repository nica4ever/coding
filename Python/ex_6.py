logs = [
    "ERROR auth-service Connection refused",
    "INFO api-server Request OK",
    "ERROR payment-gateway Timeout",
    "ERROR auth-service Timeout",
    "INFO api-server Health check passed",
    "ERROR auth-service Connection refused",
    ]

def count_errors_by_service(logs):
    logs_dic = {}
    for line in logs:
        part = line.split()
        service = part[1]
        status = part[0]
        if status == "ERROR":
            if service in logs_dic:
                logs_dic[service] += 1
            else:
                logs_dic[service] = 1
    return logs_dic

def most_errors(error_counts):
    best = ""
    highest = 0
    for key, value in error_counts.items():
        if value > highest:
            highest = value
            best = key
    return best

result = count_errors_by_service(logs)
worst = most_errors(result)

print(result)
print(worst)




