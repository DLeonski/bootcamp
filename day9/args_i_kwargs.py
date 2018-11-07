# def foo(pierwszy, *reszta):
#     # print ('pierwszy', pierwszy )
#     # print ('reszta', reszta)
#     if reszta:
#         return pierwszy + reszta[-1]
#     return pierwszy
#
#
# # foo(1)
#
# foo(1, 2)
# print(foo(1))
# print(foo(1, 2, 4, 5, 6, 7, 10))
# reszta = [1, 2, 5, 6, 7, 8, 10]
# print(*reszta)
#
#
# def druga_funkcja(**slownik):
#     if 'd' in slownik:
#         return slownik['a'] + slownik['d']
#     if slownik:
#         return slownik['a']
#     return "żaden warunek nie był spełniony"
#
#
# print(druga_funkcja(a=2, b=2, c=3, d=4))
# print('a i d', druga_funkcja(a=2, b=2, c=3, d=4))
# print('a i d drugi raz', druga_funkcja(a=2, b=2, c=3, d=14, zosia=5, adas=15))
# print('a drugi raz ale bez d', druga_funkcja(a=2, b=2, c=3, d=14, zosia=5, adas=15))

# co_na_co = {
#     "Ala": "Kot",
#     "kota": "Alę"
# }
#
#
# def zamien(jakis_tekst, **co_na_co):
#     for klucz in co_na_co:
#         jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
#
#     return jakis_tekst
#
#
# print(zamien("Ala ma kota", **co_na_co))
# print(zamien("Ala ma kota", Ala="Kot", kota="Alę"))

zamiana  = {
    "$produkt": "Samochod",
    "$cena": "20000"
}
napis = "Ten $produkt kosztuje $cena"
napis2 = "Zajęcia z $przedmiot zostały odwołane"
def formatuj(napis, **zamiana):
    for klucz in zamiana:
        napis = napis.replace("$" + klucz, zamiana[klucz])
    print(napis)
    return napis
assert formatuj(napis, produkt="Samochod", cena="20000") == "Ten Samochod kosztuje 20000"