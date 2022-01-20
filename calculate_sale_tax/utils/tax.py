class Tax:
    food_items = ["chocolate", "waffles", "cakes", "chips", "soft drink"]
    medical_items = ["tablets", "capsules", "syrup"]
    book_items = ["book"]
    exempted_items = food_items + medical_items + book_items

    def __init__(self, item_desc, price):
        self.item_desc = item_desc
        self.price = price

    def check_imported(self):
        if self.item_desc.lower().find("imported") != -1:
            return True
        else:
            return False

    def check_for_exempted(self, items):
        for item in items:
            if self.item_desc.lower().find(item) != -1:
                return True
        return False

    def calculate(self):
        tax = 0
        if self.check_imported():
            tax = tax + self.price * 0.05
        if not (self.check_for_exempted(self.exempted_items)):
            tax = tax + self.price * 0.1

        return round(round(tax / 0.05) * 0.05, 2)
