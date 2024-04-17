from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    good_products = models.ManyToManyField(
        'products.Product', related_name='good_users')
