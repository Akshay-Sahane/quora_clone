from django.contrib.auth import logout
from django.shortcuts import redirect
from django import views


class UserLogout(views.View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')  # Redirect to home or feed

