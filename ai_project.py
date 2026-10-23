class Laptop:
    def __init__(self, brand, ram):
        brand = brand
        ram = ram

    def details(self):
        print(self.brand, self.ram)

l1 = Laptop("HP", 8)
l1.details()
