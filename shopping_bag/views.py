from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from decimal import Decimal
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    q_set_products = []
    all_products = Product.objects.all()

    grand_total = request.session.get("grand_total", {})

    list_of_products = []
    for item, key in bag.items():
        bag_products = all_products.filter(pk=int(item))
        for product in bag_products:
            bag_quantity = key
            bag_set = {
                "name": product.product_name,
                "color": product.color,
                "price": product.price,
                "image": product.image,
                "image_2": product.image_2,
                "quantity": bag_quantity,
                "item_total_price": product.price * bag_quantity
            }
            list_of_products.append(bag_set)
    print(list_of_products)
    context = {
        "products": list_of_products,
        "grand_total": grand_total,
    }
    return render(request, 'shopping_bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    print(item_id)
    product = Product.objects.get(pk=item_id)
    # product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    grand_total = request.session.get("grand_total", {})

    # size = None
    print(type(quantity))
    print(type(product.price))
    grand_total += float(product.price) * quantity
    print(grand_total)
    request.session['grand_total'] = grand_total
    print(request.session["grand_total"])
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    # print(quantity)
    context = {
        "all_products": product,
        "grand_total": grand_total,
    }
    # print(product)
    return redirect(redirect_url, context)
