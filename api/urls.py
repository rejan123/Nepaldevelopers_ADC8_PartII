from django.urls import path
from .views import *

urlpatterns = [
    path('display/',view_get_post_user),
    path('display/<int:ID>',view_getByID_updateByID_deleteByID),
] 