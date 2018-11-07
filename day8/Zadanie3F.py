def policz_znaki(napis, start="<", end=">"):
    licznik = 0
    stopien = 0
    licz = False
    for znak in napis:
        if znak == start and licz == False:
            licz = True
        elif znak == start and licz == True:
            stopien += 1
        elif licz == True:
            licznik += 1
            if stopien >= 1:
                licznik +(1+stopien)
        elif znak == end:
            if znak == end and stopien >= 1:
                stopien -= 1
            elif znak == end and stopien == 0:
                break

    return licznik
    pass

def test_policz_znaki_bez_znacznikow():
    assert policz_znaki('ala ma kota a kot ma ale') == 0


def test_policz_znaki_jeden_poziom_zaglebienie_standardowe_znaczniki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4


def test_policz_znaki_wiele_pozioow_zaglebienia_niestandardowe_znaczniki():
    assert policz_znaki('ala ma [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('ala ma [kota [a kot]] ma [ale]', start='[', end=']') == 18


def test_policz_znaki_standardowe_znaczniki_wiele_poziomow():
    assert policz_znaki('a <a<a<a>>>') == 6
