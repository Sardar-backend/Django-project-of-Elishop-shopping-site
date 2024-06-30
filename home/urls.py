from django.urls import path
from home.views import *
app_name = 'home'
urlpatterns = [
    path('',home_view, name="blog_view"),
    path('contact',contact_view, name="contact_view"),
    path('category',category_view, name="category_view"),
    path('products',products_view, name="products_view"),
    path('product-<str:cat_name>',products_views, name="pros"),
    path('newsletter',newsletter, name="prose"),
    
]
