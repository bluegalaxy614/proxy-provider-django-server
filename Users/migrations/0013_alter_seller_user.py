# Generated by Django 5.1.2 on 2024-10-24 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0012_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.user'),
        ),
    ]
