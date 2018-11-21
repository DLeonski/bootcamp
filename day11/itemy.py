class Item():
    def __init__(self, nazwa, staty):
        self.nazwa = nazwa
        self.staty = staty
    def __str__(self):
        return f"self {nazwa}, +{self.staty} do ataku."