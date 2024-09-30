from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # username = None
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    # objects = CustomUserManager()

    def __str__(self):
        return self.username



