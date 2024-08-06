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
    path('cart/add', views.addProductToCart, name='add-product'),
    path('product/remove', views.removeProduct, name='remove-product'),
    path('cart/increase', views.IcreaseQuantity, name='increase-quantity'),
    path('cart/decrease', views.DecreaseQuantity, name='decrease-quantity'),
    path('checkout/product/remove', views.removeProductFromCheckout, name='remove-product'),
    path('checkout/quantity/increase', views.IcreaseQuantityFromCheckout, name='increase-quantity'),
    path('checkout/quantity/decrease', views.DecreaseQuantityFromCheckout, name='decrease-quantity')

]