# Generated by Django 5.0.3 on 2024-03-30 15:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0004_product_rayting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rayting',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='Рейтинг'),
        ),
    ]