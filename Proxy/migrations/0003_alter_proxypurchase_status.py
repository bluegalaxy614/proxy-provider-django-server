# Generated by Django 5.1.2 on 2024-10-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proxy', '0002_alter_proxypurchase_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxypurchase',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('enabled', 'Enabled'), ('expired', 'Expired')], default='active', max_length=50),
        ),
    ]