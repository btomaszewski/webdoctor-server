# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionthread',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 15, 51, 36, 361733, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
