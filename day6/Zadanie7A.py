napis = input("Podaj napis: ")
napis = napis.lower()
x = 0
SAMOGLOSKI = ["a", "e", "i", "o", "u", "y"]
for litera in napis:
    if litera in SAMOGLOSKI:
        x += 1
print(f'W napisie wystąpiło {x} samogłosek: ')
