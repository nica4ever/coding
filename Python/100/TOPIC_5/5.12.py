# 5.12 Split "user1:admin:active" and "user2:viewer:inactive" on ":"
#      Store each as a dict with keys "username", "role", "status".
#      Put both dicts in a list. Print.

string_1 = "user1:admin:active"
string_2 = "user2:viewer:inactive"

def dic(st):
    dic = {}
    dic["username"] = st.split(":")[0]
    dic["role"] = st.split(":")[1]
    dic["status"] = st.split(":")[2]
    return dic

print(dic(string_1))
print(dic(string_2))
