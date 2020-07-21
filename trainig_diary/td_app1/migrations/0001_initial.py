# Generated by Django 3.0.8 on 2020-07-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDiaryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_part', models.CharField(choices=[('chest', '胸'), ('back', '背中'), ('leg', '足')], max_length=100)),
                ('train_name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('raise_times', models.IntegerField()),
                ('set_times', models.IntegerField()),
                ('date', models.DateField()),
                ('memo', models.TextField()),
            ],
        ),
    ]