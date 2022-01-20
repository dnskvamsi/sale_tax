from .tax import Tax


class Item:
    def __init__(self, qty, item_desc, price):
        self.qty = qty
        self.item_desc = item_desc
        self.price = price
        self.item_price = self.qty * self.price
        self.tax = Tax(self.item_desc, self.item_price)
        self.item_tax = self.tax.calculate()
        self.item_total = self.item_tax + self.item_price
