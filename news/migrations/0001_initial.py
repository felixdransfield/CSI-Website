# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.utils.timezone
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0012_auto_20150607_2207'),
        ('staff', '0003_auto_20150825_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArchivePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('show_months', models.BooleanField(default=False, help_text='Check this option to break the archive down into years and months.', verbose_name=b'show months?')),
            ],
            options={
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('name', models.CharField(default=b'', help_text='Please provide a unique name for this news category.', max_length=64, verbose_name=b'category name')),
                ('slug', models.SlugField(default=b'', help_text=b'', max_length=255, verbose_name=b'slug')),
                ('info', cms.models.fields.PlaceholderField(slotname=b'category_info', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
                'verbose_name_plural': 'news categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(default=b'', help_text='Please provide a unique headline for this news item.', max_length=255, verbose_name=b'headline')),
                ('slug', models.SlugField(default=b'', help_text=b'', max_length=255, verbose_name=b'slug')),
                ('announcement', models.BooleanField(default=False, help_text='Check this box to display this item in the Announcements box on the front page.', verbose_name='announcement?')),
                ('announcement_title', models.CharField(default=b'', help_text='Optional. Alternate title to be used in the Announcements Box on the front page.', max_length=255, verbose_name=b'announcement title', blank=True)),
                ('subtitle', models.CharField(default=b'', help_text='Optional. Please provide a unique subtitle for this news item.', max_length=255, verbose_name=b'subtitle', blank=True)),
                ('published', models.BooleanField(default=False, help_text='Check to allow this news post to be publically visible', verbose_name=b'pubished')),
                ('news_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Please provide the date of this news item. Note, setting this to a future date will prevent this news item from appearing until that time.', verbose_name='news date')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
                ('key_image_tooltip', models.CharField(default=b'', help_text=b'', max_length=255, verbose_name=b'key image tooltip', blank=True)),
                ('categories', models.ManyToManyField(help_text='Please select one or more categories for this news item.', related_name='news_items', to='news.NewsCategory')),
                ('key_image', filer.fields.image.FilerImageField(related_name='news_key_image', blank=True, to='filer.Image', help_text='Optional. Please supply an image, if one is desired. This will be resized automatically.', null=True)),
                ('news_body', cms.models.fields.PlaceholderField(slotname=b'news_item_body', editable=False, to='cms.Placeholder', null=True)),
                ('related_staff', models.ManyToManyField(related_name='news_items', to='staff.StaffMember', blank=True, help_text='Optional. Please choose zero or more staff related to this item. Selected staff will automatically get a Publication added that references this news item.', null=True, verbose_name='related staff')),
            ],
            options={
                'ordering': ['-news_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PANSS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating_date', models.DateField(default=django.utils.timezone.now, verbose_name=b'date of rating', blank=True)),
                ('P1', models.IntegerField(default=0, verbose_name=b'P1 - Delusions')),
                ('P2', models.IntegerField(default=0, verbose_name=b'P2 - Conceptual Disorganisation')),
                ('P3', models.IntegerField(default=0, verbose_name=b'P3 - Hallucinatory Behaviour')),
                ('P4', models.IntegerField(default=0, verbose_name=b'P4 - Excitement')),
                ('G15', models.IntegerField(default=0, verbose_name=b'G15 - Preoccupation')),
                ('G16', models.IntegerField(default=0, verbose_name=b'G16 - Active Social Avoidance')),
                ('S1', models.IntegerField(default=0, verbose_name=b'S1 - Anger')),
                ('S2', models.IntegerField(default=0, verbose_name=b'S2 - Difficulty in Delaying Gratification')),
                ('S3', models.IntegerField(default=0, verbose_name=b'S3 - Affective Lability')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecentNewsPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('max_items', models.PositiveIntegerField(default=5, help_text='Please provide the maximum number of items to display (0 means unlimited)', verbose_name=b'max. number')),
            ],
            options={
            },
            bases=('cms.cmsplugin',),
        ),
    ]
