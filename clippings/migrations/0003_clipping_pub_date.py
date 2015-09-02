# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clippings', '0002_clipping_news_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='clipping',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'date of publication', blank=True),
            preserve_default=True,
        ),
    ]
