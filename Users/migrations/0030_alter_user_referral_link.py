# Generated by Django 5.1.2 on 2024-11-11 20:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0029_user_referral_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referral_link',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]