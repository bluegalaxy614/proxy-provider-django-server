# Generated by Django 5.1.2 on 2024-10-27 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proxy', '0011_alter_proxypurchase_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxypurchase',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 24, 17, 11, 19, 519402)),
        ),
    ]