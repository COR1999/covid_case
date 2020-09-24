
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)

            return redirect(reverse("login_page"))


    grand_total = request.session.get("grand_total", {})
    context = {
        "form": form,
        "grand_total": grand_total
    }
    return render(request, 'profiles/sign_up.html', context)



def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        backend ='django.contrib.auth.backends.ModelBackend'
        if user is not None:
            login(request, user)
            return redirect("products")
    grand_total = request.session.get("grand_total", {})
    context = {
        "grand_total": grand_total
    }
    return render(request, 'profiles/Login.html', context)

