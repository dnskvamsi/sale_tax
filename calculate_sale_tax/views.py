from django.shortcuts import render
from django.http import HttpResponse


class Tax:
    def __init__(self, item_desc, price):
        self.value = item_desc
        self.price = price

    def check_imported(self):
        if self.value.lower().find("imported") != -1:
            return True
        else:
            return False

    def check_food(self):
        food_items = ["chocolate", "waffles", "cakes", "chips", "soft drink"]
        for item in food_items:
            if self.value.lower().find(item) != -1:
                return True
        return False

    def check_medical(self):
        medical_items = ["tablets", "capsules", "syrup"]
        for item in medical_items:
            if self.value.lower().find(item) != -1:
                return True
        return False

    def check_book(self):
        book_items = ["book"]
        for item in book_items:
            if self.value.lower().find(item) != -1:
                return True
        return False

    def calculate(self):
        tax = 0
        if self.check_imported():
            tax = tax + self.price * 0.05
        if not (self.check_book() or self.check_medical() or self.check_food()):
            tax = tax + self.price * 0.1
            return round(round(tax / 0.05) * 0.05, 2)
        else:
            return round(round(tax / 0.05) * 0.05, 2)


class Item:
    def __init__(self, qty, item_desc, price):
        self.qty = qty
        self.item_desc = item_desc
        self.price = price
        self.item_price = self.qty * self.price
        self.tax = Tax(self.item_desc, self.item_price)
        self.item_tax = self.tax.calculate()
        self.item_total = self.item_tax + self.item_price


# Create your views here.
def add_items(request):
    if request.method == "POST":
        count = 1
        items = []
        total_tax = 0
        total_price = 0
        for key, value in request.POST.items():
            if value == "":
                break
            if key.find("qty") != -1:
                qty = value
                count = count + 1
            elif key.find("desc") != -1:
                item_desc = value
            elif key.find("price") != -1:
                price = value
                print(qty, item_desc, price)
                ## Addeing Item objects to items list
                items.append(Item(int(qty), item_desc, float(price)))
        for item in items:
            total_tax = total_tax + item.item_tax
            total_price = total_price + item.item_total
        return render(
            request,
            "result-test.html",
            {
                "context": items,
                "total_tax": round(round(total_tax / 0.05) * 0.05, 2),
                "total_price": total_price,
            },
        )
    return render(request, "index.html")
