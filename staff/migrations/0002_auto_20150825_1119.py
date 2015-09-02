# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='is_current',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffmember',
            name='title',
            field=models.CharField(default=b'', help_text='Provide a Job title for this staff member', max_length=64, verbose_name='job title'),
            preserve_default=True,
        ),
    ]
