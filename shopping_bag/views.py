from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    q_set_products = []
    all_products = Product.objects.all()
    print(bag)
    list_of_products = []
    for item, key in bag.items():
        # print(item)
        bag_products = all_products.filter(pk=int(item))
        # print(bag_products)
        # q_set_products.append(bag_products)
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
    # print(list(list_of_products))

    # print("list q set", list(q_set_products))
    # for product in q_set_products:
    #     # print(id)
    #     product_id_list = list(product.values("pk"))
    #     product_id = product_id_list[0]["pk"]
    #     bag_quantity = bag.pop(str(product_id))

    #     # print(bag_quantity)

    #     # bag_value = bag.pop(id)
    #     bag_set = {
    #         "name": product.values("product_name"),
    #         "color": product.values("color"),
    #         "price": product.values("price"),
    #         "image": product.values("image"),
    #         "image_2": product.values("image_2"),
    #         "quantity": bag_quantity
    #     }
    #     list_of_prodcts.append(bag_set)
    print(list_of_products)
    context = {
        "products": list_of_products,
    }
    return render(request, 'shopping_bag/bag.html', context)


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
