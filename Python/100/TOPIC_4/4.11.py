# 4.11 Write a function is_palindrome(s) that returns True if the string
#      reads the same forwards and backwards. Test with "racecar" and "hello".
string = "racecar"
nstring = "hello"
def is_palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

print(string)
print(is_palindrome(string))
print("")
print(nstring)
print(is_palindrome(nstring))
