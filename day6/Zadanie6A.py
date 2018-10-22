liczby = [5, 2, 1, 4, 3]
min_ = liczby[0]
max_ = liczby[0]
for liczba in liczby:
    if liczba < min_:
        min_ = liczba
    if liczba > max_:
        max_ = liczba
liczby[liczby.index(min_)], liczby[liczby.index(max_)] = max_, min_
