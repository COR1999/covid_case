
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from .forms import CustomerForm

def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data("username")
            print(username)
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            address_line_1 = form.cleaned_data.get("address_line_1")
            address_line_2 = form.cleaned_data.get("address_line_2")
            country = form.cleaned_data.get("country")
            # print(user)
            
            customer = Customer(
                user=User.Objects.get(user=username),
                name=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                country=country,
            )
            customer.save()
            messages.success(request, "Account was created for " + customer)
            return redirect(reverse("login_page"))
        else:
            messages.info(request, "Username OR password is incorrect")


    # grand_total = request.session.get("grand_total", {})
    context = {
        "form": form,
        # "grand_total": grand_total
    }
    return render(request, 'profiles/sign_up.html', context)


def logout_user(request):
    logout(request)
    return redirect(reverse("login_page"))

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("products")
    # grand_total = request.session.get("grand_total", {})
    context = {
        # "grand_total": grand_total
    }
    return render(request, 'profiles/login.html')

def my_profile(request):
    # Should be a id not user_name !!!
    context = {}
    customer = Customer.objects.get(name=request.user)
    print(customer)
    if customer:
        context = {
            "profile": customer,
        }
    
    return render(request, "profiles/my_profile.html" ,context)


def edit_profile(request):
    customer = Customer.objects.get(name=request.user)

    form = CustomerForm(request.POST or None,instance=customer)
    if form.is_valid():
            form.save()
            return redirect(reverse("products"))

    context = {
        "form": form,
    }
    return render(request, "profiles/edit_profile.html", context)