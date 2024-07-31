from django.urls import path

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('mens/shirts', views.mensShirts, name='mens-shirts'),
    path('mens/trousers', views.mensTrousers, name='mens-trousers'),
    path('product-details', views.ProductDetails, name='product-details'),
]