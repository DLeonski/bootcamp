lista = []
liczba_ele = 0
x = 0
while x != 'stop' or liczba_ele < 10:
    x = input("Podaj liczbę lub zakończ[stop]: ")
    if x == 'stop':
        del lista[liczba_ele]
        liczba_ele = liczba_ele - 1
        break
    else:
        lista.append(x)
        liczba_ele += 1
if len(lista) == 0:
    print("Nie podano żadnej liczby.")
else:
    print(liczba_ele)
    sr = sum(lista) / liczba_ele
    print(f"Średnia podanych liczb to: {sr}")
