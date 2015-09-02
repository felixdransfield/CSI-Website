# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_newsitem_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='funding',
            field=models.CharField(help_text='information on who is funding this research', max_length=240, verbose_name=b'funding', blank=True),
            preserve_default=True,
        ),
    ]
