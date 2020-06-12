class Orange:
    def __init__(self):
        print(self)

orange = Orange()
print(orange)

# You can use self to define an instance variable a variable that belongs to an object like this.

# class Orange:
#     def __init__(self, w , c):
#         self.weight = w
#         self.color = c
#         print("Created!")

class Apple:
    def __init__(self, w , c):
        self.weight = w
        self.color = c

apple_one = Apple(2, "red")
apple_two = Apple(9, "light red")
apple_three = Apple(7, "green")

print(apple_one)
print(apple_one.weight)
print(apple_one.color)
print("\n")

# You can change the value of an instance variable like this. 
# In this case, you orange obejcts weight started 10 but you changed it to 100. 

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c

or1 = Orange(10, "dark orange")
print(or1.weight)
print(or1.color)
print("\n")

or1.weight = 100
or1.color = "light orange"
print(or1.weight)
print(or1.color)
print("\n")

# Oranges also do things like rot, that you can model with methods.
# Here is how you can give the orange the ability to rot, rot accepts two paramters.

class Orange2:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
    def rot(self, days, temp):
        self.mold = days * temp

orange2 = Orange2(6, "orange")
print(orange2.mold)
orange2.rot(10 , 98)
print(orange2.mold)

# You can define multiple methods in a class. 
class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    # method to calculate its area
    def area(self):
        return self.width * self.len
    # method to change its size
    def change_size(self, w, l):
        self.width = w
        self.len = l


class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed 
        self.owner = owner 

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanely", "Bulldog", mick)
print(stan.owner.name)