# Generated by Django 4.2 on 2024-04-19 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_like_users_productlike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productlike',
            old_name='article',
            new_name='product',
        ),
    ]