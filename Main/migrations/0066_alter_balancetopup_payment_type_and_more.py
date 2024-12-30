# Generated by Django 5.1.2 on 2024-12-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0065_balancetopup_txid_purchase_txid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="balancetopup",
            name="payment_type",
            field=models.CharField(
                choices=[
                    ("balance", "Баланс аккаунта"),
                    ("crypto", "Криптовалютой"),
                    ("cryptomus", "Криптовалютой через Cryptomus"),
                    ("bonus", "Bonus from Gemups"),
                ],
                default="cryptomus",
            ),
        ),
        migrations.AlterField(
            model_name="purchase",
            name="payment_type",
            field=models.CharField(
                choices=[
                    ("balance", "Баланс аккаунта"),
                    ("crypto", "Криптовалютой"),
                    ("cryptomus", "Криптовалютой через Cryptomus"),
                    ("bonus", "Bonus from Gemups"),
                ],
                default="cryptomus",
            ),
        ),
    ]