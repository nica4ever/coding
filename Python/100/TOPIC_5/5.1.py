# 5.1  Split "ERROR auth-service Timeout" into a list. Print each part separately.

string = "ERROR auth-service Timeout"
print(string)
print("")

ls = string.split()
for i in ls:
    print(i)
