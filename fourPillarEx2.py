# Define a method in your Square class called change_size. That allows you to pass in a number that increases or 
# decreases (if the number is negative) each side of a Square object by that number. Make sure your Square's class
# instnace variable is set to self.s1.

class Square:
    def __init__(self, s):
        self.s1 = s
    def change_size(self):
        if self.s1 > 0:
            self.s1 +=1
        elif self.s1 < 0:
            self.s1 -=1
        else:
            pass
        return self.s1

square = Square(int(input("Enter a size: ")))
print(square.change_size())

# The solution they give 
class Square():
    def __init__(self, s1):
        self.s1 = s1
    def change_size(self, new_size):
        self.s1 += new_size