# Generated by Django 5.0.3 on 2024-05-07 12:55

from django.db import migrations, models
from django.utils.timezone import now

class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderuser',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
