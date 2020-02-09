from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html',views.home, name='home'),
    path('custom.html',views.custom, name='custom'),
    path('contact.html',views.contact, name='contact'),
    path('store.html',views.store, name='Store'),
    path('search.html',views.search, name='search'),
]