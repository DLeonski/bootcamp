class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Employee(Osoba):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko)
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


class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, kwota):
        self.bonus += kwota


employee1 = Employee("Adam", "Małysz", 100.0)
employee1.register_time(5)
employee1.register_time(10)
print(employee1.pay_salary())
