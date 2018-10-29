podaj = ()
liczby = set()
parzyste = set(range(0,100,2))
while podaj != "stop":
    podaj = (input("Podaj liczby [stop]: "))
    podaj = int(podaj)
    liczby.add(podaj)
zgodnosc=0
for i in liczby:
    if i in liczby:
        zgodnosc+=1
print(zgodnosc)