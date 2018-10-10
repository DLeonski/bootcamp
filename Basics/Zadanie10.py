a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = input("Podaj rodzaj operacji: ")
t = 0
if c == "+":
    w = a + b
elif c == "-":
    w = a - b
elif c == "*":
    w = a * b
elif c == "/":
    if b != 0:
        w = a / b
    if b == 0:
        t = 1
if t == 1:
    d = ("Nie można tego obliczyć.")
elif t == 0:
    d =(f"Wynik to {w}.")
print(d)