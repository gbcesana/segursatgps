# Generated by Django 3.1.3 on 2022-04-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20220407_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_superadmin',
            field=models.BooleanField(default=False),
        ),
    ]
