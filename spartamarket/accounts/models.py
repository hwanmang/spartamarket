from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    good_products = models.ManyToManyField(
        'products.Product', related_name='good_users')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = models.DateField(auto_now_add=True)
