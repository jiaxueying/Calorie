# Generated by Django 3.1 on 2020-11-19 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0014_auto_20201119_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='order',
            new_name='orders',
        ),
    ]
