import tkinter


def obliczanie():
    cena = float(dystans_entry.get())
    dystans = int(dystans_entry.get())
    spalanie = float(spalanie_entry.get())
    koszt = (dystans / 100) * spalanie * cena
    wynik.configure(text=f'{koszt} PLN')


root = tkinter.Tk()
root.columnconfigure(1, weight = 1)

dystans_label = tkinter.Label(master=root, text="Dystans")
dystans_label.grid(row=0, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="Spalanie")
spalanie_label.grid(row=1, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1)

cena_label = tkinter.Label(master=root, text="Cena paliwa")
cena_label.grid(row=2, column=0)
cena_entry = tkinter.Entry(master=root)
cena_entry.grid(row=2, column=1)

wynik_label = tkinter.Label(master=root, text = "Wynik")
wynik_label.grid(row=3, column=0)
wynik = tkinter.Label(master=root, text = " - ")
wynik.grid(row=3, column=1)

button_wynik = tkinter.Button(master=root,text = "Calculate!", command = obliczanie)
button_wynik.grid(row=4, column=0)


root.mainloop()








# entry = tkinter.Entry(master=root)
# entry.grid(row = 0, column = 1)
# label_cena = tkinter.Label(master = root, text = "Cena:")
# label_cena.grid(row = 0 , column= 0)
# label_spalanie = tkinter.Label(master = root, text = "Spalanie:")
# label_spalanie.grid(row = 1 , column= 0)
# entry_spalanie = tkinter.Entry(master=root)
# entry_spalanie.grid(row = 1, column = 1)

#

# button.grid(row = 2, column = 0)
# root.mainloop()
