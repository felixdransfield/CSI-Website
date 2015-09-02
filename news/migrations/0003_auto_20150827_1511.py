# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_delete_panss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='categories',
            field=models.ForeignKey(related_name='news_items', to='news.NewsCategory', help_text='Please select one or more categories for this news item.'),
            preserve_default=True,
        ),
    ]
