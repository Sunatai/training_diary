# Generated by Django 3.0.8 on 2020-07-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('td_app1', '0004_auto_20200722_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingdiarymodel',
            name='date',
            field=models.DateField(),
        ),
    ]