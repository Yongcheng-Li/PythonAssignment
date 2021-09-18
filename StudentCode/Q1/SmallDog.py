from Dog import Dog

class SmallDog(Dog):
    def __init__(self, name, weight, days):
        super().__init__(name, weight, days)
        self.unit = 1
    
    def isSenior(self):
        return False

    def getU(self):
        return self.unit
    
    def getCost(self):
        return round(float(self.weight)/10 * 19.99 * (int(self.days)/7) * 10 * 1.15, 2)
