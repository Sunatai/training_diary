# Generated by Django 3.0.8 on 2020-07-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('td_app1', '0006_auto_20200728_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingdiarymodel',
            name='author',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainingdiarymodel',
            name='memo',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]