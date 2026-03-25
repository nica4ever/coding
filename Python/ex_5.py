log = "ERROR auth-service Connection refused"
parts = log.split()
level = log.split(' ')[0]
service = log.split(' ')[1]
message = log.split (' ', 2)[2]
error_message = {
        "Error": level,
        "Service": service,
        "Message": message
        }
print(error_message)
