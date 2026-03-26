# 1.15 Create a string "auth-service". Check if it starts with "auth". Print True or False.
string = "auth-service"
f = string.split("-")[0]
s = string.split("-")[1]
if f == "auth":
    print("True")
else:
    print("False")
