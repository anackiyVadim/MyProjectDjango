# Generated by Django 5.0.3 on 2024-04-19 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0040_alter_productimagesdescr_options_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='product',
        ),
    ]