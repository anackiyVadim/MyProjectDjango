# Generated by Django 5.0.3 on 2024-03-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0015_remove_product_states'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='states',
            field=models.CharField(default=10, max_length=10, verbose_name='Test'),
            preserve_default=False,
        ),
    ]
