# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20150901_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='published',
        ),
    ]
