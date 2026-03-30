# 3.9  Create a dict. Use .get() to access a key that EXISTS. Print.
dic = {"key": "spec", "nkey": "nspec"}
print(dic.get("key", "spec"))
print(dic.get("skey", "default"))
