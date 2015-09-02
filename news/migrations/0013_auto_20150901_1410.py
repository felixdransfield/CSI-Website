# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20150901_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='full_titlt',
            field=models.CharField(default=b'', help_text='Optional. Please provide the full title for this research item.', max_length=555, verbose_name=b'subtitle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='published',
            field=models.BooleanField(default=False, help_text='Check to allow this news post to be publically visible', verbose_name=b'published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='slug',
            field=models.SlugField(default=b'', help_text=b'the slug that will be the url for this research item', max_length=255, verbose_name=b'slug'),
            preserve_default=True,
        ),
    ]
