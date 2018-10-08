x = int(input("Podaj pozycje x: "))
y = int(input("Podaj pozycje y: "))
if x <= 25 and y <= 25:
    z = "w lewym dolnym rogu."
elif x<=25 and y > 25 and y <= 75:
    z = "na lewej krawędzi."
elif x > 25 and x <= 75 and y <= 25:
    z = "na dolnej krawędzi planszy."
elif y > 75 and y <= 100 and x > 25 and x <= 75:
    z = "na górnej krawędzi."
elif y > 75 and y <= 100 and x <= 25:
    z = "w lewym górnym rogu."
elif y > 75 and y < 100 and x > 75 and x <= 100 :
    z = "w prawym górnym rogu."
elif y > 25 and y <= 75 and x <= 100 and x > 75:
    z = "na prawej krawędzi planszy."
elif y <= 25 and x <= 100 and x > 75:
    z = "w prawym dolnym rogu."
elif y > 25 and y <= 75 and x <= 75 and x > 25:
    z = "w centrum planszy."
elif (y > 100 and x > 100) or (y < 0 and x < 0):
    z = " poza planszą."

d = print(f"Gracz znajduje się {z}")