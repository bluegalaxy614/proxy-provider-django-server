# Generated by Django 5.1.2 on 2024-12-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0064_referraltransaction_transaction"),
    ]

    operations = [
        migrations.AddField(
            model_name="balancetopup",
            name="txid",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="purchase",
            name="txid",
            field=models.TextField(blank=True, null=True),
        ),
    ]
