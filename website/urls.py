from django.urls import path

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact')
]