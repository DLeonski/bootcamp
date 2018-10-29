podaj = ()
liczby = set()
parzyste = set(range(0,101,2))
while True:
    podaj = (input("Podaj liczby [stop]: "))
    if podaj == "stop":
        break
    liczby.add(podaj)
print(f"Unikalnych liczb: {len(liczby)}")
print(f"W tym parzystych: {len(liczby & parzyste)}")
