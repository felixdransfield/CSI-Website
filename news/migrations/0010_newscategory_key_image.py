# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('news', '0009_newscategory_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscategory',
            name='key_image',
            field=filer.fields.image.FilerImageField(related_name='category_key_image', blank=True, to='filer.Image', help_text='Optional. Please supply an image, if one is desired. This will be resized automatically.', null=True),
            preserve_default=True,
        ),
    ]
