# Generated by Django 3.2.4 on 2021-07-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default='user.jpg', upload_to='photos/profile'),
        ),
    ]