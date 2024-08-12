from django.urls import path
from .view import *

app_name = 'api_v1'
# router = DefaultRouter()
# router.register('post',PostApiView , basename='post')
# router.register('comment',commentApiView , basename='comment')
urlpatterns = [
    path('register',reqistration.as_view(), name="api_view")
]
# urlpatterns += router.urls
