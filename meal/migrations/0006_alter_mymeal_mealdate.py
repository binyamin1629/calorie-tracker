# Generated by Django 3.2.4 on 2021-07-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0005_auto_20210712_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymeal',
            name='mealDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
