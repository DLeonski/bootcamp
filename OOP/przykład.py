class Osoba():
    def __init__(self, imie, nazwisko):
        print("No elo")
        self.imie = imie
        self.nazwisko = nazwisko



    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    @staticmethod
    def metoda_statyczna():
        print("Metoda statyczna")

obiekt = Osoba("Adam", "Małysz")
obiekt2 = Osoba("Adam", "Mickiewicz")

print(obiekt.imie)
print(obiekt2.nazwisko)

obiekt.przedstaw_sie()
Osoba.metoda_statyczna()