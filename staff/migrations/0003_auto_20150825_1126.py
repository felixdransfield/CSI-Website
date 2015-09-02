# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20150825_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmember',
            name='title',
            field=models.CharField(default=b'', help_text='Provide a Job title for this staff member', max_length=128, verbose_name='job title'),
            preserve_default=True,
        ),
    ]
