from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("", views.accounts, name="accounts"),
    path("", views.register, name="register")
]