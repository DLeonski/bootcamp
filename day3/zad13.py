dzien = 1
suma = 0
while dzien < 8:
    t = (int(input(f"Podaj temperaturę dnia {dzien}: ")))
    dzien = dzien + 1
    suma = suma + t
sr = suma / 7
print(f"Średnia temperatura w tym tygodniu wynosiła = {sr}")