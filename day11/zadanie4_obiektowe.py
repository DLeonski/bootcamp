from zadanie1_obiektowe import Product


class Basket():
    def __init__(self, x):
        self.x = x
        self.x = list()

    def add_product(self, product, qty):
        self.qty = qty
        self.x.add(product, qty)

    def count_total_price(self):
        self.qty * self.x()

    def generate_report(self):
        pass
