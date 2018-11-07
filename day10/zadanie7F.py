lista = [1, 2, 3, 4, 5, 6, 7]


# warunek ze wieksze niz 3

out = [False, False, False, True, True, True]

def bigger_than_3(liczba):
    if liczba > 3:
        return True
    else:
        return False


def smaller_than_3(liczba):
    if liczba < 3:
        return True
    return False


def sprawdzam_czy_wieksze_niz_3(lista):
    out = []
    for element in lista:
        out.append(bigger_than_3(element))
    return out


def sprawdzam_czy(lista, warunek):
    out=[]
    for element in lista:
       out.append(warunek(element))
    return out

def x(i):
    if i == 4:
        return True
    return False

lambda x: x > 3 <= 6

assert sprawdzam_czy_wieksze_niz_3(lista) == out
assert sprawdzam_czy(lista, bigger_than_3) == out
