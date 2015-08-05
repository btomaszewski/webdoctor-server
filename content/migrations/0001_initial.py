# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(validators=[content.models.name_validator], max_length=200)),
                ('version', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('pdf', 'PDF'), ('txt', 'Raw Text')], max_length=10)),
                ('file', models.FileField(validators=[content.models.file_validator], upload_to='./%Y-%m/')),
            ],
        ),
    ]
