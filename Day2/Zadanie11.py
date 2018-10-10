x = int(input("Podaj pozycje x: "))
y = int(input("Podaj pozycje y: "))
if (y > 100 or x > 100) or (y < 0 or x < 0):
    z = "poza planszą."
else:
    if x <= 10 and y <= 10:
        z = "w lewym dolnym rogu."
    elif x<=10 and y > 10 and y <= 90:
        z = "na lewej krawędzi."
    elif x > 10 and x <= 90 and y <= 10:
        z = "na dolnej krawędzi planszy."
    elif y > 90 and y <= 100 and x > 10 and x <= 90:
        z = "na górnej krawędzi."
    elif y > 90 and y <= 100 and x <= 10:
        z = "w lewym górnym rogu."
    elif y > 90 and y < 100 and x > 90 and x <= 100 :
        z = "w prawym górnym rogu."
    elif y > 10 and y <= 90 and x <= 100 and x > 90:
        z = "na prawej krawędzi planszy."
    elif y <= 10 and x <= 100 and x > 90:
        z = "w prawym dolnym rogu."
    elif y > 10 and y <= 90 and x <= 90 and x > 10:
        z = "w centrum planszy."
d = print(f"Gracz znajduje się {z}")