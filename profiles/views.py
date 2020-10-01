
from django.shortcuts import render, redirect, reverse

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
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
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

def my_profile(request, user_name):
    # Should be a id not user_name !!!
    customer = Customer.objects.get(name=user_name)

    context = {
        "profile": customer,
    }
    return render(request, "profiles/my_profile.html" ,context)


def edit_profile(request, user_name):
    customer = Customer.objects.get(name=user_name)

    form = CustomerForm(request.POST or None,instance=customer)
    if form.is_valid():
            form.save()
            return redirect(reverse("products"))

    context = {
        "form": form,
    }
    return render(request, "profiles/edit_profile.html", context)