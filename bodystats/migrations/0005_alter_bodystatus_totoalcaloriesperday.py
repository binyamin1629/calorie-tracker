# Generated by Django 3.2.4 on 2021-07-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodystats', '0004_bodystatus_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodystatus',
            name='totoalCaloriesPerDay',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
