# Generated by Django 3.0.8 on 2020-07-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('td_app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingdiarymodel',
            name='body_part',
            field=models.CharField(choices=[('info', '胸'), ('primary', '背中'), ('success', '足')], max_length=100),
        ),
    ]