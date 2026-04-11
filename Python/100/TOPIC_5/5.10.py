# 5.10 Given "cpu:85,mem:72,disk:45" — parse it into a dict:
#      {"cpu": 85, "mem": 72, "disk": 45}
#      Values must be integers, not strings.
string = "cpu:85,mem:72,disk:45"
string_list = string.split(",")
result = {}
for item in string_list:
    key, value = item.split(":")
    result[key] = int(value)
print(result)
