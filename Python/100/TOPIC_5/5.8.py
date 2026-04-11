# 5.8  Given a list of 3 log strings (you make them up), split each one
#      and store level + service in a list of tuples. Print the list.
#      Example result: [("ERROR", "auth"), ("INFO", "api"), ("WARN", "db")]
log_1 = "ERROR auth service down"
log_2 = "INFO api request received"
log_3 = "WARN db connection slow"

def log_list(log):
    log_list = []
    log_list.append((log.split()[0], log.split()[1]))
    return log_list
logs = log_list(log_1) + log_list(log_2) + log_list(log_3)
print(logs)

