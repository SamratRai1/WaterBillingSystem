# Generated by Django 4.0.4 on 2022-05-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='meternum',
            field=models.BigIntegerField(default=None, max_length=200, unique=True),
        ),
    ]
