from django.urls import path , include
from home.views import *
app_name = 'home'
urlpatterns = [
    path('',home_view.as_view(), name="index"),
    # path('contact',contact_view, name="contact_view"),
    path('profile/add-ticket',contact_view, name="contact_view"),
    path('category',category_view.as_view(), name="category_view"),
    path('products/',products_view.as_view(), name="products_view"),
    path('product-<str:cat_name>/',products_views, name="pros"),
    path('products_exist/',products_exist.as_view(), name="exist"),
    path('products_ready/',products_ready.as_view(), name="ready"),
    # path('newsletter',newsletter, name="prose"),
    path('profile',profile, name="profile"),
    path('profile/add_adress',add_adress, name="profile_add_adress"),
    path('profile/edit_personal',edit_personal, name="edit_personal"),
    path('profile/favorates',favorates, name="favorates"),
    path('profile/list-ticket',list_ticket, name="list_ticket"),
    path('profile/product-orders',product_orders, name="product-orders"),
    path('profile/notifications',notifications, name="notifications"),
    path('about',about.as_view(), name="about"),
    path('api/',include('home.api.v1.urls'))
    ]
