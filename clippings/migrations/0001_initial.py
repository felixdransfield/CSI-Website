# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('staff', '0003_auto_20150825_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('title', models.CharField(default=b'', help_text='Please provide a title for this clipping.', max_length=255, verbose_name=b'title', blank=True)),
                ('source', models.CharField(default=b'', help_text='Please provide a source for this clipping.', max_length=255, verbose_name=b'source', blank=True)),
                ('external_link', models.CharField(default=b'', help_text='Provide an external link.', max_length=2048, verbose_name='external link', blank=True)),
                ('download', filer.fields.file.FilerFileField(blank=True, to='filer.File', help_text='Provide a file download. This overrides research items and external links.', null=True)),
                ('staff', models.ForeignKey(related_name='clippings', default=None, to='staff.StaffMember', help_text='Required. To whom is this clipping connected?')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
