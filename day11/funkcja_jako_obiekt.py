def fun():
    print("cześć")


class Klasa:
    def __call__(self, *args, **kwargs):
        print("No elo")


fun()

x = Klasa()
x()

def silnia(x):
    wynik = 1
    for i in range(1, x + 1):
        wynik *= i
    return wynik

print(silnia(5))