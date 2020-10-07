
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
            # print(form)
            username = form.cleaned_data["username"]
            # print(username)
            # first_name = form.cleaned_data["first_name"]
            # last_name = form.cleaned_data["last_name"]
            # phone = form.cleaned_data["phone"]
            # email = form.cleaned_data["email"]
            # address_line_1 = form.cleaned_data["address_line_1"]
            # address_line_2 = form.cleaned_data["address_line_2"]
            # city = form.cleaned_data["city"]
            # country = form.cleaned_data["country"]
            # print(user)
            
            form.save()
            # user = User(user=request.user)
            # customer = Customer(
            #     user=request.user,
            #     name=username,
            #     first_name=first_name,
            #     last_name=last_name,
            #     # phone=phone,
            #     email=email,
            #     # address_line_1=address_line_1,
            #     # address_line_2=address_line_2,
            #     # city=city,
            #     # country=country,
            # )
            # customer.save()
            messages.success(request, "Account was created for " + username)
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


def edit_profile(request):
    # customer = Customer.objects.get(name=request.user)
    customer = Customer.objects.filter(user=request.user).first()
    if customer:
        form = CustomerForm(request.POST or None,instance=customer)
        if form.is_valid():
                form.save()
                return redirect(reverse("products"))
        
        print("we have a customer")
    else:
        form = CustomerForm(instance=request.user)
        if request.method == "POST":
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                address_line_1 = form.cleaned_data["address_line_1"]
                address_line_2 = form.cleaned_data["address_line_2"]
                country = form.cleaned_data["country"]
                city = form.cleaned_data["city"]
                print("form is valid")
                customer = Customer(
                    user=request.user,
                    name=request.user.username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address_line_1=address_line_1,
                    address_line_2=address_line_2,
                    country=country,
                    city=city,
                )
                customer.save()
                print("customer saved", customer)
                    
                return redirect(reverse("products"))

    

    context = {
        "form": form,
    }
    return render(request, "profiles/edit_profile.html", context)