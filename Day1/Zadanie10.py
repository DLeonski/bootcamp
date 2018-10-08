a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = input("Podaj rodzaj operacji: ")
if c == "+":
    w = a + b
elif c == "-":
    w = a - b
elif c == "*":
    w = a * b
elif c == "/" and b != 0:
    w = a / b
if c == "/" and b == 0:
    d = ("Nie można tego obliczyć.")
else:
    d =(f"Wynik to {w}.")
print(d)