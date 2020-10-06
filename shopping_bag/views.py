from django.http import request, JsonResponse
from django.http.response import HttpResponseNotAllowed
import json
from shopping_bag.forms import OrderForm
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from profiles.models import Customer
# from decimal import Decimal, Rounded
from django.contrib import messages
from products.models import Product
from .forms import OrderForm
from .models import OrderItem, Order
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.views.decorators.http import require_http_methods
import stripe
from django.forms.models import model_to_dict


@never_cache
def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    # q_set_products = []
    all_products = Product.objects.all()
    # print("view_bag")
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
                "number_in_stock": product.number_in_stock,
                "quantity": bag_quantity,
                "item_total_price": total_price
            }
            list_of_products.append(bag_set)
            final_price += total_price
    # print(grand_total)
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
    # print(item_id)
    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = request.POST.get('quantity')
    grand_total = request.session.get("grand_total", 0)
    bag = request.session.get('bag', {})
    price = product.price
    if int(quantity) <= product.number_in_stock:
        if len(quantity) > 0:
            # print(type(quantity))
            # print(quantity)
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

    product = Product.objects.get(pk=item_id)

    bag = request.session.get('bag', {})

    if int(bag[item_id]) == product.number_in_stock:
        if delta == "minus":
            bag[item_id] = int(updated_value) - 1
            request.session["bag"] = bag
    if delta == "minus":
        if int(updated_value) > 0:
            if int(updated_value) <= product.number_in_stock:
                bag[item_id] = int(updated_value) - 1
                request.session["bag"] = bag
            # else:
                # messages.info(request, "Sorry not enough in stock")
        # else:
            # messages.info(request, "Sorry your item quantity cant be less then 0")
    if delta == "add":
        if int(updated_value) >= 0:
            if int(updated_value) < product.number_in_stock:
                bag[item_id] = int(updated_value) + 1
                request.session["bag"] = bag

    # return redirect(reverse("view_bag"))
    return JsonResponse({"status": "success",},status=200)


def remove_from_bag(request, item_id):
    bag = request.session.get('bag', {})
    # print(bag)
    del request.session["bag"][item_id]
    request.session.modified = True
    return redirect((reverse("view_bag")))

def checkout(request):
    form = OrderForm()
    user = request.user

    # Add logic for none logged in users to purchase!!!!

    customer = Customer.objects.get(user_id=user.id)

    if customer:
        form = OrderForm(instance=customer)

    bag = request.session.get('bag', {})
    # q_set_products = []
    all_products = Product.objects.all()
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
                "quantity": bag_quantity,
                "item_total_price": total_price
            }
            list_of_products.append(bag_set)
    
    try:
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        stripe.api_key = stripe_secret_key
        grand_total = request.session.get("grand_total", 0)
        intent = stripe.PaymentIntent.create(
            amount=round(grand_total * 100),
            currency=settings.STRIPE_CURRENCY,
        )

        context = {
            "form": form,
            "STRIPE_PUBLIC_KEY": str(stripe_public_key),
            "client_secret": intent.client_secret,
            "products": list_of_products,
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
    # print(request.POST)
    # print(post_details)
    # print(request.user)

    for _post_details in post_details:
        _post_details = _post_details.split("=")
        post_data[_post_details[0]] = _post_details[1]

    # print(post_data)
    grand_total = request.session.get("grand_total", 0)
    pid = request.POST.get('client_secret').split('_secret')[0]
    # print(type(grand_total))
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_grand_total = round(grand_total * 100)
    stripe.api_key = stripe_secret_key


    try:
        # first_name = post_data['first_name']
        # last_name = post_data['last_name']
        email = post_data['email']
        # phone = post_data["phone"]
        # address_line_1 = post_data['address_line_1']
        # address_line_2 = post_data['address_line_2']
        # city = post_data['city']
        # country= post_data['country']
        token = request.POST.get('token')

        # print("customer",check_customer)
        # if len(check_customer < 1):
        stripe_customer = stripe.Customer.create(
            card=token,
            description=email
        )
        # else:
        # stripe_customer = check_customer.stripe_pid

        intent = stripe.PaymentIntent.create(
            amount=stripe_grand_total,
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
        # pass customer into current order if created else create new customer
        # print(email)
        check_customer = Customer.objects.get(user=request.user)
        current_order = Order(user_profile=check_customer, stripe_pid=stripe_customer.id, order_total=grand_total, order_confirmed=True)
        current_order.save()
 
 
        # print(current_order)
        orders = request.session["bag"]


        #  Make a funciton !!!!!!
        for _orders in orders:
            # saving of product item
            current_order_item = OrderItem(item=Product.objects.get(id=_orders),
                                        order=Order.objects.get(id=current_order.id), quantity=orders[_orders])
            current_order_item.save()
            print(current_order.id)
            # updating of stock
            product_details = Product.objects.get(id=_orders)
            product_details.number_in_stock = product_details.number_in_stock - orders[_orders]
            product_details.save()

        del request.session['bag']
        del request.session["grand_total"]
        # context = {
        #     "message": "Thank you! Your purchase was successful",
        #     "stripe_pid": current_order.stripe_pid,
        #     "first_name": current_order.first_name,
        #     "last_name": current_order.last_name,
        #     "email": current_order.email,
        #     "address_line_1": current_order.address_line_1,
        #     "address_line_2": current_order.address_line_2,
        #     "phone": current_order.phone,
        #     "country": current_order.country,
        #     "city": current_order.city,
        #     "order_total": current_order.order_total,
        # }
        json_current_order = model_to_dict(current_order)
        # print(json_current_order)
        context = {
            "message": "Thank you! Your purchase was successful",
            "order": json_current_order,
        }

        # messages.info(request, "Thank you! Your purchase was successful")
        # messages = "Thank you! Your purchase was successful"
    except Exception as e:
        # messages.error(request, "Error:" + str(e))
        context = {
            "message": str(e),
        }  
    return JsonResponse(context)



def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        "order": order,
        "order_items": order_items
    }
    return render(request, "shopping_bag/order_success.html", context)