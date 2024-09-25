from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter
app_name = 'api'
router = DefaultRouter()
router.register('Products',ProductApiView , basename='Products')
router.register('Categorys',CategorysApiView , basename='Categorys')
router.register('Orders',OrderViewSet , basename='Orders')
router.register('profile/favorates',favoratesViewSet , basename='favorates')
router.register('profile/list-ticket',listticketViewSet , basename='list-ticket')
router.register('comment',CommentViewSetApiView , basename='comment')

# urlpatterns = router.urls
urlpatterns = [
    path('v1/', include(router.urls)),  # اضافه کردن prefix برای API
]
