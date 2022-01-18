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
                item = "item" + str(item_no)
                context[item] = {}
                item_quantity = int(request.POST["item" + str(item_no)])
                context["item" + str(item_no)]["item_quantity"] = item_quantity
                item_desc = request.POST["item" + str(item_no) + "-descr"]
                context["item" + str(item_no)]["item_descr"] = item_desc
                item_price = float(request.POST["price" + str(item_no)])
                context["item" + str(item_no)]["price"] = item_price
                imported = check_imported(item_desc)
                # print("total-tax-before:", total_tax)
                if check_book(item_desc):
                    context["item" + str(item_no)]["tax"] = calculate_tax(
                        item_quantity * item_price, imported, "book"
                    )
                    # print("inside-book", total_tax)
                    total_tax = total_tax + calculate_tax(
                        item_quantity * item_price, imported, "book"
                    )
                    # print("inside-book", total_tax)

                elif check_food(item_desc):
                    context["item" + str(item_no)]["tax"] = calculate_tax(
                        item_quantity * item_price, imported, "food"
                    )
                    total_tax = total_tax + calculate_tax(
                        item_quantity * item_price, imported, "food"
                    )
                elif check_medical(item_desc):
                    context["item" + str(item_no)]["tax"] = calculate_tax(
                        item_quantity * item_price, imported, "medical"
                    )
                    total_tax = total_tax + calculate_tax(
                        item_quantity * item_price, imported, "medical"
                    )
                else:
                    context["item" + str(item_no)]["tax"] = calculate_tax(
                        item_quantity * item_price, imported, "others"
                    )
                    total_tax = total_tax + calculate_tax(
                        item_quantity * item_price, imported, "others"
                    )
                print("total-tax", total_tax)
                total_price = total_price + item_quantity * item_price
                print("total-price", total_price)
        print(total_tax)
        print(total_price)
        print(total_price + total_tax)
        print(context)
        return render(
            request,
            "result.html",
            {
                "context": context,
                "total_tax": round(round(total_tax / 0.05) * 0.05, 2),
                "total_price": round(round(total_tax / 0.05) * 0.05, 2) + total_price,
                # "total_price": round(round((total_price + total_tax) / 0.05) * 0.05, 2),
            },
        )
    return render(request, "index.html")


def check_imported(value):
    print(value)
    if value.lower().find("imported") != -1:
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
    return round(round(tax / 0.05) * 0.05, 2)
