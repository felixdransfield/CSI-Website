# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0008_auto_20150903_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='file',
            field=models.FileField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
