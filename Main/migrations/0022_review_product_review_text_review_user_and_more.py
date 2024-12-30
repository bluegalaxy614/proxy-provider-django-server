# Generated by Django 5.1.2 on 2024-10-24 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0021_review_alter_balancetopup_table_alter_category_table_and_more'),
        ('Users', '0010_alter_seller_table_alter_token_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Main.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.user'),
        ),
        migrations.AlterModelTable(
            name='review',
            table='reviews',
        ),
    ]
