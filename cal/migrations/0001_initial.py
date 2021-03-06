# Generated by Django 3.0.3 on 2020-03-01 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.date(2020, 3, 1))),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('notes', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
    ]
