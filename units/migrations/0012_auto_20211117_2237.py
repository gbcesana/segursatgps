# Generated by Django 3.1.3 on 2021-11-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0011_auto_20210904_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='ignition_source',
            field=models.CharField(default='ignition', max_length=50),
        ),
        migrations.AddField(
            model_name='device',
            name='panic_source',
            field=models.CharField(default='panic', max_length=50),
        ),
    ]
