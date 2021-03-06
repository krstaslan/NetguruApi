# Generated by Django 4.0 on 2021-12-24 23:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='avg_rating',
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.TextField(max_length=20, unique=True),
        ),
    ]
