# 3.11 Create a dict of 5 students and their grades (integers).
#      Loop through and print only students with grade above 80.
dic = {"Andrei": 30, "Mihai": 15, "Alex": 90}
x = 80
filtered_dic = {key: value for key, value in dic.items() if value > x}
print(filtered_dic)
