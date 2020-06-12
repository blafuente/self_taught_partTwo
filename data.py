# OOP example for encapsulation  

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    def change_data(self, index, n):
        self.nums[index] = n

data = Data()

print(data.nums)

# You can change the data in the list by directly accessing it
data.nums[0] = 100
print(data.nums)

# Or change it by using the change_data method
data.change_data(1, 99)
print(data.nums)

# if the list was changed into a tuple, it will break the code