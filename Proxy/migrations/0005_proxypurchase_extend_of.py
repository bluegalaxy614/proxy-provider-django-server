# Generated by Django 5.1.2 on 2024-10-20 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proxy', '0004_alter_proxypurchase_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxypurchase',
            name='extend_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Proxy.proxypurchase'),
        ),
    ]
