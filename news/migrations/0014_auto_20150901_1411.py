# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20150901_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='full_titlt',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='full_title',
            field=models.CharField(default=b'', help_text='Optional. Please provide the full title for this research item.', max_length=555, verbose_name=b'full_title'),
            preserve_default=True,
        ),
    ]
