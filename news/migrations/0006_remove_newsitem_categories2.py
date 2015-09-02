# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_newsitem_categories2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='categories2',
        ),
    ]
