# Generated by Django 5.1.2 on 2024-11-12 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0058_referraltransaction_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referraltransaction',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
