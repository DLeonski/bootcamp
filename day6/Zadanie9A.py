koszyk = {}
magazyn = {"poziomki": 5, "ziemniaki":10, "kapusta": 4}
kilo = {"poziomki": 10, "ziemniaki": 3, "kapusta": 5}
print("W naszym sklepie oferujemy: ")
for prd in kilo:
    print(f"- {prd} -w cenie: {kilo[prd]}  pln  ")
print()
wybor = ()
while True:
    komenda = input("""Wybierz opcję:"
    [d]- dodaj do magazynu
    [k]- kup produkty
    [z]- zakończ
    """)
    if komenda == "k":
        wybor = input("Który produkt chciałbyś kupić?: ")
        wybor = wybor.lower()
        if wybor in kilo:
            ile = float(input(f"Ile chcesz kupic {wybor}: "))
            if ile <= magazyn[wybor]:
                koszyk[wybor] = ile
                magazyn[wybor] -= ile
                decyzja = input("Czy coś jeszcze?[tak/nie]: ")
                decyzja = decyzja.lower()
                print()
                if decyzja != "tak":
                    break
            else:
                print()
                print(f"Niestety nie mam tyle produktu. Pozostało: {magazyn[wybor]}")
        else:
            print("Niestety nie mamy takiego produktu.")
        print()
        print()
    elif komenda == "d":
        co = input("Jaki produkt chcesz dodać?: ")
        ile = int(input(f"Ile {co} chcesz dodać?: "))
        magazyn[co] = magazyn.get(co, 0) + ile
        if co not in kilo:
            cena = float(input(f"Jaka cena za {co}?:"))
            kilo[co] = cena
    elif komenda == "z":
        break
sumarycznie = 0
print("        PARAGON:")
for produkty in koszyk:
    sumarycznie = sumarycznie + koszyk[produkty] * kilo[produkty]
    print(f"{produkty} w ilości {koszyk[produkty]}kg")
print("="*30)
print(f"Koszt to {sumarycznie} PLN.")