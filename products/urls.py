from django.urls import path
from . import views

urlpatterns=[
    path('', views.products_page, name='product_page')
]