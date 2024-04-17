from django import forms
from products import models
from accounts.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['title', 'content', 'price']

    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #     self.fields['author'].queryset = User.objects.all()

    def save(self, author):
        product_instance = super().save(commit=False)
        product_instance.author = author
        product_instance.save()
        return product_instance
