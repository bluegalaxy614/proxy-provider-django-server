# Generated by Django 5.1.2 on 2024-11-04 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0042_alter_product_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductData',
            new_name='AccountData',
        ),
        migrations.AlterModelTable(
            name='accountdata',
            table='accounts_data',
        ),
    ]