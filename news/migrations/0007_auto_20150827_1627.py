# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_newsitem_categories2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='subtitle',
            field=models.CharField(default=b'', help_text='Optional. Please provide a unique subtitle for this news item.', max_length=555, verbose_name=b'subtitle', blank=True),
            preserve_default=True,
        ),
    ]
