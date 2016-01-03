# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClockGuardModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_url', models.TextField(unique=True)),
                ('page_name', models.TextField(default=None)),
                ('page_start_time', models.IntegerField()),
                ('page_end_time', models.IntegerField()),
            ],
        ),
    ]
