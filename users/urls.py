from django.urls import path, include
from . import views

urlpatterns = [
    path("dashboard", views.dashboard_base, name="dashboard_base"),
    path("", views.accounts, name="accounts"),
    path("register", views.register, name="register"),
    path("", views.oauth, name="oauth"),
]