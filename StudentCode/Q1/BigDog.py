from Dog import Dog

class BigDog(Dog):
    def __init__(self, name, weight, days, age):
        super().__init__(name, weight, days)
        self.unit = 3
        self.age = age
    

    def isSenior(self):
        if int(self.age) > 9:
            return True
        else:
            return False

    def getCost(self):
        if self.isSenior():
            return round(float(self.weight)/10 * 19.99 * (int(self.days)/7) * 15 * 1.15, 2)
        else:
            return round(float(self.weight)/10 * 24.99 * (int(self.days)/7) * 12.5 * 1.15, 2)

    


