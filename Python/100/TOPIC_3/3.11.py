# 3.11 Create a dict of 5 students and their grades (integers).
#      Loop through and print only students with grade above 80.
dic = {"Andrei": "30", "Mihai": "15", "Alex": "90"}
for key, value in dic.items():
    if value > 80:
        print(key, value)
