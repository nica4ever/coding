# 5.14 Given "/var/log/nginx/access.log" — split on "/" and print only the filename.
string = "/var/log/nginx/access.log"
print(string.split("/")[-1])
