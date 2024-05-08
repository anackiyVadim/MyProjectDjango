# Generated by Django 5.0.3 on 2024-03-30 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0010_leaders_alter_product_states_delete_leadersofsells'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='states',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstApp.leaders', verbose_name='Лидер продаж?'),
            preserve_default=False,
        ),
    ]