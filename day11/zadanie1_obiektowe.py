class Product():
    def __init__(self, produkt, id, cena):
        self.produkt = produkt
        self.id = id
        self.cena = cena

    def produkt_info(self):
        print(f"Produkt: {self.produkt}, id: {self.id}, cena: {self.cena} PLN")


produkt1 = Product("woda", 9, 10)
produkt2 = Product("piwo", 4, 2)
produkt1.produkt_info()
produkt2.produkt_info()
