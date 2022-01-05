from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm

# Create your views here.

def dashboard(request):
    print("I am in dashboard")
    return render(request, "users/dashboard.html")

def accounts(request):
    return render(request, "users/registration/login.html")

def register(request):
    print("First level register")
    if request.method == "GET":
        print("I am in get")
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))