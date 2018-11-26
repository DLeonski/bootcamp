from random import randint
from itemy import Item


class Postac:
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []


    def __str__(self):
        if self.stan_zdrowia():
            return f"Mam na imię {self.imie}, mam {self.atak} ataku i {self.zdrowie} HP."
        else:
            return f"{self.imie} nie zyje."

    def ojcowska_lepa(self):
        hitproc = randint(50, 1000)
        unik = randint(50, 80)
        if self.zdrowie <= 0:
            print("Koniec")
            print(self.zdrowie)
        else:
            if hitproc > unik:
                dmg = randint(5, 10)
                self.zdrowie = self.zdrowie - dmg * self.atak
                if self.stan_zdrowia():
                    print(f"{self.imie} dostał lepe! It's super effective!")
                    print(f"Zdrowie {self.imie}: {self.zdrowie}/{self.max_zdrowie}. ")
                else:
                    self.stan_zdrowia = 0
            else:
                print("Unik!")

    @property
    def atak(self):
        wynik = self._atak
        for i in self.ekwipunek:
            wynik += i.staty
        return wynik

    def stan_zdrowia(self):
        return self.zdrowie > 0

    def healek(self):
        if self.zdrowie > 0:
            ulecz = randint(1, 10)
            self.zdrowie = self.zdrowie + ulecz
            print(f"{self.imie} uzyl mocy leczacych! +{ulecz}HP")
        else:
            pass
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

    def daj_item(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def atak_plus(self):
        wynik = self.atak
        for i in self.ekwipunek:
            wynik += i.staty    
        return wynik

    @staticmethod
    def walka(atak, obrona):
        print(f"Walka: {atak.imie} vs {obrona.imie}")
        print()
        print(atak)
        print(obrona)
        obrona.ojcowska_lepa()
        atak.ojcowska_lepa()
        obrona.healek()
        atak.ojcowska_lepa()
        obrona.ojcowska_lepa()
        atak.ojcowska_lepa()
        obrona.ojcowska_lepa()


kastet = Item("kastet", 3)
terca = Postac("Tomasz", 7, 100)
janusz = Postac("Janusz", 5, 140)
janusz.daj_item(kastet)
print(f"bonus atk: {janusz.atak_plus()}")
Postac.walka(terca, janusz)
