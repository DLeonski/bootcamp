lista = [1,2,3, 4]

try:
    print(lista[4])
    list.add(5)
except IndexError as e:
    raise IndexError("Próbujesz pobrać element spoza zakresu listy.")
except AttributeError as e:
    print("Próbujesz wywołać metodę której ten obiekt nie ma.")


print("po wyjątkach")