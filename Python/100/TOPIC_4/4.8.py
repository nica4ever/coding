# 4.8  Write a function that takes a string and RETURNS a dict with:
#      - "length": length of the string
#      - "upper": string in uppercase
#      - "words": number of words (split and count)
string = "this is a string"
def ict(x):
    dic = {}
    dic["lenght"] = len(x)
    dic["upper"] = x.upper()
    dic["words"] = len(x.split())
    return dic

print(ict(string))
