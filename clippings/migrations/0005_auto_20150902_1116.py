# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('news', '0021_auto_20150901_1551'),
        ('staff', '0004_auto_20150901_1033'),
        ('clippings', '0004_auto_20150902_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('title', models.CharField(default=b'', help_text='Please provide a title for this clipping.', max_length=255, verbose_name=b'title', blank=True)),
                ('pub_date', models.DateField(default=django.utils.timezone.now, verbose_name=b'date of publication', blank=True)),
                ('source', models.CharField(default=b'', help_text='Please provide a source for this clipping.', max_length=255, verbose_name=b'source', blank=True)),
                ('external_link', models.CharField(default=b'', help_text='Provide an external link.', max_length=2048, verbose_name='external link', blank=True)),
                ('download', filer.fields.file.FilerFileField(blank=True, to='filer.File', help_text='Provide a file download. This overrides research items and external links.', null=True)),
                ('news_item', models.ForeignKey(default=None, blank=True, to='news.NewsItem', help_text='Select a Research Item. This overrides external links.', null=True)),
                ('staff', models.ForeignKey(related_name='clippings', default=None, to='staff.StaffMember', help_text='Required. To whom is this clipping connected?')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='publication',
            name='download',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='news_item',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='staff',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
