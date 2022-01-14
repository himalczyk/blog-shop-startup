from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_index, name="home_index"),
    path("<int:pk>/", views.product_detail, name="product_detail"), # value passed in the URL is an integer, and its variable name is pk.
]