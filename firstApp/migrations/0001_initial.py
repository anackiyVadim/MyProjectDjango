# Generated by Django 5.0.3 on 2024-03-28 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Имя Категории')),
                ('images', models.ImageField(upload_to='catalogImg', verbose_name='Иконка')),
                ('description', models.CharField(max_length=50, verbose_name='Доп. описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tegs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена Товара')),
                ('sale', models.IntegerField(verbose_name='Скидка в %')),
                ('images', models.ImageField(upload_to='productIcon', verbose_name='Картинка Товара')),
                ('tegs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstApp.tegs', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]