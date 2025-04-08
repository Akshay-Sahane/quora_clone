from django import views
from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.forms.user import UserRegisterForm, UserRegisterViewForm
from django.db import transaction


class UserView(views.View):
    http_method_names = [
        "get", "post"
    ]

    def get(self, request, *args, **kwargs):
        user_form = UserRegisterViewForm()
        return render(request, 'users/register.html', {
            'user_form': user_form
        })

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            request.POST._mutable = True # to modify request data
            request.POST['username'] = request.POST['email'] # set username as email
            user_form = UserRegisterForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                login(request, user)  # Auto login after registration
                return redirect('home')  # Redirect to home or feed
