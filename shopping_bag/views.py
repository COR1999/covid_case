from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    list_of_ids = []
    # print("bag", bag)
    products = Product.objects.all()
    print("id", bag.keys())
    for item in bag.keys():
        print(item)
        list_of_ids.append(item)
    print(list_of_ids)

    products = Product.objects.all()
    bag_products = products.filter(pk=item)
    context = {
        "products": bag_products,
    }
    return render(request, 'shopping_bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # size = None
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    print(bag)
    print(quantity)
    context = {
        "all_products": product,
    }
    # print(product)
    return redirect(redirect_url)
