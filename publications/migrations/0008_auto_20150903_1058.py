# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0007_auto_20150903_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='staff',
            field=models.ForeignKey(related_name='publications', default=None, to='staff.StaffMember', help_text='Required. To whom is this publication connected?'),
            preserve_default=True,
        ),
    ]
