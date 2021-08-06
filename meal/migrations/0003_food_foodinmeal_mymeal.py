# Generated by Django 3.2.4 on 2021-07-12 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meal', '0002_mealtypes_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.CharField(max_length=200)),
                ('protien', models.CharField(max_length=200)),
                ('fat', models.CharField(max_length=200)),
                ('carbs', models.CharField(max_length=200)),
                ('foodName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MyMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCalosPerMeal', models.CharField(max_length=200)),
                ('mealDate', models.DateTimeField(auto_now_add=True)),
                ('mealType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.mealtypes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='foodInMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.food')),
                ('meal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.mymeal')),
            ],
        ),
    ]
