# Generated by Django 3.2 on 2021-05-03 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('cars', '0004_rename_model_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.brand'),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]