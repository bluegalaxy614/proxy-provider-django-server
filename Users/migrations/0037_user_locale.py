# Generated by Django 5.1.2 on 2024-12-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0036_alter_user_referral_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="locale",
            field=models.CharField(default="ru"),
        ),
    ]
