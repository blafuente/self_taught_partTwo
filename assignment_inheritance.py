# Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when
# called. Change your Square and Rectangle classes from the previous challenges to inherit from Shape,
# create Square and Rectangle, and call the new method on both of them.

class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        print(2 * (self.width + self.len))

class Square(Shape):
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        print(4 * self.side)

a_square = Square(2)
a_square.what_am_i()
a_rec = Rectangle(2, 4)
a_rec.what_am_i()