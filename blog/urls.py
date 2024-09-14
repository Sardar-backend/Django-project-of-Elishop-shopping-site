from django.urls import path , include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('product_<int:pid>',product_view, name="product_single"),
    path('search/',search_view, name="search"),
    path('filter/',range_view, name="filter"),
    path('off-limit/',limit_view.as_view(), name="limit"),
    path('delete_favorates<int:pid>/',delete_favorates, name="delete_favorates"),
    path('delete_adresses<int:pid>/',delete_adresses, name="delete_adresses"),
    
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    # path('vip-limit/',limit_vip, name="limit_vip"),
    path('api/',include('blog.api.v1.urls'))
]
