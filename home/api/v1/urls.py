from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter
app_name = 'api'
router = DefaultRouter()
router.register('Products',ProductApiView , basename='Products')
router.register('Categorys',CategorysApiView , basename='Categorys')
router.register('Orders',OrderViewSet , basename='Orders')
router.register('profile',profileViewSet , basename='profile')
# router.register('profile/favorates',favoratesViewSet , basename='favorates')
router.register('profile/ticket',listticketViewSet , basename='list-ticket')
router.register('comment',CommentViewSetApiView , basename='comment')
router.register('cart',cartApiView , basename='cart')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/index',indexApiView.as_view() , name='index'),
    path('v1/add_adress',addadressApiView.as_view() , name='add_adress'),
    path('v1/profile/favorates',favoratesViewSet.as_view() , name='favorates'),
    path('v1/profile/Createfavorates',favoratesCreateViewSet.as_view() , name='favorates'),
    # path('v1/cart',cartApiView.as_view() , name='add_to_cart'),
    # path('cart/remove/<int:product_id>/', cartApiView.as_view(), name='cart-remove'),
    # path('v1/add-ticket',TicketCreateView.as_view() , name='add_ticket'),
]

urlpatterns += router.urls
