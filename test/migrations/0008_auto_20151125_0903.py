# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0007_auto_20151124_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmismatchtest',
            name='datetime_started',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 25, 9, 3, 53, 286000)),
        ),
    ]
