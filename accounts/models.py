from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    phone_no = models.CharField(max_length=50, default=True)

    def __str__(self):
        return self.username
