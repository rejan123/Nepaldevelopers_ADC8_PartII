from django.urls import path
from .views import *

urlpatterns = [
    path('user/',view_get_post_user),
    path('user/<int:ID>',view_getByID_updateByID_deleteByID),
    path('user/<int:page_no>/<int:items>',get_pagination)
] 