# 4.17 Write a function that takes a dict of {name: score} and a threshold.
#      Returns a list of names whose score is ABOVE the threshold.
import random
def random_dic():
    dic = {}
    for i in range(1, 11):
        dic[f'Server-{i}'] = random.randint(1, 100)
    return dic
random_dic = random_dic()
print(random_dic)
def above_threshold(dic, x):
    lst = []
    for key, value in dic.items():
        if value > x:
            lst.append(key)
    return lst
print(above_threshold(random_dic, 50))
            
