# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150827_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='categories2',
            field=models.ForeignKey(default=1, to='news.NewsCategory'),
            preserve_default=False,
        ),
    ]
