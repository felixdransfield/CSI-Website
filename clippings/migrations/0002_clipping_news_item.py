# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('clippings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clipping',
            name='news_item',
            field=models.ForeignKey(default=None, blank=True, to='news.NewsItem', help_text='Select a Research Item. This overrides external links.', null=True),
            preserve_default=True,
        ),
    ]
