# Generated by Django 3.2 on 2021-04-29 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210412_2339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Model',
            new_name='Car',
        ),
    ]
