# Create a Square class that has one method that calculates its perimeter. when you print Square object,
# a message should print telling you the length of each of the four sides of the shape. For example,
# the code print(Square(29)) should print "29 by 29 by 29 by 29".

class Square:
    def __init__(self, s):
        self.side = s
    
    def calc_peri(self):
        return 4 * self.side
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

print(Square(11))

