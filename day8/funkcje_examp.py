# # def hellow():
# #     print("Hellow Wolrd!")
# #
# #
# # hellow()
# #
# #
# # def hello2(name):
# #     print(f"Hellow {name}")
# #
# #
# # hello2("Leonski!")
# #
# #
# # def hello3(name="World!"):
# #     print(f"Hellow {name}")
# #
# #
# # hello3()
# # x = print("Co tam sporotwe swiry")
# # print("x:", x)
# # y = dir()
# # print("y:", y)
# # z = hellow()
# # print(z)
# #
# #
# def dodaj(a, b):
#     return a + b
#
#
# # wynik = dodaj(10, 11)
# # wynik2 = dodaj(1.1, 20.2)
# # wynik3 = dodaj("a", "b")
# # print(wynik, wynik2, wynik3)
# def test_dodaj_dwie_liczby():
#     assert dodaj(1, 2) == 3
# def test_dodaj_dwa_napisy():
#     assert dodaj("1", "2") == "12"

def klon (imie, wiek=18, wzrost=181):
    print(f"Witaj {imie}")
    if wiek == 18 and wzrost ==181:
        print(f"Jestes masny.")
    else:
        print("Jestes zly.")
klon("Adam")