miastoA = input("Miasto startowe: ")
miastoB = input("Miasto końcowe: ")
dystans = int(input(f"Podaj odległość między {miastoA}-{miastoB}: "))
cena = float(input("Podaj cenę paliwa: "))
spalanie = float(input("Podaj średnie spalanie na 100km: "))
koszt = float(dystans/100 * spalanie * cena)
print()
koszt = round(koszt, 2)
print(f"Koszt porzejazdu {miastoA}-{miastoB} to {koszt}zł.")