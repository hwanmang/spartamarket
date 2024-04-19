from django.conf import settings
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField()
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", blank=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )

    def __str__(self) -> str:
        return self.title
