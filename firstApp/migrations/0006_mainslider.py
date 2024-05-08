# Generated by Django 5.0.3 on 2024-03-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0005_alter_product_rayting'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(max_length=255, null=True, verbose_name='Текст Слайда')),
                ('text2', models.CharField(max_length=255, null=True, verbose_name='Текст Слайда')),
                ('text3', models.CharField(max_length=255, null=True, verbose_name='Текст Слайда')),
                ('image', models.ImageField(upload_to='mainSliderImages', verbose_name='Картанка слайда')),
            ],
            options={
                'verbose_name': 'Главный Слайдер',
                'verbose_name_plural': 'Главный Слайдер',
            },
        ),
    ]