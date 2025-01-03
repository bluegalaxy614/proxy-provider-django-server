# Generated by Django 5.1.2 on 2024-10-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0018_usercart'),
        ('Users', '0006_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='products_cart',
            field=models.ManyToManyField(through='Main.UserCart', to='Main.product'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('temp_user', 'Временный пользователь'), ('seller', 'Продавец'), ('admin', 'Администратор сайта'), ('root-admin', 'ГА сайта')], default='user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
