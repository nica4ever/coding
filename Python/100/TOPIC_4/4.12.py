# 4.12 Write a function count_vowels(s) that returns how many vowels are in a string.
#      Vowels: a, e, i, o, u (lowercase only is fine).
string = "hello"
string_2 = "racecar"
string_3 = "nnn"
def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    x = 0
    for i in s:
        if i in vowels:
            x += 1
    return x

print(count_vowels(string))
print(count_vowels(string_2))
print(count_vowels(string_3))
