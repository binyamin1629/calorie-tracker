# Generated by Django 3.2.4 on 2021-07-06 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodystats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodystatus',
            name='hiegth',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='bodystatus',
            name='weight',
            field=models.IntegerField(default=160),
        ),
    ]
