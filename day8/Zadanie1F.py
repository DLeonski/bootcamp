def czy_pierwsza(a):
    for x in range(2, a):
        if a % x == 0:
            return False
    return True

def test_czy_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(11)
    assert czy_pierwsza(3)
    assert czy_pierwsza(101)


def test_czy_pierwsza_dla_liczby_niepierwszej():
    assert not czy_pierwsza(10)
    assert not czy_pierwsza(27)
    assert not czy_pierwsza(121)
