# Generated by Django 5.1.2 on 2024-10-29 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0022_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
