# Generated by Django 3.2.4 on 2021-07-14 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0011_totalcalosperday_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='totalcalosperday',
            name='slug',
        ),
    ]