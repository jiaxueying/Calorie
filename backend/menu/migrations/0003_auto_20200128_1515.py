# Generated by Django 3.0.2 on 2020-01-28 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200128_0849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dishorder',
            old_name='amount',
            new_name='mass',
        ),
    ]
