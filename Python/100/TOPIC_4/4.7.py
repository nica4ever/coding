# 4.7  Write a function with a DEFAULT argument:
#      greet(name, greeting="Hello") -> returns "{greeting}, {name}"
#      Call it with and without the greeting argument.
def greet(name, greeting="Hello"):
    return (f'{greeting}, {name}')
print(greet("Nika", greeting="Hello"))
