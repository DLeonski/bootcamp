lista = [-2, -4, 1, 2, 3, -3, -9]
dod = 0
uj = 0
for x in lista:
    if x > 0:
        dod += 1
    elif x < 0:
        uj += 1
print(f"Tyle dodatnich: {dod}")
print(f"Tyle ujemnych: {uj}")
