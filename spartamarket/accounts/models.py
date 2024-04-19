from django.contrib.auth.models import AbstractUser
from django.db import models
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your models here.


class User(AbstractUser):
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = models.DateField(auto_now_add=True)
