# Generated by Django 5.1.2 on 2024-10-20 07:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_remove_product_category_product_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='message',
            new_name='buyer_message',
        ),
        migrations.AddField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='seller_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
