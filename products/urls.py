from django.urls import path,include
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('add-product',get_products),
    path('post_add_product',post_add_product),
    path('update_product/<int:ID>',get_update_products),
    path('post_update_product/<int:ID>',post_update_product),
    path('post_delete/<int:ID>',post_delete_product)
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
