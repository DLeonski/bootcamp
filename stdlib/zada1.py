import json
import sys
try:
    with open("pracownicy.json", "r") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []




praca = {}
decyzja = input("Co chcesz zrobic? [d - dodaj, w - wypisz]: ")
if decyzja == "d":
    name = input("Imie: ")
    sname = input("Nazwisko: ")
    age = int(input("Wiek:" ))
    kasa = float(input("Pensja: "))
    pracownicy.append(
        {"Imie" : name,
                    "Nazwisko" : sname,
                        "Wiek:" : age,
                        "Pensja:" : kasa})
    with open("pracownicy.json", "w") as plik:
        json.dump(pracownicy, plik)
elif decyzja == "w":
    for nr, p in enumerate(pracownicy, 1):
        print(f"{(nr)} {p(imie)} {p(nazwisko)} - wiek: {p(age)}, pensja: {p(pensja)} PLN" )



#
# obiekt = {"Imie": "Jan", "wiek":33}
#
# print(json.dumps(obiekt))
#
# napis = '{"Imie": "Jan", "wiek":33}'
#
# print(json.loads(napis))