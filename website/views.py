from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')

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
