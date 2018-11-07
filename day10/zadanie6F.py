lista = [1, 2, 3, [4, 5, [6]], 7]


def splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element, list):
            out.extend(splaszcz(element))
        else:
            out.append(element)
    return out


# assert isinstance(lista[0], int)  # 1
# assert isinstance(lista[3], list)  # [4,5,[6]]
def test_splaszcz_niezagniezdzona_lista():
    lista = [1, 2, 3, 4, 5, 6, 7]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7]


def test_splaszcz_zagniezdzona_lista():
    lista = [1, 2, 3, [4, 5, [6]], 7]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7]

def test_splasz_jednozagniezdzona_lista():
    lista = [1,2,3,[4,5],6 ,7]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7]