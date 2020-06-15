class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []
    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory = {}

customer = Customer("Joe", "joe@gmail.com")
print(customer.name)
print(customer.email)