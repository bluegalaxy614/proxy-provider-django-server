# Generated by Django 5.1.2 on 2024-11-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0044_rename_accountdata_productdata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='seller_message',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
