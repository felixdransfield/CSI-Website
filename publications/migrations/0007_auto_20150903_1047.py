# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_auto_20150903_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='download',
            field=filer.fields.file.FilerFileField(blank=True, to='filer.File', help_text='Provide a file download. this will override an external link if given.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='external_link',
            field=models.CharField(default=b'', help_text='Provide an external link to the publication.', max_length=2048, verbose_name='external link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='source',
            field=models.CharField(default=b'', help_text='Please provide a the name of the journal it was published in.', max_length=255, verbose_name=b'source', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='staff',
            field=models.ForeignKey(related_name='clippings', default=None, to='staff.StaffMember', help_text='Required. To whom is this publication connected?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(default=b'', help_text='Please provide a title for this publication.', max_length=255, verbose_name=b'title', blank=True),
            preserve_default=True,
        ),
    ]
