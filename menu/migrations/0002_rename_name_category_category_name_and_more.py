# Generated by Django 5.2 on 2025-05-05 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='category_slug',
        ),
    ]
