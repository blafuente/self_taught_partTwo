# Add a square_list variable to a class called Square and set your class up so that every time you create 
# a new Square object, the new object gets added to the square list.

class Square():
    
    square_list = []
    
    def __init__(self,s):
        self.side = s 
        self.square_list.append((self.side))

sq1 = Square(2)
sq2 = Square(3)
sq3 = Square(43)

print(Square.square_list)

# Solution they have 
class Square1():

    square_list1 = []

    def __init__(self):
        self.square_list1.append(self)
