licznik = {}
napis = input("Podaj napis: ")
napis = napis.lower()
for znak in napis:
    licznik[znak] = licznik.get(znak, 0)+1
print(licznik)