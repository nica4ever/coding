# 5.7  Split "2024-03-15 14:30:00 ERROR auth-service Connection refused"
#      Store date, time, level, service, message in separate variables. Print each.
string = "2024-03-15 14:30:00 ERROR auth-service Connection refused"
date = string.split(" ")[0]
time = string.split(" ")[1]
level = string.split(" ")[2]
service = string.split(" ")[3]
message = string.split(" ")[4] + " " + string.split(" ")[5]
print(date, time, level, service, message)
