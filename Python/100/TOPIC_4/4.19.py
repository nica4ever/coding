# 4.19 Write a function that takes a list of dicts like:
#      [{"name": "Ana", "age": 25}, {"name": "Ion", "age": 30}]
#      and returns the name of the oldest person
import random


def gen_random():
    names = ["Ana", "Alex", "Vladimir", "Suzan", "Rob", "Mary", "Andrew", "Peter"]
    dic = {}
    for i in range(1,2):
        dic["name"] = random.choice(names)
        dic["age"] = random.randint(1, 81)
    return dic


dic_1 = gen_random()
dic_2 = gen_random()
dic_3 = gen_random()
print(dic_1, dic_2, dic_3)

def extract(dic):
    name_age = {}
    for key, value in dic.items():
        name_age[dic.get("name")] = dic.get("age")
    return name_age

def oldest(x, y, z):
    dic_join_1 = extract(x) | extract(y)
    dic_main = dic_join_1 | extract(z)
    x = 0
    for key, value in dic_main.items():
        if value > x:
            x = value
    for key, value in dic_main.items():
        if value == x:
            return key

print(oldest(dic_1, dic_2, dic_3))
