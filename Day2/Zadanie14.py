s = ()
z=[]
ilosc = -1
print("Możesz zakończyć wprowadzanie liczb pisząc STOP.")
while s != ("STOP"):
    s = input("Podaj liczbę: ")
    z.append(s)
    ilosc = ilosc + 1
    if s == ():
        print("Nie została podana żadna liczba.")
    else:
        ilosc+int(1)
    if s == ("STOP"):
        break
print(ilosc)
del z[ilosc]
print (z)