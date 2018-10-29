lista = [5, 4, 3, 1, 2]
print("Liczby przed: ", lista)
for indeks_podstawienia in range(len(lista)):
    indeks_min = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia+1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min]:
            indeks_min = indeks_ogona
    value_temp=lista[indeks_min]
    lista[indeks_min]=lista[indeks_podstawienia]
    lista[indeks_podstawienia] = value_temp
print("Liczby po: ", lista)
assert lista == [1, 2, 3, 4, 5]