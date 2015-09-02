# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_auto_20150901_1423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ['-start_date']},
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='news_date',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Please provide the date that this study started the default is the current time ', verbose_name='research start date'),
            preserve_default=True,
        ),
    ]
