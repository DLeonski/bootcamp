print("Liczby podzielne przez 3 lub 5: ")
ile = 0
for x in range(0, 101):
    if x % 3 == 0 or x % 5 == 0:
        ile += 1
        print(x)
print(f"W przedziale od 0-100 jest {ile} liczb podzielnych przez 3 lub 5.")
