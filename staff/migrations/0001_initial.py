# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import cms.models.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seniority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(default=b'', help_text='Please provide a label for this seniority', unique=True, max_length=64, verbose_name='label')),
            ],
            options={
                'verbose_name_plural': 'seniorities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('full_name', models.CharField(default=b'', help_text='Please enter a full name for this staff member', unique=True, max_length=64, verbose_name='full name')),
                ('slug', models.SlugField(default=b'', help_text='Provide a unique slug for this staff member', max_length=64, verbose_name='slug')),
                ('bio', cms.models.fields.PlaceholderField(slotname=b'staff_bio', editable=False, to='cms.Placeholder', null=True)),
                ('photo', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', help_text='Optional. Please supply a photo of this staff member.', null=True)),
                ('seniority', models.ForeignKey(default=None, blank=True, to='staff.Seniority', help_text='Please specify a seniority level for this staff member', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
