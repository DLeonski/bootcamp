s = ()
z=[]
ilość = 0
print("Możesz zakończyć wprowadzanie liczb pisząc STOP.")
while s != ("STOP"):
    x = input("Podaj liczbę: ")
    z.append(x)
    if x == ():
        print("Nie została podana żadna liczba.")
    else:
        ilość+1
print (z)