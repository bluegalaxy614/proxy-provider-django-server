# Generated by Django 5.1.2 on 2024-10-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0026_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.IntegerField(default=0),
        ),
    ]
