class Employee():
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.godzin = 0.0

    def register_time(self, godzin):
        if godzin >= 9:
            x = (godzin - 8)
            self.godzin = godzin + x
        else:
            self.godzin += godzin


    def pay_salary(self):
        return self.stawka * self.godzin
        self.godzin = 0


employee1 = Employee("Adam", "Małysz", 100.0)
employee1.register_time(5)
employee1.register_time(10)
print(employee1.pay_salary())
