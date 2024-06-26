# Generated by Django 5.0.3 on 2024-04-12 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0030_basketofgoods_totalprice_alter_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='featuredProducts',
        ),
        migrations.CreateModel(
            name='featuredProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featuredProducts_Product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='firstApp.product')),
                ('featuredProducts_User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='firstApp.profile')),
            ],
            options={
                'verbose_name': 'История заказов',
                'verbose_name_plural': 'История заказов',
            },
        ),
    ]
