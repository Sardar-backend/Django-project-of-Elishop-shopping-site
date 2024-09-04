from django.urls import path , include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('product_<int:pid>',product_view, name="product_single"),
    path('search/',search_view, name="search"),
    path('filter/',range_view, name="filter"),
    path('off-limit/',limit_view.as_view(), name="limit"),
    # path('vip-limit/',limit_vip, name="limit_vip"),
    path('api/',include('blog.api.v1.urls'))
]
