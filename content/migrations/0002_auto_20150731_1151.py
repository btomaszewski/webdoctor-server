# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentfile',
            name='type',
            field=models.CharField(choices=[('pdf', 'PDF')], max_length=10),
        ),
    ]
