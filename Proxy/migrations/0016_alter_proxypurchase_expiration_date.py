# Generated by Django 5.1.2 on 2024-10-27 19:32

import Proxy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proxy', '0015_alter_proxypurchase_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxypurchase',
            name='expiration_date',
            field=models.DateTimeField(default=Proxy.models.get_expiration_date),
        ),
    ]
