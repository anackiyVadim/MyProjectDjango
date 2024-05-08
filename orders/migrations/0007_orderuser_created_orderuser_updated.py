# Generated by Django 5.0.3 on 2024-05-07 13:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_orderuser_created_remove_orderuser_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderuser',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orderuser',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
