from django.http import request
from shopping_bag.forms import OrderForm
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
# from decimal import Decimal, Rounded
from django.contrib import messages
from products.models import Product
from .forms import OrderForm
from .models import OrderItem, Order
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.views.decorators.http import require_http_methods
import stripe


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
    request.session["grand_total"] = final_price

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
    quantity = request.POST.get('quantity')
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
        # "grand_total": grand_total,

    }
    return redirect(redirect_url, context)




def adjust_bag(request, item_id, updated_value, delta):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)

    bag = request.session.get('bag', {})
    print(bag[item_id])
    print(product.number_in_stock)
    if int(bag[item_id]) == product.number_in_stock:
        if delta == "minus":
            bag[item_id] = int(updated_value) - 1
            request.session["bag"] = bag
    if delta == "minus":
        if int(updated_value) > 0:
            if int(updated_value) <= product.number_in_stock:
                bag[item_id] = int(updated_value) - 1
                request.session["bag"] = bag
            else:
                messages.info(request, "Sorry not enough in stock")
        else:
            messages.info(request, "Sorry your item quantity cant be less then 0")
    if delta == "add":
        if int(updated_value) >= 0:
            if int(updated_value) < product.number_in_stock:
                bag[item_id] = int(updated_value) + 1
                request.session["bag"] = bag

    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    bag = request.session.get('bag', {})
    print(bag)
    del request.session["bag"][item_id]
    request.session.modified = True
    return redirect((reverse("view_bag")))

def checkout(request):
    form = OrderForm()
    try:
        STRIPE_PUBLIC_KEY = "pk_test_51HH4jLDjlHsBcv8nsTDlvMs1Zkdk3enUg23OOVaAJ8kliIhK4zV86NrNnNimffXD9gOrtquyNtz5DcwhxdPGBKps00vJv0uBcg"
        STRIPE_SECRET_KEY = "sk_test_51HH4jLDjlHsBcv8n5xQRVA2Q4SLIT4c9gCUj25yNOmxHXsmCyexC56X8SfP3imAcG24BVWrI60JuBWUVgJUC360u00UQeRhPoz"
        stripe.api_key = STRIPE_SECRET_KEY
        grand_total = request.session.get("grand_total", 0)
        intent = stripe.PaymentIntent.create(
            amount=round(grand_total * 100),
            currency=settings.STRIPE_CURRENCY,
        )

        context = {
        "form": form,
        "STRIPE_PUBLIC_KEY": str(STRIPE_PUBLIC_KEY),
        "client_secret": intent.client_secret,
        }
    except Exception as e:
        print(str(e))

    #return 1
    return render(request, 'shopping_bag/checkout.html', context)

@require_http_methods(["POST"])
def checkout_process(request):
    form = OrderForm()
    post_details = request.POST.get('form').split("&")
    post_data = {}
    print(request.POST)
    print(post_details)
    print(request.user)

    for _post_details in post_details:
        _post_details = _post_details.split("=")
        post_data[_post_details[0]] = _post_details[1]

    print(post_data)

    pid = request.POST.get('client_secret').split('_secret')[0]

    STRIPE_PUBLIC_KEY = "pk_test_51HH4jLDjlHsBcv8nsTDlvMs1Zkdk3enUg23OOVaAJ8kliIhK4zV86NrNnNimffXD9gOrtquyNtz5DcwhxdPGBKps00vJv0uBcg"
    STRIPE_SECRET_KEY = "sk_test_51HH4jLDjlHsBcv8n5xQRVA2Q4SLIT4c9gCUj25yNOmxHXsmCyexC56X8SfP3imAcG24BVWrI60JuBWUVgJUC360u00UQeRhPoz"
    grand_total = request.session.get("grand_total", 0)
    grand_total = round(grand_total * 100)
    stripe.api_key = STRIPE_SECRET_KEY


    try:
        firstname = post_data['firstname']
        lastname = post_data['lastname']
        user_email = post_data['user_email']
        address_1 = post_data['address_1']
        address_2 = post_data['address_2']
        city = post_data['city']
        country= post_data['country']
        token = request.POST.get('token')

        # check_customer = Order.objects.get(email=user_email)
        # print(check_customer.user_email)
        # if len(check_customer < 1):
        stripe_customer = stripe.Customer.create(
            card=token,
            description=user_email
        )
        # else:
        # check_customer.stripe_pid

        intent = stripe.PaymentIntent.create(
            amount=round(grand_total * 100),
            currency=settings.STRIPE_CURRENCY,
            customer=stripe_customer.id
        )

        # stripe_charge = stripe.Charge.create(
        # amount=grand_total,
        # currency=settings.STRIPE_CURRENCY,
        # customer=stripe_customer.id
        # )

        # print(stripe_charge)

        ## saving to Order
        current_order = Order(stripe_pid=stripe_customer.id,firstname=firstname, lastname=lastname,
        email=user_email, address_1=address_1, address_2=address_2,
        country=country,city=city)
        current_order.save()
        
        print("stripe pid", stripe_customer.id)
        print("current order id",current_order.id)

        orders = request.session["bag"]

        for _orders in orders:
            # saving of product item
            current_order_item = OrderItem(item=Product.objects.get(id=_orders),
            order=Order.objects.get(id=current_order.id), quantity=orders[_orders])
            current_order_item.save()

            # updating of stock
            product_details = Product.objects.get(id=_orders)
            product_details.number_in_stock = product_details.number_in_stock - orders[_orders]
            product_details.save()


        del request.session['bag']
        messages.success(request, "Order Successful")

    except Exception as e:
        messages.error(request, "Error:" + str(e))
        print(str(e))   


    context = {
    "form": form,
    "STRIPE_PUBLIC_KEY": str(STRIPE_PUBLIC_KEY),
    "client_secret": intent.client_secret,
    }

    return render(request, 'shopping_bag/checkout.html', context)