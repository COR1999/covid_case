from django.http import request
from shopping_bag.forms import OrderForm
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from decimal import Decimal, Rounded
from django.contrib import messages
from products.models import Product
from .forms import OrderForm
from products.models import OrderItem, Order
from django.views.decorators.cache import never_cache
# from profiles.models import Customer
from django.conf import settings
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


STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY = settings.STRIPE_SECRET_KEY
stripe.api_key = STRIPE_SECRET_KEY
def checkout(request):
    form = OrderForm()
    all_products = Product.objects.all()
    bag = request.session.get('bag', {})
    
    grand_total = request.session.get("grand_total", 0)
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
    
    intent = stripe.PaymentIntent.create(
        amount=round(grand_total * 100),
        currency=settings.STRIPE_CURRENCY,
    )
    context = {
        "form": form,
        "STRIPE_PUBLIC_KEY": str(STRIPE_PUBLIC_KEY),
        "client_secret": intent.client_secret,
        "products": list_of_products,
    }

    return render(request, 'shopping_bag/checkout.html', context)


def checkout_confirm(request):
    
    print(STRIPE_SECRET_KEY)
    
    grand_total = request.session.get("grand_total", 0)
    
    try:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user_email = request.POST.get('user_email')
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        city = request.POST.get('city')
        country= request.POST.get("country")
        card_number = request.POST.get('card_number')
        cvc_number = request.POST.get('cvc_number')
        exp_month = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')
        print(exp_month)
        
        stripe_token = stripe.Token.create(
            card={
                
                "number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc_number,
            },
        )
        print(stripe_token)
        stripe_customer = stripe.Customer.create(
            card=stripe_token.card.id,
            description=user_email
        )

        stripe.Charge.create(
            amount=grand_total,
            currency=settings.STRIPE_CURRENCY,
            customer=stripe_customer.id
        )

        ## saving to Order
        current_order = Order(firstname=firstname, lastname=lastname,
        email=user_email, address_1=address_1, address_2=address_2,
        country=country,city=city)
        current_order.save()

        orders = request.session["bag"]
        for _orders in orders:
            current_order_item = OrderItem(item=orders[_orders], order=current_order.id)
            current_order_item.save()

        del request.session['bag']
        messages.success(request, "Order Successful")
        return HttpResponse("checkout confirmed")
    except Exception as e:
        messages.error(request, "Error:" + str(e))

    return redirect(reverse("view_bag"))