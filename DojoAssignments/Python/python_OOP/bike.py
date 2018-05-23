class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = 0
        self.miles = miles
    def displayInfo(self):
        print "price: " + str(self.price)
        print "max speed: " + str(self.max_speed)
        print "total miles: " + str(self.miles)
    def ride(self):
        print "Riding"
        self.miles += 10
    def reverse(self):
        print "Reversing"
        self.miles -= 5

bike1 = Bike(200, 30, 2)
bike1.displayInfo()
bike1.ride()
bike1.ride()
bike1.displayInfo()
