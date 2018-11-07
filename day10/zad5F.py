def silnia(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba * silnia(liczba-1)



def test_silnia():
    assert silnia(5) == 120
def test_silnia_dla_0():
    assert silnia(0) == 1