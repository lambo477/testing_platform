# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0009_auto_20151125_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='datetime_started',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 10, 22, 58, 356000)),
        ),
    ]
