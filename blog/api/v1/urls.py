from django.urls import path
from .view import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
app_name = 'api_v1'
# router = DefaultRouter()
# router.register('post',PostApiView , basename='post')
# router.register('comment',commentApiView , basename='comment')
urlpatterns = [
    path('register',reqistration.as_view(), name="api_view"),
    path('token/login',ObtainAuthToken.as_view(), name="token-login"),
    # path('send-email',send_email.as_view(), name="send-email"),
    path('jwt/create', customTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verfiy/', TokenVerifyView.as_view(), name='token_refresh'),
    path('change_password', changepasswordView.as_view(), name='token_refresh')
]
# urlpatterns += router.urls
