from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_items(request):
    if request.method == "POST":
        context = {}
        total_tax = 0
        total_price = 0
        for item_no in range(1, 5):
            if request.POST["item" + str(item_no)] != "":
                print(request.POST["item" + str(item_no)])
                context["item" + str(item_no)] = {}
                item_quantity = int(request.POST["item" + str(item_no)])
                context["item" + str(item_no)]["item" + str(item_no)] = item_quantity
                item_desc = request.POST["item" + str(item_no) + "-descr"]
                context["item" + str(item_no)][
                    "item" + str(item_no) + "-descr"
                ] = item_desc
                item_price = float(request.POST["price" + str(item_no)])
                context["item" + str(item_no)]["price" + str(item_no)] = item_price
                imported = check_imported(item_desc)
                if check_book(item_desc):
                    total_tax = total_tax + calculate_tax(
                        item_quantity * item_price, imported, "book"
                    )
                elif check_food(item_desc):
                    total_tax = total_tax + calculate_tax(
                        item_quantity * item_price, imported, "food"
                    )
                elif check_medical(item_desc):
                    total_tax = total_tax + calculate_tax(
                        item_quantity * item_price, imported, "medical"
                    )
                else:
                    total_tax = total_tax + calculate_tax(
                        item_quantity * item_price, imported, "others"
                    )
                total_price = total_price + item_price
        print(total_price + total_tax)
        print(total_tax)
        print(total_price)
        context["total_price"] = total_price
        context["total_tax"] = total_tax
        print(context)
        return render(request, "result.html", context)
    return render(request, "index.html")


def check_imported(value):
    if value.lower().find("imported"):
        return True
    else:
        return False


def check_food(value):
    food_items = ["chocolate", "waffles", "cakes", "chips", "soft drink"]
    for item in food_items:
        if value.lower().find(item) != -1:
            return True
    return False


def check_medical(value):
    medical_items = ["tablets", "capsules", "syrup"]
    for item in medical_items:
        if value.lower().find(item) != -1:
            return True
    return False


def check_book(value):
    book_items = ["book"]
    for item in book_items:
        if value.lower().find(item) != -1:
            return True
    return False


def calculate_tax(price, imported_or_not, category):
    tax = 0
    if imported_or_not:
        tax = tax + price * 0.05
    if category == "others":
        tax = tax + price * 0.1
    return tax
