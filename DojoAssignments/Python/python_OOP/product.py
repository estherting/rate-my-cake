class Product:
    def __init__(self, price, name, weight, brand, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.price = (1-tax) * self.price
        return self

    def Return(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "in-box":
            self.status = "for sale"
        if reason_for_return == "open-box":
            self.status = "used"
            self.price = 0.8*self.price
        return self
    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Name: " + self.name
        print "Weight: " + str(self.weight) + "lb"
        print "Brand: " + self.brand
        print "Status: " + self.status
        return self

computer = Product(8000, "Computer", 5, "Apple", "for Sale")
computer.displayInfo()
computer.Return("open-box")
computer.displayInfo()
computer.addTax(0.1)
computer.displayInfo()
