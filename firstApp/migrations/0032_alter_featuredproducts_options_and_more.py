# Generated by Django 5.0.3 on 2024-04-12 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0031_remove_profile_featuredproducts_featuredproducts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='featuredproducts',
            options={'verbose_name': 'Избран. тов.', 'verbose_name_plural': 'Избран. тов.'},
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='featuredProducts_Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='firstApp.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='featuredProducts_User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='firstApp.profile', verbose_name='Пользователь'),
        ),
    ]