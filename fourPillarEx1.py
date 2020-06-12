# Create a Rectangle and Square classes. Rectangle should have two instance varaibles: self.width and self.len. 
# Square should just have one instnace variable self.1. Define a method for both classes called calculate_perimeter
# that calculates the perimeter of the shapes they represent and return it. Then, create Rectangle and Square objects
# and call the method on both of them.

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        print(2 * (self.width + self.len))

class Square:
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        print(4 * self.side)

a_rec = Rectangle(2, 4)
a_sq = Square(2)
a_rec.calculate_perimeter()
a_sq.calculate_perimeter()


# Solutino they wanted 
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
       return 2 * (self.width + self.len)

class Square:
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        return 4 * self.side

a_rec = Rectangle(2, 4)
a_sq = Square(2)
print(a_rec.calculate_perimeter())
print(a_sq.calculate_perimeter())