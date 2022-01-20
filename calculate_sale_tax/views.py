from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
from .utils.items import Item
from .utils.tax import Tax

# Create your views here.
def add_items(request):
    if request.method == "POST":
        count = 0
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
                count = count + 1
            elif key.find("price") != -1:
                price = value
                ## Adding Item objects to items list
                count = count + 1
                # if count % 3 == 0:
                items.append(Item(int(qty), item_desc, float(price)))
        for item in items:
            total_tax = total_tax + item.item_tax
            total_price = total_price + item.item_total
        for folder in settings.STATICFILES_DIRS:
            javascript_files = os.listdir(folder + "/js")
        all_plugins = []
        for js_file in filter(
            lambda x: x.startswith("plug-") and x.endswith(".js"), javascript_files
        ):
            name_of_plug = js_file.replace("plug-", "")
            name_of_plug = name_of_plug.replace(".js", "")
            all_plugins.append(name_of_plug)
        javascript_files_path = []
        for js_file in javascript_files:
            javascript_files_path.append(
                os.path.join(os.path.join("/static", "js"), js_file)
            )
        print(javascript_files_path)
        return render(
            request,
            "result-test.html",
            {
                "context": items,
                "total_tax": round(round(total_tax / 0.05) * 0.05, 2),
                "total_price": total_price,
                "plugins": all_plugins,
                "paths": javascript_files_path,
            },
        )
    return render(request, "index.html")
