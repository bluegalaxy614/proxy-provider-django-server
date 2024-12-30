# Generated by Django 5.1.2 on 2024-11-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0062_remove_adminaction_response_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='data_file',
            field=models.FileField(blank=True, null=True, upload_to='products_data'),
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='data_file',
        ),
    ]