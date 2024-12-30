# Generated by Django 5.1.2 on 2024-10-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0023_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='Main.tag'),
        ),
    ]