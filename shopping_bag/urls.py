from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_bag, name="view_bag"),
    path("add/<item_id>/", views.add_to_bag, name="add_to_bag"),
    path("adjust/<item_id>/<updated_value>/<delta>", views.adjust_bag, name="adjust_bag"),
    path("remove_from_bag/<item_id>/", views.remove_from_bag, name="remove_from_bag"),
    
    path("checkout/", views.checkout, name="checkout"),
    path("checkout_process", views.checkout_process, name="checkout_process"),
    path("order_success/", views.order_success, name="order_success"),
    
]
