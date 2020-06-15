# Write a function that takes two objects as parameters and 
# returns True if they have the same object, False if not.

def check(a , b):
    return a is b

print(check("a","a"))
print(check(12, 13))
print(check("a", "b"))
print(check(100, 100))

