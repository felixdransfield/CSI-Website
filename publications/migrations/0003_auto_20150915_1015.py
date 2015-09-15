# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_publication_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='staff',
            field=models.ForeignKey(related_name='publications', to='staff.StaffMember'),
        ),
    ]
