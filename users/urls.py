from django.urls import path

from users.views.logout import UserLogout
from users.views.user_register import UserView
from users.views.user_login import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserView.as_view()),
    path('logout/', UserLogout.as_view()),
]
