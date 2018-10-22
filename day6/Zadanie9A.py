kilo = dict()
kilo = {"poziomki": 10, "ziemniaki": 3, "kapusta": 5}
print("W naszym sklepie oferujemy: ")
for prd in kilo:
    print(f"- {prd} -w cenie: {kilo[prd]}  pln  ")
print()
wybor=input("Który produkt chciałbyś kupić?: ")
ile = float(input(f"Ile chcesz kupic {wybor}: "))
suma = kilo[wybor]*ile
print(f"Koszt to {suma} PLN.")
