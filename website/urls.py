from django.urls import path

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout')
]