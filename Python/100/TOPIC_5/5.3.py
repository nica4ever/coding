# 5.3  Split "name=Nika" on "=". Store in a dict {key: value}. Print.

string = "name=Nika"

dic = {}
dic[string.split("=")[0]] = string.split("=")[1]
print(dic)
