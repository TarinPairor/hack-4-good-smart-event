from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AnonymousUser



# Create your views here.
def home_page(request):
    return render(request, "home_page.html")

def anonymous_user_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        users = AnonymousUser.objects.all()
        context = {'users': users}
        return render(request, 'anonymous_user_list.html', context)
    else:
        return None

## ADMIN USER VIEWS

def admin_user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken.')
        else:
            user = User.objects.create_user(username=username, password=password, is_superuser=True, is_staff=True)
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('volunteers:admin_user_login')
    return render(request, 'admin_user_signup.html')

@csrf_exempt
def admin_user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('volunteers:validate')
        messages.error(request, 'Invalid username or password, or the user is not a superuser.')
    return render(request, 'admin_user_login.html')


def admin_user_logout(request):
    logout(request)
    return redirect('volunteers:home_page')

## ANONYMOUS USER VIEWS

def anonymous_user_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        if AnonymousUser.objects.filter(name=name).exists():
            messages.error(request, 'Name is taken.')
            return redirect('volunteers:home_page')  # Redirect back to home_page
        else:
            user = AnonymousUser(name=name)
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('volunteers:validate')
    return render(request, 'anonymous_user_signup.html')


def anonymous_user_logout(request):
    return redirect('volunteers:home_page')


def anonymous_user_login(request):
    if request.method == 'POST':
        name = request.POST['name']
        if AnonymousUser.objects.filter(name=name).exists():
            return redirect('volunteers:validate')
        else:
            messages.error(request, 'Invalid name.')
    else:
        return render(request, 'anonymous_user_login.html')
    
# VALIDATE VIEW    
def validate(request):
    users = AnonymousUser.objects.all()
    if request.user.is_authenticated and request.user.is_superuser:
        user_type = 'admin'
    else:
        user_type = 'anonymous'
    context = {
        'user_type': user_type,
        'users': users   
       }
    return render(request, 'validate.html', context)

# myproject/
#     manage.py
#     myproject/
#         __init__.py
#         settings.py
#         urls.py
#         asgi.py
#         wsgi.py
#     users/
#         migrations/
#         __init__.py
#         admin.py
#         apps.py
#         models.py
#         tests.py
#         views.py
#     events/
#         migrations/
#         __init__.py
#         admin.py
#         apps.py
#         models.py
#         tests.py
#         views.py