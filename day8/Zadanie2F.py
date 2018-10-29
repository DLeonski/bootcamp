def wiecej_niz(napis, prog):
    wynik = set()
    for litera in napis:
        if napis.count(litera) > prog:
            wynik.add(litera)
# x = wiecej_niz("", 0)
# print(x)
def test_czy_litera_wystepuje_3_razy():
    assert wiecej_niz("", 0) == set()

def test_wiecej_niz_dla_niepustego_testu():
    assert wiecej_niz("aaa bb mc", 2) == {'a'}
    assert wiecej_niz("aaa bb mc", 3) == set()