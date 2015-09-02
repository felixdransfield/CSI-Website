# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('staff', '0003_auto_20150825_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='contact',
            field=cms.models.fields.PlaceholderField(related_name='contact', slotname=b'staff_contact', editable=False, to='cms.Placeholder', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staffmember',
            name='bio',
            field=cms.models.fields.PlaceholderField(related_name='bio', slotname=b'staff_bio', editable=False, to='cms.Placeholder', null=True),
            preserve_default=True,
        ),
    ]
