from random import randint

krok = 0
x = randint(1, 10)
y = randint(1, 10)
skarbX = randint(1, 10)
skarbY = randint(1, 10)
minKrokow = (abs(skarbX - x) + abs(skarbY - y))
while x < 10 or y < 10 or x < 1 or y < 1:
    minKrokprzed = (abs(skarbX - x) + abs(skarbY - y))
    krok += 1
    print(f"Znajdujesz się na pozycji {x},{y}")
    kierunek = input("W którą stronę idziesz? [W],[A],[S],[D]: ")
    if kierunek == 'w':
        y += 1
    elif kierunek == 's':
        y -= 1
    elif kierunek == 'a':
        x -= 1
    elif kierunek == 'd':
        x += 1
    minKrokpo = (abs(skarbX - x) + abs(skarbY - y))
    wskazowka = randint(1, 5)
    if wskazowka != 2:

        if minKrokpo < minKrokprzed:
            print("Zbliżasz się.")
        else:
            print("Oddalasz się. ")
    if x > 10 or y > 10 or y < 1 or x < 1:
        print("Koniec gry, przegrana.")
        break
    if x == skarbX and y == skarbY:
        print("Wygrana.")
        break
    if 2 * minKrokow == krok:
        skarbX = randint(1, 10)
        skarbY = randint(1, 10)
        print()
        print("Skarb znajduje się w nowym miejscu.")
        print()
