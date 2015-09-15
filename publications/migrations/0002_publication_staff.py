# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20150901_1033'),
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='staff',
            field=models.ForeignKey(default=1, to='staff.StaffMember'),
            preserve_default=False,
        ),
    ]
