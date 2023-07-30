from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products),
    path('product/detail/<int:pk>/', views.product),
    path('product/archieve/<int:year>/<int:month>', views.product_archieve),
    ]