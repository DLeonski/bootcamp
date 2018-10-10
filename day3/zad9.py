import datetime;
year = datetime.datetime.now().year
w = int(input("Podaj swój rok urodzenia: "))
if year-w >= 18:
    print("Jesteś pełnoletni/a!")
else:
    print("Jesteś niepełnoletni/a!")

