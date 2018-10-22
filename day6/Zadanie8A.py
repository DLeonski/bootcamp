napis = input("Podaj napis i oznacz wyraz do policzenia [<], [>]: ")
znaki = 0
licz = False
for i in napis:
    if i == "<":
        licz = True
    elif i == ">":
        break
    elif licz == True:
        znaki+=1
print(f"Oznaczony wyraz ma {znaki} znaków.")