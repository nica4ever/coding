# 4.15 Write a function that takes a sentence (string) and returns the
#      longest word in that sentence.
sentence = "The alphanumeric word is the longest"
def longest_word(x):
    y = 0
    for i in x.split():
        count = len(i)
        if count > y:
            y = count
    return y
print(longest_word(sentence))
