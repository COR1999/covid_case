from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_bag, name="view_bag"),
    path("add/<item_id>/", views.add_to_bag, name="add_to_bag"),
    path("adjust/<item_id>/<updated_value>/<delta>", views.adjust_bag, name="adjust_bag"),
    path("remove_from_bag/<item_id>/", views.remove_from_bag, name="remove_from_bag"),
    path("checkout/", views.checkout, name="checkout"),
    path("checkout_process", views.checkout_process, name="checkout_process"),
    path("order_success/<int:order_id>", views.order_success, name="order_success"),
    path("order_history/", views.order_history, name="order_history"),
    path("place_order_again/<int:order_id>", views.place_order_again, name="place_order_again"),
    
]
