from zadanie1_obiektowe import Product


class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity



class Basket():
    def __init__(self):
        self.entries = {}

    def add_product(self, product, qty):
        self.entries.append(BasketEntry(product, qty))

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()
        return total_price

    def generate_report(self):
        pass



pr1 = Product("Woda", 1, 5)
basket = Basket()
basket.add_product(pr1, 2)
