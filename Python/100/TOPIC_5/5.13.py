# 5.13 Given "ERROR,WARN,ERROR,INFO,ERROR,INFO,INFO"
#      Split on comma, then count how many of each level there are.
#      Store in a dict. Print.

string = "ERROR,WARN,ERROR,INFO,ERROR,INFO,INFO"
dic = {}

for item in string.split(","):
    if item in dic:
        dic[item] += 1 
    else:
        dic[item] = 1
print(dic)
