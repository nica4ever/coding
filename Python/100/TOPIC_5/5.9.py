# 5.9  Split "GET /api/users HTTP/1.1" into method, path, protocol.
#      Store in a dict with those keys. Print.
string = "GET /api/users HTTP/1.1"
dic = {}
dic["method"] = string.split()[0]
dic["path"] = string.split()[1]
dic["protocol"] = string.split()[2]
print(dic)
