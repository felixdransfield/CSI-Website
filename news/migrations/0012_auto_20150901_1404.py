# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20150901_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='headline',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='title',
            field=models.CharField(default=b'', help_text='Please provide a title for the Research item (usually and acronym', max_length=255, verbose_name=b'title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='slug',
            field=models.SlugField(default=b'', help_text=b'the slugg that will be the url for this research item', max_length=255, verbose_name=b'slug'),
            preserve_default=True,
        ),
    ]
