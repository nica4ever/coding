# 5.6  Given the list ["hello", "world", "foo"] — join them into one string
#      with " - " between each. Print.
ls = ["hello", "world", "foo"]
string = ls[0] + "-" + ls[1] + "-" + ls[-1]
print(string)
