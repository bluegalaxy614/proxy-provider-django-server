# Generated by Django 5.1.2 on 2024-11-09 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0049_invoice_purchase_amount_alter_invoice_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='balance_top_up',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.balancetopup'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='type',
            field=models.CharField(choices=[('balance', 'Пополнение баланса'), ('purchase', 'Покупка товара')], db_index=True, default='purchase'),
        ),
    ]