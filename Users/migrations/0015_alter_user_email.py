# Generated by Django 5.1.2 on 2024-10-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
