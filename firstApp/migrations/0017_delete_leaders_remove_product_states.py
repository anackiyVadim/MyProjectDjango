# Generated by Django 5.0.3 on 2024-03-30 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0016_product_states'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Leaders',
        ),
        migrations.RemoveField(
            model_name='product',
            name='states',
        ),
    ]