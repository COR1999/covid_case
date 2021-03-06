from django.http import request, JsonResponse
from shopping_bag.forms import OrderForm
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from profiles.models import Customer
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
    all_products = Product.objects.all()
    grand_total = request.session.get("grand_total", {})
    final_price = 0
    list_of_products = []
    for item, key in bag.items():
        bag_products = all_products.filter(pk=int(item))
        for product in bag_products:
            # All product attributes are mandatory so don't have to check if they are None
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
    request.session["grand_total"] = final_price

    context = {
        "products": list_of_products,
        "grand_total": grand_total,

    }
    return render(request, 'shopping_bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = request.POST.get('quantity')
    grand_total = request.session.get("grand_total", 0)
    bag = request.session.get('bag', {})
    price = product.price
    if int(quantity) <= product.number_in_stock:
        if len(quantity) > 0:
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
    if delta == "add":
        if int(updated_value) >= 0:
            if int(updated_value) < product.number_in_stock:
                bag[item_id] = int(updated_value) + 1
                request.session["bag"] = bag

    return JsonResponse({"status": "success",},status=200)


def remove_from_bag(request, item_id):
    """A view that deletes the item from the session"""
    del request.session["bag"][item_id]
    request.session.modified = True
    return redirect((reverse("view_bag")))

def checkout(request):
    """A view that loads the checkout page. if the user is signed in populates the form with their information"""
    if request.user.is_anonymous:
        form = OrderForm()
    else:
        customer = Customer.objects.filter(email=request.user.username).first()
        form = OrderForm(instance=customer)

    bag = request.session.get('bag', {})
    
    list_of_products = []
    for item, key in bag.items():
        product = Product.objects.get(pk=int(item))
        if product:
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
        else:
            # Should not happen cause allready displayed products to the user
            messages.info(request, "Sorry could not find this product on our records.")
            delete_bag(request)
            return redirect(reverse("products"))

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
        # Log the Exception to a log file
        messages.error(request, "Sorry there has been an error in the checkout process please try again later.")


    return render(request, 'shopping_bag/checkout.html', context)

@require_http_methods(["POST"])
def checkout_process(request):
    """A view that proccess the checkout information and adds the necessary objects to the database."""
    post_details = request.POST.get('form').split("&")
    post_data = {}
    
    for _post_details in post_details:
        _post_details = _post_details.split("=")
        post_data[_post_details[0]] = _post_details[1]
    
    grand_total = request.session.get("grand_total", 0)
    
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key


    try:
        # Decode the data thats been url encoded
        email = post_data['email'].replace("%40", "@")
        token = request.POST.get('token')
        first_name = post_data['first_name']
        last_name = post_data['last_name'].replace("%20", " ")
        phone = post_data['phone']
        address_line_1 = post_data['address_line_1'].replace("%20", " ")
        address_line_2 = post_data['address_line_2'].replace("%20", " ")
        city = post_data['city'].replace("%20", " ")
        country = post_data['country']
        

        current_customer_id = 0
        if request.user.is_anonymous:
            check_customer = Customer.objects.filter(email=email).first()
            if check_customer:
                current_customer_id = check_customer.id
            else:
                customer = Customer(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address_line_1=address_line_1,
                    address_line_2=address_line_2,
                    city=city,
                    country=country,
                )
                customer.save()
                current_customer_id = customer.id
            # Getting the Customer
            customer = Customer.objects.get(id=current_customer_id)
        else:
            # Getting the Customer
            customer = Customer.objects.get(user=request.user)
            
        customer.first_name = first_name
        customer.last_name = last_name
        customer.phone = phone
        customer.address_line_1 = address_line_1
        customer.address_line_2 = address_line_2
        customer.city = city
        customer.country = country
        customer.save()

        stripe_customer = stripe.Customer.create(card=token, description=email)
        ## saving to Order
        current_order = Order(customer_profile=customer, stripe_pid=stripe_customer.id, order_total=grand_total, order_confirmed=True)
        current_order.save()

        orders = request.session["bag"]

        for item in orders:
            # saving of product item
            current_order_item = OrderItem(item=Product.objects.get(id=item),
                                        order=Order.objects.get(id=current_order.id), quantity=orders[item])
            current_order_item.save()

            # updating of stock
            product_details = Product.objects.get(id=item)
            product_details.number_in_stock = product_details.number_in_stock - orders[item]
            product_details.save()

        delete_bag(request)

        order_id = current_order.id
        
        context = {
            "message": "Thank you! Your purchase was successful",
            "order_id": str(order_id),
        }
    except Exception as e:
        context = {
            "message": str(e),
        }  
    return JsonResponse(context)



def order_success(request, order_id):
    """A view that renders the order success page"""
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        "order": order,
        "order_items": order_items
    }
    return render(request, "shopping_bag/order_success.html", context)



@login_required
def order_history(request):
    """Load a view that shows the order history"""
    customer = Customer.objects.filter(email=request.user.email).first()
    all_orders = Order.objects.filter(customer_profile=customer).order_by("-ordered_date")
    customers_orders = []
    for item in all_orders:
        order_items = OrderItem.objects.filter(order=item.id)
        customers_order = {
            "order": item,
            "order_items": list(order_items),
        }
        customers_orders.append(customers_order)
    context = {
        "customer": customer,
        "customers_order": customers_orders,
    }
    return render(request, "shopping_bag/order_history.html", context)


@login_required
def place_order_again(request, order_id):
    """View that lets the user replace that same order"""
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    bag = request.session.get("bag", {})
    grand_total = request.session.get("grand_total", 0)
    for item in order_items:
        quantity = item.quantity
        if quantity <= item.item.number_in_stock:
            item_id = item.item.id
            
            grand_total += float(item.item.price) * quantity
            
            bag[item_id] = quantity
            request.session["bag"] = bag
            request.session["grand_total"] = grand_total
        else:
            messages.info(request, "Sorry cant replace this order item is out of stock")
        
    return redirect((reverse("products")))


def delete_bag(request):
    del request.session['bag']
    del request.session["grand_total"]