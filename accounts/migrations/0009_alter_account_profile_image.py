# Generated by Django 3.2.4 on 2021-07-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_account_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default='user.png', upload_to='photos/profile'),
        ),
    ]
