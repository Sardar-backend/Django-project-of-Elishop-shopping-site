from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('login',login_view, name="login_view"),
    path('product_<int:pid>',product_view, name="product_view"),
    path('search/',search_view, name="search")
]
