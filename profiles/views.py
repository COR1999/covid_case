
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Customer
from .forms import CustomerForm

def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user = User.objects.filter(username=email).first()
            if user:
                messages.info(request, "Account with this email is already exists")
                return redirect(reverse("sign_up"))

            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            customer = Customer.objects.filter(email=email).first()
            form.save()
            user = User.objects.get(username=email)
            if customer:
                customer.user = user
                customer.save()
            else:
                customer = Customer(user=user,
                                    first_name=first_name,
                                    last_name=last_name,
                                    email=email)
                customer.save()
            
            
            messages.success(request, "Account was created for " + email)
            return redirect(reverse("login_page"))

    context = {
        "form": form,
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
        else:
            messages.info(request, "Sorry could not log in this user")

    return render(request, 'profiles/login.html')


def edit_profile(request):
    customer = Customer.objects.filter(email=request.user.username).first()
    print(customer)
    form = CustomerForm(request.POST or None,instance=customer)
    if form.is_valid():
            form.save()
            return redirect(reverse("products"))
            
    context = {
        "form": form,
    }
    return render(request, "profiles/edit_profile.html", context)