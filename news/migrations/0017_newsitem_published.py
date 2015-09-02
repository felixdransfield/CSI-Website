# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_remove_newsitem_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='published',
            field=models.BooleanField(default=False, help_text='Check to allow this news post to be publically visible', verbose_name=b'published'),
            preserve_default=True,
        ),
    ]
