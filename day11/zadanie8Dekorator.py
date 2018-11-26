def bold(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return "<b>"+wynik+"</b>"
    return wrapper

@bold
def nasza_funkcja():
    return "jakis napis"

print(nasza_funkcja())