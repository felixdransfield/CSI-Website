# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('news', '0008_remove_newscategory_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscategory',
            name='info',
            field=cms.models.fields.PlaceholderField(slotname=b'category_info', editable=False, to='cms.Placeholder', null=True),
            preserve_default=True,
        ),
    ]
