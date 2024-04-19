from django import forms
from products import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['title', 'content', 'price']

    def save(self, author):
        product_instance = super().save(commit=False)
        product_instance.author = author
        product_instance.save()
        return product_instance
