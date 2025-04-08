from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    email = models.EmailField(_("email address"), unique=True)

    class Meta:
        verbose_name = "usermodel"
        verbose_name_plural = "usersmodel"
        db_table = "UserModel"
