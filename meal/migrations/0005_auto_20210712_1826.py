# Generated by Django 3.2.4 on 2021-07-12 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0004_auto_20210712_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodinmeal',
            name='totalCalosPerMeal',
        ),
        migrations.AddField(
            model_name='mymeal',
            name='totalCalosPerMeal',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
