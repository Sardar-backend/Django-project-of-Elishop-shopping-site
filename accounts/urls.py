from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login',login_view, name="login_view"),
    path('logout',logout_view ,name="logout_view"),
    path('signup',signup_view ,name="signup_view")
]
