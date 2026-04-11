# 5.20 Given "server=web-01;port=8080;status=online;cpu=72"
#      Parse into dict: {"server": "web-01", "port": "8080", "status": "online", "cpu": "72"}
#      Then convert "port" and "cpu" values to integers.
#      Print the dict.

log = "server=web-01;port=8080;status=online;cpu=72"
pairs = log.split(";")

result = {}
for pair in pairs:
    key, value = pair.split("=")
    result[key] = value

result["port"] = int(result["port"])
result["cpu"] = int(result["cpu"])

print(result)


