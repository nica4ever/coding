# 4.18 Write a function that takes a string and returns a dict counting
#      how many times each character appears.
#      Example: char_count("aab") -> {"a": 2, "b": 1}
def char_count(x):
    dic = {}
    count = 0
    for i in x:
        if i in dic:
            count += 1
            dic[i] = count
        else:
            count = 1
            dic[i] = count
    return dic

print(char_count("aaabbcccc"))
        
