# Generated by Django 5.0.3 on 2024-05-07 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_orderuser_user_alter_orderuser_created'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderUser',
        ),
    ]
