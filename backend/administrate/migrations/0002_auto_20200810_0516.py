# Generated by Django 3.1 on 2020-08-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiration',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
