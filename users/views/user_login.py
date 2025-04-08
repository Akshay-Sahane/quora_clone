from django import views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms.user import UserLoginForm
from users.models import UserModel


class UserLoginView(views.View):
    http_method_names = [
        "get", "post"
    ]

    def get(self, request, *args, **kwargs):
        user_form = UserLoginForm()
        return render(request, 'users/login.html', {
            'user_form': user_form
        })

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
        login(request, user)
        return redirect('home')  # Redirect to home or feed
