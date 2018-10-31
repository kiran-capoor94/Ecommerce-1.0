from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import login_page, register_page, guest_register_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]