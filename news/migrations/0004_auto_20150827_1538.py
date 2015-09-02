# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150827_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='categories',
            field=models.ManyToManyField(help_text='Please select one or more categories for this news item.', related_name='news_items', to='news.NewsCategory'),
            preserve_default=True,
        ),
    ]
