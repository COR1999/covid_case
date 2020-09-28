from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from decimal import Decimal
from django.contrib import messages
from products.models import Product
# from .forms import OrderForm
from django.views.decorators.cache import never_cache
@never_cache
def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    q_set_products = []
    all_products = Product.objects.all()
    print("view_bag")
    grand_total = request.session.get("grand_total", {})
    final_price = 0
    list_of_products = []
    for item, key in bag.items():
        bag_products = all_products.filter(pk=int(item))
        for product in bag_products:
            bag_quantity = key
            total_price = float(product.price) * bag_quantity
            bag_set = {
                "id": product.id,
                "name": product.product_name,
                "color": product.color,
                "price": product.price,
                "image": product.image,
                "image_2": product.image_2,
                "quantity": bag_quantity,
                "item_total_price": total_price
            }
            list_of_products.append(bag_set)
            final_price += total_price
    print(grand_total)
    grand_total = final_price

    context = {
        "products": list_of_products,
        "grand_total": grand_total,
        # "form": form,
    }
    return render(request, 'shopping_bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    # print(item_id)
    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    # product = get_object_or_404(Product, pk=item_id)
    quantity = request.POST.get('quantity', 0)
    grand_total = request.session.get("grand_total", 0)
    bag = request.session.get('bag', {})
    price = product.price
    if int(quantity) <= product.number_in_stock:
        if len(quantity) > 0:
            print(type(quantity))
            print(quantity)
            quantity = int(quantity)
            grand_total += float(price) * quantity
            if item_id in list(bag.keys()):
                bag[item_id] += quantity
            else:
                bag[item_id] = quantity
        request.session['grand_total'] = grand_total
        request.session['bag'] = bag
    else:
        messages.info(request, "Sorry not enough in stock")


    context = {
        "all_products": product,
        "grand_total": grand_total,

    }
    return redirect(redirect_url, context)




def adjust_bag(request, item_id, updated_value):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    # quantity = int(request.session.get('quantity'))
    # request.session["bag"]["quantity"] = updated_value
    bag = request.session.get('bag', {})
    grand_total = request.session.get("grand_total", 0)
    print(int(updated_value))
    # bag[item_id] == int(updated_value)
    bag[item_id] = int(updated_value)
    print("bag", bag)
    
    request.session["bag"] = bag
    # quantity = quantity + int(delta)
    # print(product.number_in_stock)

    return redirect(reverse("view_bag"))


