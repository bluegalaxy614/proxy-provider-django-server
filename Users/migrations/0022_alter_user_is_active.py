# Generated by Django 5.1.2 on 2024-10-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0021_confirmrequest_token_confirmrequest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]