# Python relies on Magic Methods when it evaluates expressions. 

# 2 + 2
# For example, in this expression, integer object has a magic method named "add" that Python calls when
# it evaluates the expression. If you override this method, you can create objects that perform additions
# however you want. 

# When Python evaluates an expression with AlwaysPositive objects...
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    # It calls the "add" method on the first operand 
    # passes the second operand object into add as a parameter
    def __add__(self, other):
        # and returns the result
        return abs(self.n + other.n) # returns the absolute value

# In this case, your code adds the first AlwaysPositive object..
x = AlwaysPositive(-20)
# to the second object and returns its absolute value
y = AlwaysPositive(10)

print(x + y)