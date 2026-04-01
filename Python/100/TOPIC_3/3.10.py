# 3.9  Create a dict. Use .get() to access a key that EXISTS. Print.
# 3.10 Same dict. Use .get() on a key that DOESN'T exist, with a default value. Print.
dic = {"key": "spec", "nkey": "nspec"}
print(dic.get("key", "spec"))
print(dic.get("skey", "default"))
