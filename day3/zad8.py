a = int(input("Podaj szerokość opakowania[cm]: "))
b = int(input("Podaj długość opakowania[cm]: "))
h = int(input("Podaj wysokość opakowania[cm]: "))
v = a * b * h
if v >= 1000:
    print("Opakowanie ma conajmniej jeden litr.")
else:
    print("Opakowanie ma mniej niż jeden litr.")