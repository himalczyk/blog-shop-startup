from django.conf.urls import include
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("", views.accounts, name="accounts"),
]