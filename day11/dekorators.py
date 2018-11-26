def prosty_dekorator(func):
    def wrapper(*args, **kwargs):
        print("Przed wywołaniem")
        result = func(*args, **kwargs)
        print("Po wywołaniu")
        return result
    return wrapper


def dwa_wywolania(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper()

@dwa_wywolania
def fun():
    print("Cześć")


# fun = prosty_dekorator(fun)
@prosty_dekorator
def silnia(x):
    print("Uwaga nakurwiam salto!")
    wynik = 1
    for i in range(1, x + 1):
        wynik *= i
    return wynik

print(silnia(5))

print("Akuku")
fun()
