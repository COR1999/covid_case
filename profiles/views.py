
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required
def sign_up(request):
    """A View to sign up the user and create a customer"""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.filter(username=email).first()
            if user:
                messages.info(request, "Account with this email is already exists")
                return redirect(reverse("sign_up"))
            else:
                form.save()
                # Get the user we just created
                user = User.objects.get(username=email)
                if user:
                    # Check to see if the user has a customer instance already created. 
                    customer = Customer.objects.filter(email=email).first()
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
                else:
                    # Should never happend cause we just saved the form but just incase 
                    messages.error(request, "Account not created properly")
                    return redirect(reverse("sign_up"))
    else:
        form = SignUpForm()
        
    context = {
        "form": form,
    }
    return render(request, 'profiles/sign_up.html', context)

@login_required
def logout_user(request):
    """A view to logout the user"""
    logout(request)
    return redirect(reverse("login_page"))

def login_page(request):
    """A view to login the user if there details are valid"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("products")
        else:
            messages.info(request, "Sorry could not log in this user")
    else:
        return render(request, 'profiles/login.html')

@login_required
def edit_profile(request):
    """A view to let the user edit their customer profile"""
    customer = Customer.objects.filter(email=request.user.username).first()
    form = CustomerForm(request.POST or None, instance=customer)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("products"))
        # ELSE error message on the form
    
    context = {
        "form": form,
    }
    return render(request, "profiles/edit_profile.html", context)