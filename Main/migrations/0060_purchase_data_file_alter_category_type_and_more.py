# Generated by Django 5.1.2 on 2024-11-14 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0059_alter_referraltransaction_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='data_file',
            field=models.FileField(blank=True, null=True, upload_to='products_data'),
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(blank=True, choices=[('proxy', 'Прокси'), ('account', 'Аккаунт'), ('soft', 'Софт')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('proxy', 'Прокси'), ('account', 'Аккаунт'), ('soft', 'Софт')], db_index=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.product'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='type',
            field=models.CharField(choices=[('proxy', 'Прокси'), ('account', 'Аккаунт'), ('soft', 'Софт')]),
        ),
    ]
