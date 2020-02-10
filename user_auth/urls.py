from django.urls import path,include
from.views import *
from django.contrib.auth import logout,login


#Core Management URL
urlpatterns=[
    path('login/',get_login_page,name="login"),
    path('post_login',post_login),
    path('sign-up/',get_sign_up,name="sign_up"),
    path('post_sign_up',post_sign_up),
    path('logout/',user_logout,name="logout")
]




