class ElectricCar():
    def __init__(self, cap):
        self.cap = cap
        self.km = self.cap
    def drive(self, droga):
        wynik = self.cap - droga
        if wynik < 0:
            wynik = self.cap
            self.cap = 0
            return wynik
        else:
            self.cap -= droga
            return droga
    def charge(self):
        self.km = self.cap



car = ElectricCar(100)
print(car.drive(70))
print(car.drive(70))
car.charge()
print(car.cap)
