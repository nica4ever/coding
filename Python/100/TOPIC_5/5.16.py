# 5.16 Split "10.0.0.1 - GET /index.html 200"
#      Store in a dict with keys: "ip", "method", "path", "status"
#      (skip the "-")
string = "10.0.0.1 - GET /index.html 200"

dic = {}
dic["ip"] = string.split()[0]
dic["method"] = string.split()[2]
dic["path"] = string.split()[3]
dic["status"] = string.split()[4]
print(dic)
