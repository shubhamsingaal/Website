# Generated by Django 3.2.9 on 2022-07-18 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(13, 10, 15, 933253)),
        ),
    ]
