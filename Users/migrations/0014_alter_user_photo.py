# Generated by Django 5.1.2 on 2024-10-24 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0013_alter_seller_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photos/users/%Y/%m/%d/'),
        ),
    ]