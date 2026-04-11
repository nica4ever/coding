# 5. Given log lines with format "TIMESTAMP LEVEL SERVICE MESSAGE",
#    return only lines from "auth-service".

logs = [
    "2024-03-15 10:00:01 INFO auth-service User login successful",
    "2024-03-15 10:00:05 ERROR payment-gateway Transaction declined",
    "2024-03-15 10:00:08 WARN auth-service Token expiring soon",
    "2024-03-15 10:00:12 INFO api-server Request processed",
    "2024-03-15 10:00:18 ERROR auth-service Connection refused",
    "2024-03-15 10:00:22 INFO db-primary Query executed",
    "2024-03-15 10:00:30 ERROR auth-service Authentication failed",
    "2024-03-15 10:00:35 WARN cache-redis Memory at 85%",
    "2024-03-15 10:00:40 INFO auth-service Session created",
]

auth_service = [line for line in logs if line.split()[3] == "auth-service"]
print(auth_service)
