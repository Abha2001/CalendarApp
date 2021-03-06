# Generated by Django 3.0.3 on 2020-03-10 10:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0003_auto_20200308_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(default=datetime.date(2020, 3, 10)),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
