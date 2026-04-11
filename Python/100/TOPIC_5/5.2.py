# 5.2  Split "192.168.1.1" on "." — print each octet.

string = "192.168.1.1"
print(string)

ls = string.split(".")
for i in ls:
    print(i)
