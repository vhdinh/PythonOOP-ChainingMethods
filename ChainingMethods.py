class Bike(object):
    def __init__(self, price, max_speed,miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def riding(self):
        print "Riding"
        self.miles = self.miles + 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles < 5:
            return self
        else:
            self.miles = self.miles - 5
            return self

    def displayInfo(self):
        return self.price, self.max_speed, self.miles

bike1 = Bike("$100", "150mph")
bike2 = Bike("$150", "200mph")
bike3 = Bike("$200", "250mph")

print "\nbike1"
print bike1.riding().riding().riding().reverse().displayInfo()

print "\nbike2"
print bike2.riding().riding().reverse().reverse().displayInfo()

print "\nbike3"
print bike3.reverse().reverse().reverse().displayInfo()
