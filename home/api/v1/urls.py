from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter
app_name = 'api'
router = DefaultRouter()
router.register('post',PostApiView , basename='post')
router.register('comment',commentApiView , basename='comment')
# urlpatterns = [
#     path('post',PostApiView.as_view(), name="api_view"),
# ]
urlpatterns = router.urls
