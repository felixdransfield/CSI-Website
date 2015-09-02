# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='age',
            field=models.IntegerField(verbose_name=b'Age'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participation',
            name='phone',
            field=models.IntegerField(verbose_name=b'Telephone Number'),
            preserve_default=True,
        ),
    ]
