# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_newsitem_funding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='funding',
            field=models.CharField(help_text='Optional: information on who is funding this research', max_length=240, verbose_name=b'funding', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='published',
            field=models.BooleanField(default=True, help_text='Check to allow this news post to be publically visible', verbose_name=b'published'),
            preserve_default=True,
        ),
    ]
