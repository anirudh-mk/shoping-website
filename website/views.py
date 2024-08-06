from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from website.models import Products, UserCart


def index(request):
    product_queryset = Products.objects.all()
    mens_products = Products.objects.filter(catogery='mens').all().values()
    return render(request, 'index.html', {
        'products': product_queryset,
        'mens': mens_products
    })


def mensShirts(request):
    mens_products = Products.objects.filter(catogery='mens').all()
    return render(request, 'mens_shirts.html', {
        'products': mens_products
    })


def ProductDetails(request):
    mens_products = Products.objects.filter(catogery='mens').all()
    return render(request, 'product-details.html', {
        'products': mens_products
    })


def mensTrousers(request):
    mens_products = Products.objects.filter(catogery='mens').all()
    return render(request, 'mens_shirts.html', {
        'products': mens_products
    })


def cart(request):
    user = request.user
    user_cart_queryset = UserCart.objects.filter(user=user).all()
    subtotal = user_cart_queryset.aggregate(total=Sum('total'))['total'] or 0
    shipping_cost = 150
    echo_tax = 0
    if subtotal > 800:
        echo_tax = 4
        shipping_cost = 0

    total = shipping_cost + echo_tax + subtotal

    return render(request, 'cart.html', {
        'user_cart_queryset': user_cart_queryset,
        'subtotal': subtotal,
        'echo_tax': echo_tax,
        'shipping_cost': shipping_cost,
        'total': total
    })


def checkout(request):
    user = request.user
    user_cart_queryset = UserCart.objects.filter(user=user).all()
    subtotal = user_cart_queryset.aggregate(total=Sum('total'))['total'] or 0
    shipping_cost = 150
    echo_tax = 0
    if subtotal > 800:
        echo_tax = 4
        shipping_cost = 0

    total = shipping_cost + echo_tax + subtotal

    return render(request, 'checkout.html', {
        'user_cart_queryset': user_cart_queryset,
        'subtotal': subtotal,
        'echo_tax': echo_tax,
        'shipping_cost': shipping_cost,
        'total': total
    })


def contact(request):
    return render(request, 'contact-us.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if email and password and username:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=name, email=email, password=password, username=username)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'all fields required')
            return redirect('register')
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'invalid username and password')
            return redirect('login')

    else:
        return render(request, 'login.html')


def addProductToCart(request):
    product_id = request.GET.get('id')
    user = request.user

    product_instance = Products.objects.filter(id=product_id).first()

    user_cart = UserCart(
        product=product_instance,
        user=user,
        total=product_instance.price
    )
    user_cart.save()

    return redirect('index')


def removeProduct(request):
    product_id = request.GET.get('id')
    UserCart.objects.filter(product_id=product_id).delete()
    return redirect('cart')


def IcreaseQuantity(request):
    product_id = request.GET.get('id')
    user_cart = UserCart.objects.filter(product_id=product_id).first()
    product = Products.objects.filter(id=product_id).first()
    product_quantity = user_cart.quantity + 1
    product_price = product.price * product_quantity

    UserCart.objects.filter(product_id=product_id).update(
        quantity=product_quantity,
        total = product_price
    )

    return redirect('cart')

def DecreaseQuantity(request):
    product_id = request.GET.get('id')
    user_cart = UserCart.objects.filter(product_id=product_id).first()
    product = Products.objects.filter(id=product_id).first()
    product_quantity = user_cart.quantity - 1
    if product_quantity == 0:
        UserCart.objects.filter(product_id=product_id).delete()
    product_price = product.price * product_quantity

    UserCart.objects.filter(product_id=product_id).update(
        quantity=product_quantity,
        total = product_price
    )

    return redirect('cart')


def removeProductFromCheckout(request):
    product_id = request.GET.get('id')
    UserCart.objects.filter(product_id=product_id).delete()
    return redirect('checkout')


def IcreaseQuantityFromCheckout(request):
    product_id = request.GET.get('id')
    user_cart = UserCart.objects.filter(product_id=product_id).first()
    product = Products.objects.filter(id=product_id).first()
    product_quantity = user_cart.quantity + 1
    product_price = product.price * product_quantity

    UserCart.objects.filter(product_id=product_id).update(
        quantity=product_quantity,
        total = product_price
    )

    return redirect('checkout')

def DecreaseQuantityFromCheckout(request):
    product_id = request.GET.get('id')
    user_cart = UserCart.objects.filter(product_id=product_id).first()
    product = Products.objects.filter(id=product_id).first()
    product_quantity = user_cart.quantity - 1
    if product_quantity == 0:
        UserCart.objects.filter(product_id=product_id).delete()
    product_price = product.price * product_quantity

    UserCart.objects.filter(product_id=product_id).update(
        quantity=product_quantity,
        total = product_price
    )

    return redirect('checkout')