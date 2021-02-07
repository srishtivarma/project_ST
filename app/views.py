from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='create')
def home(request):
    return render(request, 'home.html')


def create(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect!')

    context = {}
    return render(request, 'home.html', context)

