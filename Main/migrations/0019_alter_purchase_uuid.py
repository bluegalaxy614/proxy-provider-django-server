# Generated by Django 5.1.2 on 2024-10-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0018_usercart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='uuid',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
